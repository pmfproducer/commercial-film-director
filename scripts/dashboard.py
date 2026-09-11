#!/usr/bin/env python3
"""Run the local Commercial Film Director dashboard (Python standard library)."""
from __future__ import annotations

import argparse
import hmac
import json
import mimetypes
import re
import secrets
import sys
import tempfile
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

from dashboard_store import DashboardError, ProjectStore, project_file

SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROJECTS_DIR = Path.home() / "Documents" / "Commercial Film Director" / "projects"
UI_CSP = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; media-src 'self' blob:; connect-src 'self'; frame-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'"
ARTIFACT_CSP = "sandbox allow-scripts; default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src 'self' data: blob:; media-src 'self' blob:; font-src data:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'self'"
MAX_BODY = 3 * 1024 * 1024


class UnavailableRunner:
    def capability(self):
        return {"available": False, "reason": "A ponte com o Codex não está disponível nesta instalação."}
    def status(self, project_root):
        return None
    def get_jobs(self, project_root):
        return []
    def chat(self, project_root):
        return []
    def start(self, project_root, text, mode="phase"):
        raise DashboardError("A execução de agentes não está disponível nesta instalação.", 409)
    def cancel(self, project_root, job_id=None):
        raise DashboardError("Não há execução disponível para cancelar.", 409)


def default_runner(codex_binary=None):
    try:
        from dashboard_bridge import JobManager
    except ImportError:
        return UnavailableRunner()
    return JobManager(skill_root=SKILL_ROOT, codex_binary=codex_binary)


def busy(job) -> bool:
    if not isinstance(job, dict):
        return False
    if "busy" in job:
        return bool(job["busy"])
    return str(job.get("status", job.get("state", ""))).lower() in {"running", "starting", "queued", "cancelling"}


class DashboardServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address, store: ProjectStore, runner=None, initial_project_id=None):
        self.store = store
        self.runner = default_runner() if runner is None else runner
        self.csrf = secrets.token_urlsafe(32)
        self.initial_project_id = initial_project_id
        super().__init__(address, DashboardHandler)

    @property
    def origin(self):
        return f"http://127.0.0.1:{self.server_port}"


