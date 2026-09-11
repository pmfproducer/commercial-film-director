#!/usr/bin/env python3
"""HTTP integration tests with real runtime state and an explicit runner test double."""
from __future__ import annotations

import hashlib
import http.client
import io
import json
import tempfile
import threading
import unittest
import zipfile
from pathlib import Path
from urllib.parse import quote

import project_runtime as runtime
from dashboard import DashboardServer
from dashboard_store import ProjectStore


class RunnerDouble:
    """Tests HTTP job locking only; does not claim agent execution."""
    def __init__(self):
        self.active = False
    def capability(self):
        return {"available": False, "authenticated": False, "message": "HTTP test double"}
    def status(self, root):
        return {"busy": self.active, "active_job": {"status": "running"} if self.active else None, "last_job": None}
    def get_jobs(self, root):
        return []
    def chat(self, root):
        return []
    def start(self, root, text, mode="phase"):
        self.active = True
        return {"id": "test-job", "status": "running", "mode": mode}
    def cancel(self, root, job_id=None):
        self.active = False
        return {"cancelled": True, "busy": False}


class DashboardHTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix="cfd-dashboard-test-")
        cls.base = Path(cls.temporary.name)
        cls.store = ProjectStore(cls.base / "projects")
        cls.runner = RunnerDouble()
        cls.server = DashboardServer(("127.0.0.1", 0), cls.store, runner=cls.runner)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.origin = cls.server.origin
        cls.token = cls.server.csrf

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)
        cls.temporary.cleanup()

    def setUp(self):
        self.runner.active = False
        status, _, created = self.request("POST", "/api/projects", {"name": self.id().rsplit(".", 1)[-1], "client": "Marca de teste", "brief": "Filme de vinte segundos, uma pessoa e uma locação. Sem promessas de resultado."})
        self.assertEqual(status, 201, created)
        self.project_id = created["id"]
        self.project = created["project"]
        self.root = Path(self.project["path"])
        self.prefix = f"/api/projects/{self.project_id}"

    def request(self, method, path, body=None, headers=None):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=10)
        supplied = {}
        data = None
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            supplied.update({"Content-Type": "application/json", "Origin": self.origin, "X-CSRF-Token": self.token})
        supplied.update(headers or {})
        connection.request(method, path, body=data, headers=supplied)
        response = connection.getresponse()
        raw = response.read()
        content_type = response.getheader("Content-Type", "")
        result = json.loads(raw) if content_type.startswith("application/json") else raw
        result_headers = dict(response.getheaders())
        status = response.status
        connection.close()
        return status, result_headers, result

    def document(self, name="01_BRIEF_ESTRATEGICO.md"):
        status, _, result = self.request("GET", self.prefix + "/document?path=" + quote(name))
        self.assertEqual(status, 200, result)
        return result

    def test_bootstrap_create_and_state_are_real(self):
        status, _, bootstrap = self.request("GET", "/api/bootstrap")
        self.assertEqual(status, 200)
        self.assertEqual(bootstrap["csrf"], self.token)
        self.assertTrue(any(p["id"] == self.project_id for p in bootstrap["projects"]))
        status, _, detail = self.request("GET", self.prefix)
        self.assertEqual(status, 200)
        self.assertEqual(len(detail["phases"]), 12)
        self.assertEqual(detail["state"], json.loads((self.root / runtime.STATE_NAME).read_text()))
        self.assertEqual(detail["state"]["execution_mode"], "MULTI_AGENT")
        self.assertEqual(detail["tasks"], [])
        self.assertTrue((self.root / "inputs/briefing.md").is_file())
        self.assertIn("inputs/briefing.md", (self.root / "00_SOURCE_MANIFEST.md").read_text())
        self.assertEqual(detail["state"]["source_materials"][0]["path"], "inputs/briefing.md")

    def test_register_existing_project_is_idempotent_and_checks_state(self):
        status, _, registered = self.request("POST", "/api/projects/register", {"path": str(self.root)})
        self.assertEqual(status, 200)
        self.assertEqual(registered["id"], self.project_id)
        external = self.base / "external"
        external.mkdir(exist_ok=True)
        self.store.run("init", project="Projeto externo", client="Cliente", output=external, directory_name="external-project")
        status, _, registered = self.request("POST", "/api/projects/register", {"path": str(external / "external-project")})
        self.assertEqual(status, 200, registered)
        self.assertEqual(registered["project"]["name"], "Projeto externo")
        status, _, error = self.request("POST", "/api/projects/register", {"path": str(self.base)})
        self.assertEqual(status, 404)
        self.assertIn("error", error)

    def test_editor_cas_history_and_change_control(self):
        original = self.document()
        # Explicit synthetic completion fixture tests change-control semantics only.
        state = json.loads((self.root / runtime.STATE_NAME).read_text())
        first = runtime.PHASES[0]["id"]
        state["phases"][first]["status"] = "COMPLETE_DRAFT"
        state["artifact_registry"][original["path"]] = {"status": "COMPLETE_DRAFT", "sha256": original["sha256"]}
        runtime.save_state(self.root, state)
        changed = original["content"] + "\nAjuste explícito de escopo do teste.\n"
        payload = {"path": original["path"], "content": changed, "sha256": original["sha256"], "reason": "Atualização do briefing"}
        status, _, saved = self.request("POST", self.prefix + "/document", payload)
        self.assertEqual(status, 200, saved)
        self.assertEqual(saved["revised_from"], first)
        self.assertEqual(saved["sha256"], hashlib.sha256(changed.encode()).hexdigest())
        state = json.loads((self.root / runtime.STATE_NAME).read_text())
        self.assertEqual(state["phases"][first]["status"], "REVISE")
        self.assertEqual(state["artifact_registry"][original["path"]]["status"], "STALE")
        history = list((self.root / ".dashboard/edits").glob("*.json"))
        self.assertEqual(len(history), 1)
        self.assertEqual(json.loads(history[0].read_text())["previous_content"], original["content"])
        status, _, error = self.request("POST", self.prefix + "/document", payload)
        self.assertEqual(status, 409, error)
        self.assertEqual((self.root / original["path"]).read_text(), changed)

    def test_readonly_state_and_submissions(self):
        doc = self.document(runtime.STATE_NAME)
        self.assertFalse(doc["editable"])
        status, _, _ = self.request("POST", self.prefix + "/document", {"path": doc["path"], "content": "{}", "sha256": doc["sha256"], "reason": "Teste"})
        self.assertEqual(status, 403)
        report = self.root / "departments/research/parecer.md"
        report.write_text("Parecer de teste somente leitura.")
        doc = self.document("departments/research/parecer.md")
        self.assertFalse(doc["editable"])
        self.assertEqual(doc["content"], report.read_text())

    def test_incomplete_approval_refused_by_runtime(self):
        before = (self.root / runtime.STATE_NAME).read_bytes()
        status, _, error = self.request("POST", self.prefix + "/approve", {"phase": runtime.PHASES[0]["id"], "by": "Pessoa teste", "note": "Tentativa prematura"})
        self.assertEqual(status, 409, error)
        self.assertIn("não está concluída", error["error"])
        self.assertEqual(before, (self.root / runtime.STATE_NAME).read_bytes())

    def test_real_revision_command(self):
        status, _, result = self.request("POST", self.prefix + "/revise", {"phase": runtime.PHASES[0]["id"], "reason": "Rever restrição de produção"})
        self.assertEqual(status, 200, result)
        self.assertEqual(result["state"]["revision_log"][-1]["type"], "CHANGE_CONTROL")
        self.assertEqual(result["state"]["revision_log"][-1]["reason"], "Rever restrição de produção")

    def test_zip_contains_project_only_and_blocks_sensitive_paths(self):
        (self.root / ".env").write_text("SECRET=not-to-export")
        (self.root / "auth.json").write_text("private")
        (self.root / ".dashboard").mkdir(exist_ok=True)
        (self.root / ".dashboard/private.log").write_text("not-to-export")
        outside = self.base / "outside-secret.txt"
        outside.write_text("outside")
        (self.root / "escape.txt").symlink_to(outside)
        status, headers, payload = self.request("GET", self.prefix + "/export")
        self.assertEqual(status, 200)
        self.assertIn("attachment", headers["Content-Disposition"])
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            names = archive.namelist()
            self.assertIn(self.root.name + "/" + runtime.STATE_NAME, names)
            self.assertIn(self.root.name + "/inputs/briefing.md", names)
            self.assertFalse(any(".dashboard" in p or ".env" in p or "auth.json" in p or "escape.txt" in p for p in names))
            self.assertTrue(all(p.startswith(self.root.name + "/") for p in names))
        for path in ["../outside-secret.txt", ".env", "auth.json", "escape.txt", "/etc/passwd", ".dashboard/private.log"]:
            status, _, _ = self.request("GET", self.prefix + "/document?path=" + quote(path, safe=""))
            self.assertEqual(status, 403, path)
        status, _, _ = self.request("GET", f"/artifacts/{self.project_id}/%2e%2e/outside-secret.txt")
        self.assertEqual(status, 403)

    def test_csrf_host_origin_protection(self):
        payload = {"phase": runtime.PHASES[0]["id"], "reason": "Teste"}
        for headers in [{"X-CSRF-Token": "wrong"}, {"Origin": "https://evil.invalid"}, {"Origin": "null"}, {"Origin": ""}, {"Host": "evil.invalid"}]:
            status, _, error = self.request("POST", self.prefix + "/revise", payload, headers=headers)
            self.assertEqual(status, 403, error)
        status, _, _ = self.request("GET", "/api/bootstrap", headers={"Host": "evil.invalid"})
        self.assertEqual(status, 403)
        status, _, _ = self.request("GET", "/api/bootstrap", headers={"Origin": "null"})
        self.assertEqual(status, 403)

    def test_jobs_block_editor_approve_and_export_until_cancel(self):
        doc = self.document()
        status, _, job = self.request("POST", self.prefix + "/message", {"text": "Desenvolva a fase", "mode": "phase"})
        self.assertEqual(status, 200, job)
        status, _, jobs = self.request("GET", self.prefix + "/jobs")
        self.assertEqual(status, 200)
        self.assertTrue(jobs["job"]["busy"])
        for action, payload in [("document", {"path": doc["path"], "content": "Alteração", "sha256": doc["sha256"], "reason": "Teste"}), ("approve", {"phase": runtime.PHASES[0]["id"], "by": "Pessoa"}), ("revise", {"phase": runtime.PHASES[0]["id"], "reason": "Teste"})]:
            status, _, _ = self.request("POST", self.prefix + "/" + action, payload)
            self.assertEqual(status, 409)
        status, _, _ = self.request("GET", self.prefix + "/export")
        self.assertEqual(status, 409)
        status, _, _ = self.request("POST", self.prefix + "/cancel", {})
        self.assertEqual(status, 200)
        self.assertFalse(self.runner.active)

    def test_artifacts_sandbox_relative_media_and_range(self):
        folder = self.root / "storyboard"
        (folder / "board.html").write_text('<img src="frame.svg"><script>window.test=true</script>')
        (folder / "frame.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"></svg>')
        status, headers, body = self.request("GET", f"/artifacts/{self.project_id}/storyboard/board.html")
        self.assertEqual(status, 200)
        self.assertIn("sandbox allow-scripts", headers["Content-Security-Policy"])
        self.assertNotIn("allow-same-origin", headers["Content-Security-Policy"])
        self.assertIn("connect-src 'none'", headers["Content-Security-Policy"])
        status, _, _ = self.request("GET", f"/artifacts/{self.project_id}/storyboard/frame.svg")
        self.assertEqual(status, 200)
        (folder / "clip.mp4").write_bytes(bytes(range(200)))
        status, headers, body = self.request("GET", f"/artifacts/{self.project_id}/storyboard/clip.mp4", headers={"Range": "bytes=10-19"})
        self.assertEqual(status, 206)
        self.assertEqual(body, bytes(range(10, 20)))
        self.assertEqual(headers["Content-Range"], "bytes 10-19/200")


if __name__ == "__main__":
    unittest.main(verbosity=2)
