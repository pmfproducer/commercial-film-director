#!/usr/bin/env python3
"""Project-backed dashboard storage. The direction runtime remains authoritative."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import mimetypes
import os
import re
import threading
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

import project_runtime as runtime

PHASE_TITLES = [
    "Briefing e estratégia", "Rotas e direção criativa", "Roteiro",
    "Tratamento de direção", "Fotografia, arte e som", "Decupagem",
    "Assets e continuidade", "Storyboard e pré-visualização", "Plano de produção",
    "Pacotes de planos", "Montagem e pós-produção", "QA e versões",
]
DOC_PHASE = {name: phase["id"] for phase in runtime.PHASES for name in phase["docs"]}
TEXT_EXTENSIONS = {".md", ".txt", ".json", ".csv", ".html", ".css", ".js", ".svg", ".srt", ".vtt", ".xml", ".py"}
SECRET_NAMES = {"credentials", "credentials.json", "auth.json", "token", "token.json", "tokens.json", "secrets.json", "id_rsa", "id_ed25519", "config.toml"}
SECRET_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".crt", ".cer", ".keystore"}
MAX_DOCUMENT_BYTES = 2 * 1024 * 1024
_RUNTIME_OUTPUT_LOCK = threading.RLock()


class DashboardError(Exception):
    def __init__(self, message: str, status: int = 400):
        super().__init__(message)
        self.status = status


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def safe_relative(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise DashboardError("Caminho de arquivo inválido.", 403)
    relative = PurePosixPath(value)
    if relative.is_absolute() or any(part in {"", ".", ".."} or part.startswith(".") for part in value.split("/")):
        raise DashboardError("Caminho de arquivo não permitido.", 403)
    if any(part.casefold() in SECRET_NAMES for part in relative.parts) or relative.suffix.lower() in SECRET_SUFFIXES:
        raise DashboardError("Arquivo reservado não pode ser acessado pelo painel.", 403)
    return relative


def project_file(root: Path, value: str, *, must_exist: bool = True) -> Path:
    relative = safe_relative(value)
    root = root.resolve()
    candidate = root.joinpath(*relative.parts)
    cursor = root
    for part in relative.parts:
        cursor /= part
        if cursor.is_symlink():
            raise DashboardError("Links simbólicos não são servidos pelo painel.", 403)
    try:
        candidate.resolve().relative_to(root)
    except ValueError:
        raise DashboardError("Arquivo fora do projeto.", 403) from None
    if must_exist and not candidate.is_file():
        raise DashboardError("Arquivo não encontrado.", 404)
    return candidate


def read_state(root: Path) -> dict[str, Any]:
    path = project_file(root, runtime.STATE_NAME)
    if path.stat().st_size > 20 * 1024 * 1024:
        raise DashboardError("Estado do projeto excede o tamanho aceito.")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
        valid = (isinstance(state, dict) and isinstance(state.get("project_name"), str)
                 and isinstance(state.get("client"), str) and isinstance(state.get("phases"), dict)
                 and all(isinstance(state["phases"].get(p["id"]), dict) for p in runtime.PHASES)
                 and state.get("current_phase") in runtime.PHASE_BY_ID
                 and state.get("schema_version") == runtime.SCHEMA_VERSION)
    except (ValueError, UnicodeError):
        valid = False
    if not valid:
        raise DashboardError("A pasta não contém um projeto compatível. Confira 00_PROJECT_STATE.json.")
    return state


class ProjectStore:
    def __init__(self, projects_dir: Path):
        self.projects_dir = projects_dir.expanduser().resolve()
        self.projects_dir.mkdir(parents=True, exist_ok=True)
        self.private_dir = self.projects_dir / ".dashboard"
        if self.private_dir.is_symlink():
            raise DashboardError("O registro local não pode ser um link simbólico.", 403)
        self.private_dir.mkdir(exist_ok=True)
        self.index_path = self.private_dir / "index.json"
        if self.index_path.is_symlink():
            raise DashboardError("O registro local não pode ser um link simbólico.", 403)
        self._guard = threading.RLock()
        self._locks: dict[str, threading.RLock] = {}
        if not self.index_path.exists():
            atomic_json(self.index_path, {"schema_version": 1, "projects": []})
        self.discover()

    def _index(self) -> dict[str, Any]:
        try:
            value = json.loads(self.index_path.read_text(encoding="utf-8"))
            if not isinstance(value.get("projects"), list):
                raise ValueError()
            return value
        except (OSError, ValueError):
            raise DashboardError("Não foi possível ler o registro local de projetos.", 500) from None

    def lock(self, project_id: str) -> threading.RLock:
        with self._guard:
            return self._locks.setdefault(project_id, threading.RLock())

    def discover(self) -> None:
        for child in sorted(self.projects_dir.iterdir()):
            if child.is_dir() and not child.is_symlink() and not child.name.startswith(".") and (child / runtime.STATE_NAME).is_file():
                try:
                    self.register(str(child))
                except DashboardError:
                    continue

    def register(self, path: str) -> dict[str, Any]:
        if not isinstance(path, str) or not path.strip():
            raise DashboardError("Informe a pasta do projeto.")
        supplied = Path(path).expanduser()
        if supplied.is_symlink():
            raise DashboardError("Registre a pasta original, não um link simbólico.", 403)
        root = supplied.resolve()
        if not root.is_dir():
            raise DashboardError("Pasta do projeto não encontrada.", 404)
        state = read_state(root)
        if (root / ".dashboard").is_symlink() or (root / ".cfd-runtime.lock").is_symlink():
            raise DashboardError("O armazenamento interno do projeto contém um link simbólico.", 403)
        with self._guard, runtime.project_lock(self.private_dir):
            index = self._index()
            record = next((p for p in index["projects"] if p["path"] == str(root)), None)
            if record is None:
                record = {"id": uuid.uuid4().hex, "path": str(root), "registered_at": now()}
                index["projects"].append(record)
                atomic_json(self.index_path, index)
        return self.summary(record, state)

    def root(self, project_id: str) -> Path:
        if not re.fullmatch(r"[a-f0-9]{32}", project_id):
            raise DashboardError("Projeto não encontrado.", 404)
        record = next((p for p in self._index()["projects"] if p.get("id") == project_id), None)
        if record is None:
            raise DashboardError("Projeto não encontrado.", 404)
        path = Path(record["path"])
        if path.is_symlink() or not path.is_dir():
            raise DashboardError("A pasta registrada não está disponível.", 404)
        read_state(path)
        if (path / ".dashboard").is_symlink() or (path / ".cfd-runtime.lock").is_symlink():
            raise DashboardError("O armazenamento interno do projeto contém um link simbólico.", 403)
        return path.resolve()

    @staticmethod
    def summary(record: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
        return {"id": record["id"], "name": state["project_name"], "client": state["client"],
                "path": record["path"], "current_phase": state["current_phase"],
                "updated_at": state.get("updated_at"),
                "completed": sum(p.get("status") in runtime.COMPLETE_STATES for p in state["phases"].values()),
                "total": len(runtime.PHASES)}

    def projects(self) -> list[dict[str, Any]]:
        rows = []
        for record in self._index()["projects"]:
            try:
                root = self.root(record["id"])
                rows.append(self.summary(record, read_state(root)))
            except DashboardError:
                continue
        return sorted(rows, key=lambda r: r.get("updated_at") or "", reverse=True)

    def run(self, command: str, root: Path | None = None, **options: Any) -> str:
        """Invoke the runtime's real command handler; caller holds its project lock."""
        argv = [command]
        if root is not None:
            argv.extend(["--project-dir", str(root)])
        for key, value in options.items():
            argv.extend(["--" + key.replace("_", "-"), str(value)])
        args = runtime.build_parser().parse_args(argv)
        output = io.StringIO()
        with _RUNTIME_OUTPUT_LOCK, contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            try:
                code = args.func(args)
            except (OSError, ValueError, RuntimeError, KeyError) as exc:
                raise DashboardError(f"O runtime não concluiu a operação: {exc}", 409) from None
        if code:
            raise DashboardError(output.getvalue().strip() or "Operação recusada pelo runtime.", 409)
        return output.getvalue().strip()

    def create(self, name: str, client: str, brief: str) -> dict[str, Any]:
        if not isinstance(name, str) or not name.strip() or len(name) > 200:
            raise DashboardError("Informe um nome de projeto com até 200 caracteres.")
        if not isinstance(client, str) or len(client) > 200:
            raise DashboardError("O nome do cliente deve ter até 200 caracteres.")
        if not isinstance(brief, str) or not brief.strip() or len(brief.encode("utf-8")) > MAX_DOCUMENT_BYTES:
            raise DashboardError("Conte a ideia ou briefing do filme.")
        directory = f"FILME_{runtime.slugify(name)[:60]}_{uuid.uuid4().hex[:8]}"
        self.run("init", project=name.strip(), client=client.strip() or "A CONFIRMAR", output=self.projects_dir, directory_name=directory)
        root = self.projects_dir / directory
        with runtime.project_lock(root):
            source = root / "inputs" / "briefing.md"
            source.parent.mkdir(exist_ok=True)
            source.write_text(brief.strip() + "\n", encoding="utf-8")
            _, state = runtime.load_state(root)
            state["source_materials"].append({"id": "SRC-001", "path": "inputs/briefing.md", "type": "BRIEFING", "origin": "usuário", "received_at": now(), "sha256": digest(source.read_bytes())})
            manifest = root / "00_SOURCE_MANIFEST.md"
            text = manifest.read_text(encoding="utf-8")
            text = text.replace("| SRC-001 | <<PREENCHER>> | <<PREENCHER>> | usuário | " + state["created_at"][:10] + " | <<PREENCHER>> | <<PREENCHER>> | RECEBIDO |",
                                "| SRC-001 | inputs/briefing.md | briefing | usuário | " + state["created_at"][:10] + " | Ideia e restrições recebidas | Claims e direitos a verificar no projeto | RECEBIDO |")
            manifest.write_text(text, encoding="utf-8")
            runtime.save_state(root, state)
        return self.register(str(root))

    def files(self, root: Path) -> list[dict[str, Any]]:
        files = []
        for current, directories, names in os.walk(root, followlinks=False):
            directories[:] = sorted(d for d in directories if not d.startswith(".") and not (Path(current) / d).is_symlink() and d.casefold() not in SECRET_NAMES)
            for name in sorted(names):
                relative = (Path(current) / name).relative_to(root).as_posix()
                try:
                    path = project_file(root, relative)
                    files.append({"path": relative, "mime": mimetypes.guess_type(relative)[0] or "application/octet-stream", "size": path.stat().st_size})
                except (DashboardError, OSError):
                    continue
        return files

    def detail(self, project_id: str) -> dict[str, Any]:
        root = self.root(project_id)
        state = read_state(root)
        phases = []
        for definition, title in zip(runtime.PHASES, PHASE_TITLES):
            docs = []
            for name in definition["docs"]:
                path = project_file(root, name, must_exist=False)
                exists = path.is_file()
                docs.append({"path": name, "label": name, "exists": exists, "sha256": digest(path.read_bytes()) if exists else None})
            phases.append({"id": definition["id"], "title": title, "status": state["phases"][definition["id"]]["status"], "docs": docs})
        return {"id": project_id, "path": str(root), "state": state, "phases": phases,
                "files": self.files(root), "tasks": state.get("role_assignments", []), "chat": [], "job": None}

    @staticmethod
    def editable(relative: str, state: dict[str, Any]) -> bool:
        if relative not in DOC_PHASE and not (relative.startswith("inputs/") and Path(relative).suffix.lower() in {".md", ".txt"}):
            return False
        # Submissions and their immutable snapshots are never editable, even when a
        # malformed task points a submission at a canonical document.
        for cycles in state.get("workflow_registry", {}).values():
            for cycle in cycles:
                if not isinstance(cycle, dict):
                    continue
                for task in cycle.get("tasks", []):
                    if task.get("submission_path") == relative or task.get("deliverable_path") == relative:
                        return False
        return True

    def document(self, project_id: str, relative: str) -> dict[str, Any]:
        root = self.root(project_id)
        path = project_file(root, relative)
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            raise DashboardError("Este arquivo deve ser aberto como artefato.")
        if path.stat().st_size > MAX_DOCUMENT_BYTES:
            raise DashboardError("Documento grande demais para o editor. Abra o artefato.", 413)
        raw = path.read_bytes()
        try:
            content = raw.decode("utf-8")
        except UnicodeError:
            raise DashboardError("O editor aceita texto UTF-8.") from None
        return {"path": relative, "content": content, "sha256": digest(raw), "editable": self.editable(relative, read_state(root))}

    def edit(self, project_id: str, relative: str, content: str, sha256: str, reason: str) -> dict[str, Any]:
        root = self.root(project_id)
        if not isinstance(content, str) or len(content.encode("utf-8")) > MAX_DOCUMENT_BYTES:
            raise DashboardError("Documento inválido ou maior que 2 MB.", 413)
        if not isinstance(sha256, str) or not re.fullmatch(r"[a-f0-9]{64}", sha256):
            raise DashboardError("Reabra o documento antes de salvar: hash de origem obrigatório.", 409)
        if not isinstance(reason, str) or not reason.strip():
            raise DashboardError("Informe o motivo da edição.")
        with runtime.project_lock(root):
            state = read_state(root)
            path = project_file(root, relative)
            if not self.editable(relative, state):
                raise DashboardError("Este arquivo é somente leitura no painel.", 403)
            old = path.read_bytes()
            if digest(old) != sha256:
                raise DashboardError("O documento mudou desde que foi aberto. Reabra antes de salvar.", 409)
            if path.suffix.lower() == ".json":
                try:
                    json.loads(content)
                except ValueError:
                    raise DashboardError("O documento JSON contém erro de sintaxe.") from None
            new = content.encode("utf-8")
            if new == old:
                return {**self.document(project_id, relative), "unchanged": True, "revised_from": None}
            phase = DOC_PHASE.get(relative, "01_BRIEF_STRATEGY")
            start = runtime.PHASE_INDEX[phase]
            must_revise = any(state["phases"][p["id"]]["status"] in runtime.COMPLETE_STATES for p in runtime.PHASES[start:])
            history = root / ".dashboard" / "edits" / f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex}.json"
            atomic_json(history, {"at": now(), "path": relative, "reason": reason.strip(), "previous_sha256": sha256, "new_sha256": digest(new), "previous_content": old.decode("utf-8")})
            if must_revise:
                self.run("revise-from", root, phase=phase, reason=f"Edição pelo painel em {relative}: {reason.strip()}")
            temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
            temp.write_bytes(new)
            temp.replace(path)
            _, state = runtime.load_state(root)
            if relative.startswith("inputs/"):
                for source in state.get("source_materials", []):
                    if source.get("path") == relative:
                        source.update({"sha256": digest(new), "updated_at": now()})
            state.setdefault("revision_log", []).append({"at": now(), "type": "DASHBOARD_DOCUMENT_EDIT", "path": relative, "reason": reason.strip(), "previous_sha256": sha256, "sha256": digest(new)})
            runtime.save_state(root, state)
        return {**self.document(project_id, relative), "revised_from": phase if must_revise else None}

    def approve(self, project_id: str, phase: str, by: str, note: str) -> dict[str, Any]:
        if not isinstance(phase, str) or phase not in runtime.PHASE_BY_ID:
            raise DashboardError("Etapa inválida.")
        if not isinstance(by, str) or not by.strip():
            raise DashboardError("Informe quem está aprovando.")
        root = self.root(project_id)
        with runtime.project_lock(root):
            message = self.run("approve", root, phase=phase, by=by.strip(), note=note or "Aprovação explícita no painel local")
        return {"message": message, "state": read_state(root)}

    def revise(self, project_id: str, phase: str, reason: str) -> dict[str, Any]:
        if not isinstance(phase, str) or phase not in runtime.PHASE_BY_ID or not isinstance(reason, str) or not reason.strip():
            raise DashboardError("Informe a etapa e o motivo da revisão.")
        root = self.root(project_id)
        with runtime.project_lock(root):
            message = self.run("revise-from", root, phase=phase, reason=reason.strip())
        return {"message": message, "state": read_state(root)}

    def export(self, project_id: str, destination: Any) -> None:
        root = self.root(project_id)
        with runtime.project_lock(root), zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
            for entry in self.files(root):
                path = project_file(root, entry["path"])
                archive.write(path, f"{root.name}/{entry['path']}")