class DashboardHandler(BaseHTTPRequestHandler):
    server_version = "CommercialFilmDirector/6.1"

    def log_message(self, format, *args):
        # File names, briefings, tokens and chat messages are not written to logs.
        pass

    def _security(self, *, mutation=False):
        allowed_hosts = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        hosts = self.headers.get_all("Host", [])
        if len(hosts) != 1 or hosts[0] not in allowed_hosts:
            raise DashboardError("Host não permitido. Abra o endereço local mostrado no terminal.", 403)
        origin = self.headers.get("Origin")
        allowed_origins = {f"http://{host}" for host in allowed_hosts}
        if origin is not None and origin not in allowed_origins:
            raise DashboardError("Origem não permitida.", 403)
        if self.headers.get("Sec-Fetch-Site") == "cross-site":
            raise DashboardError("Requisição externa não permitida.", 403)
        if mutation:
            if origin not in allowed_origins:
                raise DashboardError("A origem local é obrigatória para alterar o projeto.", 403)
            tokens = self.headers.get_all("X-CSRF-Token", [])
            if len(tokens) != 1 or not hmac.compare_digest(tokens[0], self.server.csrf):
                raise DashboardError("Sessão do painel expirou. Recarregue a página.", 403)

    def _headers(self, status, mime, length=None, *, artifact=False, extras=None):
        self.send_response(status)
        self.send_header("Content-Type", mime)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Security-Policy", ARTIFACT_CSP if artifact else UI_CSP)
        if not artifact:
            self.send_header("X-Frame-Options", "DENY")
        if length is not None:
            self.send_header("Content-Length", str(length))
        for key, value in (extras or {}).items():
            self.send_header(key, value)
        self.end_headers()

    def _json(self, value, status=200):
        data = (json.dumps(value, ensure_ascii=False) + "\n").encode("utf-8")
        self._headers(status, "application/json; charset=utf-8", len(data))
        if self.command != "HEAD":
            self.wfile.write(data)

    def _body(self):
        if self.headers.get("Transfer-Encoding"):
            raise DashboardError("Formato de requisição não aceito.")
        if self.headers.get("Content-Type", "").split(";", 1)[0].strip() != "application/json":
            raise DashboardError("Envie o conteúdo em JSON.", 415)
        lengths = self.headers.get_all("Content-Length", [])
        if len(lengths) != 1:
            raise DashboardError("Tamanho de requisição obrigatório.", 411)
        try:
            size = int(lengths[0])
        except ValueError:
            raise DashboardError("Tamanho de requisição inválido.") from None
        if size < 0 or size > MAX_BODY:
            raise DashboardError("Conteúdo maior que o limite de 3 MB.", 413)
        try:
            value = json.loads(self.rfile.read(size).decode("utf-8"))
        except (UnicodeError, ValueError):
            raise DashboardError("JSON inválido.") from None
        if not isinstance(value, dict):
            raise DashboardError("O corpo da requisição precisa ser um objeto JSON.")
        return value

    def _send_file(self, path: Path, *, artifact=False):
        if not path.is_file():
            raise DashboardError("Arquivo não encontrado.", 404)
        mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
        if mime.startswith("text/") or mime in {"application/javascript", "application/json", "image/svg+xml"}:
            mime += "; charset=utf-8"
        size = path.stat().st_size
        first, last = 0, size - 1
        extras = {"Accept-Ranges": "bytes"}
        status = 200
        value = self.headers.get("Range")
        if value and size:
            match = re.fullmatch(r"bytes=(\d*)-(\d*)", value)
            if not match or not any(match.groups()):
                raise DashboardError("Intervalo de arquivo inválido.", 416)
            start_text, end_text = match.groups()
            if start_text:
                first = int(start_text)
                last = min(int(end_text), size - 1) if end_text else size - 1
            else:
                first = max(0, size - int(end_text))
            if first > last or first >= size:
                raise DashboardError("Intervalo de arquivo indisponível.", 416)
            status = 206
            extras["Content-Range"] = f"bytes {first}-{last}/{size}"
        length = max(0, last - first + 1)
        self._headers(status, mime, length, artifact=artifact, extras=extras)
        if self.command == "HEAD":
            return
        with path.open("rb") as source:
            source.seek(first)
            remaining = length
            while remaining:
                chunk = source.read(min(65536, remaining))
                if not chunk:
                    break
                self.wfile.write(chunk)
                remaining -= len(chunk)

    def _get(self):
        self._security()
        parsed = urlsplit(self.path)
        path = unquote(parsed.path)
        query = parse_qs(parsed.query)
        if path in {"/", "/index.html"}:
            return self._send_file(SKILL_ROOT / "assets" / "dashboard" / "index.html")
        if path in {"/app.js", "/styles.css", "/assets/app.js", "/assets/styles.css"}:
            return self._send_file(SKILL_ROOT / "assets" / "dashboard" / path.rsplit("/", 1)[-1])
        if path.startswith("/assets/dashboard/"):
            relative = path[len("/assets/dashboard/"):]
            return self._send_file(project_file(SKILL_ROOT / "assets" / "dashboard", relative))
        if path == "/example":
            return self._send_file(SKILL_ROOT / "examples" / "REMENDA_ROUGHBOARD.html", artifact=True)
        if path == "/api/bootstrap":
            return self._json({"csrf": self.server.csrf, "projects": self.server.store.projects(), "runner": self.server.runner.capability(), "default_projects_dir": str(self.server.store.projects_dir), "initial_project_id": self.server.initial_project_id})
        if path == "/api/projects":
            return self._json({"projects": self.server.store.projects()})
        artifact_match = re.fullmatch(r"/artifacts/([a-f0-9]{32})/(.+)", path)
        if artifact_match:
            project_id, relative = artifact_match.groups()
            root = self.server.store.root(project_id)
            return self._send_file(project_file(root, relative), artifact=True)
        match = re.fullmatch(r"/api/projects/([a-f0-9]{32})(?:/(document|export|jobs))?", path)
        if not match:
            raise DashboardError("Recurso não encontrado.", 404)
        project_id, action = match.groups()
        root = self.server.store.root(project_id)
        if action == "document":
            return self._json(self.server.store.document(project_id, query.get("path", [""])[0]))
        if action == "jobs":
            return self._json({"jobs": self.server.runner.get_jobs(root), "chat": self.server.runner.chat(root), "job": self.server.runner.status(root)})
        if action == "export":
            with self.server.store.lock(project_id):
                if busy(self.server.runner.status(root)):
                    raise DashboardError("Aguarde ou cancele a execução antes de exportar.", 409)
                with tempfile.TemporaryFile() as output:
                    self.server.store.export(project_id, output)
                    size = output.tell()
                    output.seek(0)
                    self._headers(200, "application/zip", size, extras={"Content-Disposition": 'attachment; filename="commercial-film-project.zip"'})
                    if self.command != "HEAD":
                        while True:
                            chunk = output.read(65536)
                            if not chunk:
                                break
                            self.wfile.write(chunk)
            return
        value = self.server.store.detail(project_id)
        value["chat"] = self.server.runner.chat(root)
        value["job"] = self.server.runner.status(root)
        return self._json(value)

    def _post(self):
        self._security(mutation=True)
        body = self._body()
        path = unquote(urlsplit(self.path).path)
        if path == "/api/projects":
            project = self.server.store.create(body.get("name"), body.get("client", ""), body.get("brief"))
            return self._json({"project": project, "id": project["id"]}, 201)
        if path == "/api/projects/register":
            project = self.server.store.register(body.get("path"))
            return self._json({"project": project, "id": project["id"]})
        match = re.fullmatch(r"/api/projects/([a-f0-9]{32})/(document|approve|revise|message|cancel)", path)
        if not match:
            raise DashboardError("Recurso não encontrado.", 404)
        project_id, action = match.groups()
        with self.server.store.lock(project_id):
            root = self.server.store.root(project_id)
            if action != "cancel" and busy(self.server.runner.status(root)):
                raise DashboardError("Há agentes trabalhando neste projeto. Aguarde ou cancele antes de alterar.", 409)
            if action == "document":
                value = self.server.store.edit(project_id, body.get("path"), body.get("content"), body.get("sha256"), body.get("reason", ""))
            elif action == "approve":
                value = self.server.store.approve(project_id, body.get("phase"), body.get("by"), body.get("note", ""))
            elif action == "revise":
                value = self.server.store.revise(project_id, body.get("phase"), body.get("reason"))
            elif action == "message":
                text, mode = body.get("text"), body.get("mode", "phase")
                if not isinstance(text, str) or not text.strip() or len(text) > 50000 or mode not in {"phase", "project", "question"}:
                    raise DashboardError("Informe uma mensagem válida e o modo de execução.")
                value = {"job": self.server.runner.start(root, text.strip(), mode=mode)}
            else:
                value = {"job": self.server.runner.cancel(root, job_id=body.get("job_id"))}
        return self._json(value)

    def _handle(self, operation):
        try:
            operation()
        except (BrokenPipeError, ConnectionResetError):
            return
        except DashboardError as exc:
            self._json({"error": str(exc)}, exc.status)
        except FileNotFoundError:
            self._json({"error": "Arquivo ou projeto não encontrado."}, 404)
        except (ValueError, RuntimeError) as exc:
            self._json({"error": str(exc) or "Operação não disponível."}, 409)
        except Exception:
            self._json({"error": "Não foi possível concluir a operação. Confira os arquivos do projeto e tente novamente."}, 500)

    def do_GET(self):
        self._handle(self._get)

    def do_HEAD(self):
        self._handle(self._get)

    def do_POST(self):
        self._handle(self._post)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Abra o dashboard local da Commercial Film Director")
    parser.add_argument("--port", type=int, default=8765, help="Porta local; 0 escolhe uma porta livre")
    parser.add_argument("--projects-dir", type=Path, default=DEFAULT_PROJECTS_DIR)
    parser.add_argument("--project-dir", type=Path, help="Registra e abre um projeto existente")
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--codex-binary", help="Caminho do Codex CLI a usar; padrão: codex no PATH")
    args = parser.parse_args(argv)
    if not 0 <= args.port <= 65535:
        parser.error("A porta deve estar entre 0 e 65535.")
    try:
        store = ProjectStore(args.projects_dir)
        initial = store.register(str(args.project_dir))["id"] if args.project_dir else None
        server = DashboardServer(("127.0.0.1", args.port), store, runner=default_runner(args.codex_binary), initial_project_id=initial)
    except (DashboardError, OSError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    url = server.origin + (f"/?project={initial}" if initial else "/")
    print(json.dumps({"url": url, "port": server.server_port, "projects_dir": str(store.projects_dir), "initial_project_id": initial}, ensure_ascii=False), flush=True)
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever(poll_interval=0.25)
    except KeyboardInterrupt:
        pass
    finally:
        if hasattr(server.runner, "shutdown"):
            server.runner.shutdown()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
