#!/usr/bin/env python3
"""Runtime file-backed para projetos da skill commercial-film-director.

O script não cria conteúdo criativo. Ele inicializa o pacote, materializa os
documentos da fase, preserva dependências e valida se o agente realmente preencheu
os arquivos antes de avançar.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any
from contextlib import contextmanager

from prepare_repertoire import build_packet


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "project-template"
STATE_NAME = "00_PROJECT_STATE.json"
LOCK_NAME = "00_DIRECTION_LOCK.md"
ROOM_NAME = "00_SALA_DE_DIRECAO.md"
PLACEHOLDER = "<<PREENCHER>>"
PLACEHOLDER_PATTERN = re.compile(r"<<PREENCHER[^>]*>>")
COMPLETE_STATES = {"COMPLETE_DRAFT", "APPROVED"}
SCHEMA_VERSION = 2
RUNTIME_VERSION = "commercial-film-director-v6-repertoire"
DIRECTOR_VERDICTS = {
    "ACCEPT",
    "REVISE",
    "MORE_RESEARCH",
    "CROSS_DEPARTMENT_REVIEW",
    "REJECT",
}
ACTOR_TYPES = {"TEMP_SUBAGENT", "ROLE_SIMULATION"}

PHASES: list[dict[str, Any]] = [
    {
        "id": "01_BRIEF_STRATEGY",
        "docs": ["01_BRIEF_ESTRATEGICO.md", "00_SOURCE_MANIFEST.md"],
    },
    {
        "id": "02_CREATIVE_DIRECTION",
        "docs": ["02_ROTAS_E_DIRECAO.md", LOCK_NAME],
    },
    {
        "id": "03_SCRIPT",
        "docs": ["03_ROTEIRO_LITERARIO.md", "03_ROTEIRO_AV.md"],
    },
    {
        "id": "04_DIRECTOR_TREATMENT",
        "docs": ["04_TRATAMENTO_DIRECAO.md", "04_MAPA_CENA_PERFORMANCE.md"],
    },
    {
        "id": "05_VISUAL_SOUND_SYSTEM",
        "docs": [
            "05_DIRECAO_FOTOGRAFIA.md",
            "05_DIRECAO_ARTE.md",
            "05_ARQUITETURA_MONTAGEM_SOM.md",
            "05_BIBLIA_VISUAL_SONORA.md",
        ],
    },
    {
        "id": "06_DECOUPAGE",
        "docs": ["06_ROTEIRO_TECNICO.md", "06_SHOT_LIST.md"],
    },
    {
        "id": "07_ASSETS_CONTINUITY",
        "docs": ["07_ASSET_BIBLE.md", "07_ASSET_MANIFEST.json"],
    },
    {"id": "08_STORYBOARD_PREVIS", "docs": ["08_STORYBOARD_PREVIS.md"]},
    {
        "id": "09_AI_EXECUTION_PLAN",
        "docs": ["09_PLANO_PRODUCAO_HIBRIDA.md", "09_PLANO_GERACAO_IA.md"],
    },
    {"id": "10_SHOT_PACKETS", "docs": ["10_SHOT_PACKETS_PROMPTS.md"]},
    {"id": "11_POST_DELIVERY", "docs": ["11_MONTAGEM_SOM_POS.md"]},
    {"id": "12_QA_VERSIONS", "docs": ["12_QA_MASTER_VERSOES.md"]},
]
PHASE_BY_ID = {phase["id"]: phase for phase in PHASES}
PHASE_INDEX = {phase["id"]: index for index, phase in enumerate(PHASES)}
PHASE_GATE = {
    "01_BRIEF_STRATEGY": "BRIEF",
    "02_CREATIVE_DIRECTION": "DIRECTION",
    "03_SCRIPT": "SCRIPT",
    "05_VISUAL_SOUND_SYSTEM": "VISUAL_SYSTEM",
    "08_STORYBOARD_PREVIS": "STORYBOARD",
}
PHASE_INTERNAL_LOCK = {
    "02_CREATIVE_DIRECTION": "DIRECTION_LOCK",
    "03_SCRIPT": "STORY_LOCK",
    "04_DIRECTOR_TREATMENT": "DIRECTOR_TREATMENT_LOCK",
    "05_VISUAL_SOUND_SYSTEM": "VISUAL_SYSTEM_LOCK",
    "08_STORYBOARD_PREVIS": "TECHNICAL_PACK_LOCK",
    "09_AI_EXECUTION_PLAN": "PRODUCTION_PLAN_LOCK",
    "12_QA_VERSIONS": "QA_DOCUMENT_LOCK",
}

PHASE_REQUIRED_ROLES: dict[str, tuple[str, ...]] = {
    "01_BRIEF_STRATEGY": ("RESEARCHER",),
    "02_CREATIVE_DIRECTION": ("CREATIVE_DIRECTOR", "SCREENWRITER", "CRITIC"),
    "03_SCRIPT": ("SCREENWRITER", "CRITIC"),
    "04_DIRECTOR_TREATMENT": ("PERFORMANCE_DIRECTOR", "CRITIC"),
    "05_VISUAL_SOUND_SYSTEM": (
        "DP",
        "PRODUCTION_DESIGNER",
        "EDITOR",
        "SOUND_DESIGNER",
        "CRITIC",
    ),
    "06_DECOUPAGE": ("DP", "EDITOR", "PRODUCER_AD", "CRITIC"),
    "07_ASSETS_CONTINUITY": ("PRODUCTION_DESIGNER", "CONTINUITY_SUPERVISOR"),
    "08_STORYBOARD_PREVIS": ("STORYBOARD_ARTIST", "DP", "EDITOR", "CRITIC"),
    "09_AI_EXECUTION_PLAN": ("PRODUCER_AD", "VFX_AI_SUPERVISOR"),
    "10_SHOT_PACKETS": ("VFX_AI_SUPERVISOR", "CRITIC"),
    "11_POST_DELIVERY": ("EDITOR", "SOUND_DESIGNER", "POST_QA"),
    "12_QA_VERSIONS": ("POST_QA", "CRITIC"),
}
PHASE_OPTIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "02_CREATIVE_DIRECTION": ("RESEARCHER",),
    "03_SCRIPT": ("RESEARCHER", "PERFORMANCE_DIRECTOR"),
    "04_DIRECTOR_TREATMENT": ("PRODUCTION_DESIGNER", "DP"),
    "05_VISUAL_SOUND_SYSTEM": ("PERFORMANCE_DIRECTOR", "CONTINUITY_SUPERVISOR"),
    "06_DECOUPAGE": ("PERFORMANCE_DIRECTOR", "PRODUCTION_DESIGNER", "SOUND_DESIGNER", "CONTINUITY_SUPERVISOR"),
    "07_ASSETS_CONTINUITY": ("DP", "VFX_AI_SUPERVISOR"),
    "08_STORYBOARD_PREVIS": ("PERFORMANCE_DIRECTOR", "PRODUCTION_DESIGNER", "SOUND_DESIGNER", "CONTINUITY_SUPERVISOR"),
    "09_AI_EXECUTION_PLAN": ("DP", "PRODUCTION_DESIGNER", "EDITOR", "SOUND_DESIGNER", "CONTINUITY_SUPERVISOR"),
    "10_SHOT_PACKETS": ("DP", "PRODUCTION_DESIGNER", "EDITOR", "SOUND_DESIGNER", "CONTINUITY_SUPERVISOR"),
    "11_POST_DELIVERY": ("VFX_AI_SUPERVISOR", "CONTINUITY_SUPERVISOR"),
    "12_QA_VERSIONS": ("PRODUCER_AD", "CONTINUITY_SUPERVISOR", "VFX_AI_SUPERVISOR"),
}

PHASE_REQUIRED_MARKERS: dict[str, dict[str, list[str]]] = {
    "03_SCRIPT": {
        "03_ROTEIRO_LITERARIO.md": [
            "INT./EXT.",
            "DIA/NOITE",
            "SCENE IDs",
            "Parecer do diretor",
        ],
    },
    "04_DIRECTOR_TREATMENT": {
        "04_MAPA_CENA_PERFORMANCE.md": [
            "Registro espacial canônico",
            "POINT ID",
            "Performance para rota IA/híbrida",
        ],
    },
    "05_VISUAL_SOUND_SYSTEM": {
        "05_DIRECAO_FOTOGRAFIA.md": [
            "DP-SYS-001",
            "LENS-SET-001",
            "Viabilidade de DOF/foco",
            "LIGHT-STATE ID",
            "TIME-STATE ID",
        ],
        "05_DIRECAO_ARTE.md": ["PRD-001", "PRP ID", "WDR ID", "POINT ID"],
        "05_ARQUITETURA_MONTAGEM_SOM.md": [
            "COVERAGE ID",
            "AUD EVENT ID",
            "Regra causal",
        ],
        "05_BIBLIA_VISUAL_SONORA.md": [
            "Registro canônico compartilhado",
            "ENTITY/POINT ID",
            "Reconciliação fechada",
        ],
    },
    "06_DECOUPAGE": {
        "06_ROTEIRO_TECNICO.md": [
            "Duração física",
            "Viabilidade de foco/DOF",
            "POINT IDs canônicos",
            "LENS-SET",
            "TIME-STATE",
            "LIGHT-STATE",
        ],
        "06_SHOT_LIST.md": [
            "Shot list operacional",
            "PLAN ID",
            "Produção/AD",
            "Parecer do diretor",
        ],
    },
}

NONCANONICAL_ID_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bTIME-\d{3}\b"), "usar TIME-STATE-NNN"),
    (re.compile(r"\bLIGHT-\d{3}\b"), "usar LIGHT-STATE-NNN"),
    (re.compile(r"\bLENS/\d+(?:mm)?\b", re.IGNORECASE), "usar LENS-SET-NNN/focal"),
    (re.compile(r"\bPROD-\d{3}\b"), "usar PRD-NNN"),
    (re.compile(r"\bPROP-\d{3}\b"), "usar PRP-NNN"),
    (re.compile(r"\bWARD-\d{3}\b"), "usar WDR-NNN"),
]


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "_", ascii_value).strip("_").upper()
    return slug or "FILME"


def state_path(project_dir: Path) -> Path:
    return project_dir.expanduser().resolve() / STATE_NAME


def load_state(project_dir: Path) -> tuple[Path, dict[str, Any]]:
    root = project_dir.expanduser().resolve()
    path = root / STATE_NAME
    if not path.is_file():
        raise FileNotFoundError(f"Estado não encontrado: {path}")
    return root, json.loads(path.read_text(encoding="utf-8"))


def save_state(root: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = now_iso()
    destination = root / STATE_NAME
    temporary = root / f".{STATE_NAME}.tmp"
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(destination)


@contextmanager
def project_lock(project_dir: Path):
    """Serialize CLI transactions so simultaneous specialists cannot lose updates."""
    root = project_dir.expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Projeto não encontrado: {root}")
    with (root / '.cfd-runtime.lock').open('a+b') as handle:
        if os.name == 'nt':
            import msvcrt
            if handle.seek(0, os.SEEK_END) == 0:
                handle.write(b'\0')
                handle.flush()
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_LOCK, 1)
            try:
                yield
            finally:
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def template_text(filename: str, state: dict[str, Any]) -> str:
    template = TEMPLATE_ROOT / filename
    if not template.is_file():
        raise FileNotFoundError(f"Template ausente: {template}")
    replacements = {
        "{{PROJECT_NAME}}": state["project_name"],
        "{{CLIENT}}": state["client"],
        "{{PROJECT_ID}}": state["project_id"],
        "{{DATE}}": state["created_at"][:10],
    }
    text = template.read_text(encoding="utf-8")
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text


def materialize_doc(root: Path, filename: str, state: dict[str, Any]) -> bool:
    destination = root / filename
    if destination.exists():
        return False
    destination.write_text(template_text(filename, state), encoding="utf-8")
    return True


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def runtime_provenance() -> dict[str, str]:
    runtime_path = Path(__file__).resolve()
    return {
        "runtime_path": str(runtime_path),
        "runtime_sha256": file_sha256(runtime_path),
        "runtime_version": RUNTIME_VERSION,
    }


def append_room(root: Path, heading: str, lines: list[str]) -> None:
    room = root / ROOM_NAME
    if not room.is_file():
        raise FileNotFoundError(f"Sala de direção ausente: {room}")
    with room.open("a", encoding="utf-8") as stream:
        stream.write(f"\n### {heading}\n\n")
        for line in lines:
            stream.write(f"- {line}\n")


def next_registry_id(prefix: str, records: list[dict[str, Any]]) -> str:
    return f"{prefix}-{len(records) + 1:03d}"


def find_cycle(state: dict[str, Any], cycle_id: str) -> dict[str, Any]:
    for cycles in state.get("workflow_registry", {}).values():
        for cycle in cycles:
            if cycle.get("cycle_id") == cycle_id:
                return cycle
    raise ValueError(f"Ciclo não encontrado: {cycle_id}")


def find_task(state: dict[str, Any], task_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    for cycles in state.get("workflow_registry", {}).values():
        for cycle in cycles:
            for task in cycle.get("tasks", []):
                if task.get("task_id") == task_id:
                    return cycle, task
    raise ValueError(f"Tarefa não encontrada: {task_id}")


def changed_cycle_inputs(root: Path, cycle: dict[str, Any]) -> list[str]:
    """Return dispatched inputs whose file disappeared or hash changed."""
    changed: list[str] = []
    for item in cycle.get("input_artifacts", []):
        path = root / item["path"]
        if not path.is_file() or file_sha256(path) != item.get("sha256"):
            changed.append(item["path"])
    return changed


def invalidate_stale_cycle(
    root: Path, state: dict[str, Any], cycle: dict[str, Any], changed: list[str]
) -> None:
    """Close an in-flight cycle invalidated by upstream change control."""
    cycle["status"] = "REVISION_REQUIRED"
    cycle["invalidation"] = {
        "reason": "STALE_INPUTS",
        "changed_inputs": changed,
        "invalidated_at": now_iso(),
    }
    for assignment in state.get("role_assignments", []):
        if assignment.get("cycle_id") == cycle.get("cycle_id"):
            assignment["status"] = "REVISION_REQUIRED"
    append_room(root, f"{cycle['cycle_id']} — ENTRADAS OBSOLETAS", [
        "Motivo: mudança formal em fase a montante",
        "Entradas alteradas: " + ", ".join(f"`{item}`" for item in changed),
        "Estado: `REVISION_REQUIRED`; abrir nova rodada com hashes atuais",
    ])


def accepted_cycle(state: dict[str, Any], phase_id: str) -> dict[str, Any] | None:
    cycles = state.get("workflow_registry", {}).get(phase_id, [])
    for cycle in reversed(cycles):
        if cycle.get("status") == "ACCEPTED_BY_DIRECTOR":
            return cycle
    return None


def collaboration_errors(root: Path, state: dict[str, Any], phase_id: str) -> list[str]:
    if phase_id in state.get("legacy_acceptance_exemptions", []):
        return []
    cycle = accepted_cycle(state, phase_id)
    if not cycle:
        return [f"nenhuma rodada aceita pelo diretor em {phase_id}"]
    errors: list[str] = []
    for item in cycle.get("input_artifacts", []):
        path = root / item["path"]
        if not path.is_file():
            errors.append(f"entrada da rodada ausente: {item['path']}")
        elif file_sha256(path) != item.get("sha256"):
            errors.append(f"entrada da rodada mudou após dispatch: {item['path']}")
    submitted_roles = {
        task.get("role")
        for task in cycle.get("tasks", [])
        if task.get("status") == "SUBMITTED"
    }
    for role in PHASE_REQUIRED_ROLES.get(phase_id, ()):
        if role not in submitted_roles:
            errors.append(f"papel obrigatório sem entrega aceita em {phase_id}: {role}")
    for task in cycle.get("tasks", []):
        if task.get("status") != "SUBMITTED":
            errors.append(f"tarefa não submetida em {phase_id}: {task.get('task_id')}")
            continue
        path = root / task["submission_path"]
        if not path.is_file():
            errors.append(f"parecer de especialista ausente: {task['submission_path']}")
        elif file_sha256(path) != task.get("submission_sha256"):
            errors.append(f"parecer mudou após revisão do diretor: {task['submission_path']}")
        expected_provenance = {
            key: task.get(key)
            for key in ("runtime_path", "runtime_sha256", "runtime_version")
        }
        reported_provenance = task.get("runtime_provenance_reported", {})
        if expected_provenance != reported_provenance:
            errors.append(
                f"runtime provenance ausente ou divergente em {task.get('task_id')}"
            )
    review = cycle.get("director_review") or {}
    if review.get("verdict") != "ACCEPT":
        errors.append(f"rodada não aceita pelo diretor em {phase_id}")
    reviewer = review.get("actor_id")
    if reviewer and reviewer in {task.get("actor_id") for task in cycle.get("tasks", [])}:
        errors.append(f"diretor não pode aprovar o próprio parecer em {phase_id}")
    return errors


def previous_phase(phase_id: str) -> str | None:
    index = PHASE_INDEX[phase_id]
    return PHASES[index - 1]["id"] if index > 0 else None


def next_phase(phase_id: str) -> str | None:
    index = PHASE_INDEX[phase_id]
    return PHASES[index + 1]["id"] if index + 1 < len(PHASES) else None


def artifact_integrity_errors(
    root: Path, state: dict[str, Any], phase_id: str
) -> list[str]:
    errors: list[str] = []
    for filename in PHASE_BY_ID[phase_id]["docs"]:
        path = root / filename
        registered = state.get("artifact_registry", {}).get(filename, {})
        expected = registered.get("sha256")
        if not expected:
            errors.append(f"hash canônico ausente: {filename}")
        elif not path.is_file():
            errors.append(f"arquivo ausente: {filename}")
        elif file_sha256(path) != expected:
            errors.append(f"arquivo mudou após conclusão: {filename}")
    return errors


def ensure_dependency(root: Path, state: dict[str, Any], phase_id: str) -> None:
    for dependency in PHASES[: PHASE_INDEX[phase_id]]:
        dependency_id = dependency["id"]
        current = state["phases"][dependency_id]["status"]
        if current not in COMPLETE_STATES:
            raise RuntimeError(
                f"Dependência bloqueada: {dependency_id} está {current}; "
                f"complete-a antes de {phase_id}."
            )
        integrity_errors = artifact_integrity_errors(root, state, dependency_id)
        if integrity_errors:
            raise RuntimeError(
                f"Dependência adulterada: {dependency_id}; execute revise-from. "
                + "; ".join(integrity_errors)
            )


def ensure_phase(root: Path, state: dict[str, Any], phase_id: str) -> list[str]:
    if phase_id not in PHASE_BY_ID:
        raise ValueError(f"Fase inválida: {phase_id}")
    ensure_dependency(root, state, phase_id)
    phase = state["phases"][phase_id]
    if phase["status"] in COMPLETE_STATES:
        integrity_errors = artifact_integrity_errors(root, state, phase_id)
        if integrity_errors:
            raise RuntimeError(
                f"Fase concluída adulterada: {phase_id}; execute revise-from. "
                + "; ".join(integrity_errors)
            )
        return []
    created: list[str] = []
    for filename in PHASE_BY_ID[phase_id]["docs"]:
        if materialize_doc(root, filename, state):
            created.append(filename)
        state["artifact_registry"].setdefault(filename, {})
        state["artifact_registry"][filename].update({
            "phase": phase_id,
            "status": "IN_PROGRESS",
        })
    if phase["status"] == "PENDING":
        phase["status"] = "IN_PROGRESS"
        phase["started_at"] = now_iso()
    state["current_phase"] = phase_id
    state["next_action"] = f"Preencher e validar {phase_id}"
    save_state(root, state)
    return created


def validate_document(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"arquivo ausente: {path.name}"]
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_PATTERN.search(text):
        errors.append(f"marcador obrigatório ainda presente: {path.name}")
    if len(text.strip()) < 240:
        errors.append(f"conteúdo insuficiente: {path.name}")
    for pattern, instruction in NONCANONICAL_ID_PATTERNS:
        match = pattern.search(text)
        if match:
            errors.append(
                f"ID não canônico em {path.name}: {match.group(0)}; {instruction}"
            )
    if path.suffix == ".json":
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            errors.append(f"JSON inválido em {path.name}: {exc}")
    return errors


def markdown_plan_table(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    """Read the first markdown table whose header contains PLAN ID."""
    if not path.is_file():
        return [], []
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if not line.lstrip().startswith("|") or "PLAN ID" not in line.upper():
            continue
        headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows: list[dict[str, str]] = []
        for candidate in lines[index + 2:]:
            if not candidate.lstrip().startswith("|"):
                break
            cells = [cell.strip() for cell in candidate.strip().strip("|").split("|")]
            if len(cells) != len(headers):
                continue
            row = dict(zip(headers, cells))
            if re.search(r"\bPL-\d+\b", row.get("PLAN ID", "")):
                rows.append(row)
        return headers, rows
    return [], []


def parse_seconds(value: str) -> float | None:
    match = re.search(r"(\d+(?:[.,]\d+)?)\s*s\b", value, flags=re.IGNORECASE)
    return float(match.group(1).replace(",", ".")) if match else None


def semantic_lint_phase06(root: Path) -> list[str]:
    """Cross-check plan identity, timing, handles, and movement-ID uniqueness."""
    technical = root / "06_ROTEIRO_TECNICO.md"
    shot_list = root / "06_SHOT_LIST.md"
    tech_headers, tech_rows = markdown_plan_table(technical)
    shot_headers, shot_rows = markdown_plan_table(shot_list)
    errors: list[str] = []
    if not tech_rows:
        return ["lint semântico: roteiro técnico sem linhas PLAN ID"]
    if not shot_rows:
        return ["lint semântico: shot list sem linhas PLAN ID"]
    required_tech = {"PLAN ID", "Duração física", "Câmera/movimento"}
    required_shot = {"PLAN ID", "Duração útil", "Handles"}
    missing_tech = required_tech - set(tech_headers)
    missing_shot = required_shot - set(shot_headers)
    if missing_tech:
        errors.append("lint semântico: colunas ausentes no roteiro técnico: " + ", ".join(sorted(missing_tech)))
    if missing_shot:
        errors.append("lint semântico: colunas ausentes na shot list: " + ", ".join(sorted(missing_shot)))
    if errors:
        return errors

    def plan_id(row: dict[str, str]) -> str:
        match = re.search(r"\bPL-\d+\b", row["PLAN ID"])
        return match.group(0) if match else ""

    tech_ids = [plan_id(row) for row in tech_rows]
    shot_ids = [plan_id(row) for row in shot_rows]
    for label, ids in (("roteiro técnico", tech_ids), ("shot list", shot_ids)):
        duplicates = sorted({item for item in ids if ids.count(item) > 1})
        if duplicates:
            errors.append(f"lint semântico: PLAN ID duplicado em {label}: {', '.join(duplicates)}")
    if set(tech_ids) != set(shot_ids):
        errors.append(
            "lint semântico: PLAN IDs divergem entre roteiro técnico e shot list; "
            f"somente técnico={sorted(set(tech_ids) - set(shot_ids))}; "
            f"somente shot list={sorted(set(shot_ids) - set(tech_ids))}"
        )

    tech_duration: dict[str, float] = {}
    for row in tech_rows:
        identifier = plan_id(row)
        duration = parse_seconds(row["Duração física"])
        if duration is None:
            errors.append(f"lint semântico: duração física inválida em {identifier}")
        else:
            tech_duration[identifier] = duration
    shot_duration: dict[str, float] = {}
    for row in shot_rows:
        identifier = plan_id(row)
        duration = parse_seconds(row["Duração útil"])
        if duration is None:
            errors.append(f"lint semântico: duração útil inválida na shot list em {identifier}")
        else:
            shot_duration[identifier] = duration
        handles = row["Handles"]
        if not re.search(r"\d+\s*(?:f|frames?|s)\b", handles, flags=re.IGNORECASE):
            errors.append(f"lint semântico: handles não quantificados em {identifier}")
    for identifier in sorted(set(tech_duration) & set(shot_duration)):
        if abs(tech_duration[identifier] - shot_duration[identifier]) > 0.01:
            errors.append(
                f"lint semântico: duração diverge em {identifier}: "
                f"técnico={tech_duration[identifier]:g}s, shot list={shot_duration[identifier]:g}s"
            )

    target_match = re.search(
        r"Duração alvo \(s\):\s*`?\s*(\d+(?:[.,]\d+)?)",
        technical.read_text(encoding="utf-8"), flags=re.IGNORECASE,
    )
    if not target_match:
        errors.append("lint semântico: duração alvo numérica ausente no roteiro técnico")
    elif tech_duration:
        target = float(target_match.group(1).replace(",", "."))
        total = sum(tech_duration.values())
        if abs(total - target) > 0.01:
            errors.append(f"lint semântico: soma dos planos {total:g}s difere da duração alvo {target:g}s")

    movements: dict[str, list[tuple[str, str]]] = {}
    for row in tech_rows:
        identifier = plan_id(row)
        camera = row["Câmera/movimento"]
        for movement in sorted(set(re.findall(r"\bCAM-MOV-\d+\b", camera))):
            movements.setdefault(movement, []).append((identifier, camera))
    for movement, uses in movements.items():
        if len(uses) > 1 and not all("SHARED_CONTINUOUS" in camera for _, camera in uses):
            errors.append(
                f"lint semântico: {movement} reutilizado em "
                + ", ".join(identifier for identifier, _ in uses)
                + "; marque SHARED_CONTINUOUS em todas as linhas apenas se for o mesmo movimento contínuo"
            )
    return errors


def validate_phase(root: Path, state: dict[str, Any], phase_id: str) -> list[str]:
    errors: list[str] = []
    for filename in PHASE_BY_ID[phase_id]["docs"]:
        errors.extend(validate_document(root / filename))
        text = (root / filename).read_text(encoding="utf-8") if (root / filename).is_file() else ""
        for marker in PHASE_REQUIRED_MARKERS.get(phase_id, {}).get(filename, []):
            if marker not in text:
                errors.append(f"contrato semântico ausente em {filename}: {marker}")
    if PHASE_INDEX[phase_id] >= PHASE_INDEX["03_SCRIPT"]:
        lock = root / LOCK_NAME
        if not lock.is_file() or PLACEHOLDER_PATTERN.search(lock.read_text(encoding="utf-8")):
            errors.append("00_DIRECTION_LOCK.md não está travado")
    if phase_id == "06_DECOUPAGE":
        errors.extend(semantic_lint_phase06(root))
    errors.extend(collaboration_errors(root, state, phase_id))
    return errors


def command_init(args: argparse.Namespace) -> int:
    parent = args.output.expanduser().resolve()
    target_name = args.directory_name or f"FILME_{slugify(args.project)}"
    target = parent / target_name
    if target.exists():
        print(f"ERRO: projeto já existe: {target}", file=sys.stderr)
        return 2
    target.mkdir(parents=True)
    for directory in (
        "collaboration/cycles",
        "collaboration/handoffs",
        "collaboration/reviews",
        "departments/research",
        "departments/script",
        "departments/performance",
        "departments/cinematography",
        "departments/production-design",
        "departments/edit-sound",
        "departments/production",
        "departments/storyboard",
        "departments/vfx-ai",
        "departments/post-qa",
        "research",
        "references",
        "storyboard",
        "generations",
        "outputs",
        "audio",
        "assets/characters",
        "assets/products",
        "assets/props",
        "assets/environments",
        "assets/wardrobe",
        "assets/look",
    ):
        (target / directory).mkdir(parents=True, exist_ok=True)

    created_at = now_iso()
    project_id = f"{slugify(args.client)}-{slugify(args.project)}"
    state: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "runtime": RUNTIME_VERSION,
        "mode": "PROJECT",
        "execution_mode": "MULTI_AGENT",
        "script_mode": "LITERARY_THEN_AV",
        "project_id": project_id,
        "project_name": args.project,
        "client": args.client,
        "project_root": str(target),
        "created_at": created_at,
        "updated_at": created_at,
        "revision": 1,
        "approval_policy": args.approval_policy,
        "current_phase": PHASES[0]["id"],
        "direction_version": 0,
        "next_action": "Preencher e validar 01_BRIEF_STRATEGY",
        "phases": {
            phase["id"]: {
                "status": "PENDING",
                "documents": phase["docs"],
                "started_at": None,
                "completed_at": None,
                "approved_at": None,
                "approved_by": None,
            }
            for phase in PHASES
        },
        "decisions": [],
        "source_materials": [],
        "open_questions": [],
        "artifact_registry": {},
        "id_registry": {"active": [], "retired": []},
        "blocked_transitions": [],
        "revision_log": [],
        "workflow_registry": {phase["id"]: [] for phase in PHASES},
        "handoff_registry": {},
        "director_reviews": [],
        "role_assignments": [],
        "internal_locks": {lock: "OPEN" for lock in PHASE_INTERNAL_LOCK.values()},
        "human_gates": {
            "BRIEF": "OPEN",
            "DIRECTION": "OPEN",
            "SCRIPT": "OPEN",
            "VISUAL_SYSTEM": "OPEN",
            "STORYBOARD": "OPEN",
            "GENERATION_SPEND": "BLOCKED",
            "CLIENT_DELIVERY": "BLOCKED",
        },
    }
    save_state(target, state)
    materialize_doc(target, "00_INDEX_PROJETO.md", state)
    materialize_doc(target, "00_SOURCE_MANIFEST.md", state)
    materialize_doc(target, LOCK_NAME, state)
    materialize_doc(target, ROOM_NAME, state)
    ensure_phase(target, state, PHASES[0]["id"])
    print(target)
    return 0


def command_status(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    print(json.dumps({
        "project_root": str(root),
        "project_name": state["project_name"],
        "client": state["client"],
        "current_phase": state["current_phase"],
        "current_status": state["phases"][state["current_phase"]]["status"],
        "direction_version": state["direction_version"],
        "revision": state["revision"],
        "execution_mode": state.get("execution_mode", "LEGACY_LINEAR"),
        "script_mode": state.get("script_mode", "LEGACY_AV_ONLY"),
        "next_action": state["next_action"],
        "open_questions": state["open_questions"],
        "human_gates": state["human_gates"],
        "internal_locks": state.get("internal_locks", {}),
        "director_room": {
            phase: [
                {
                    "cycle_id": cycle.get("cycle_id"),
                    "status": cycle.get("status"),
                    "verdict": (cycle.get("director_review") or {}).get("verdict"),
                }
                for cycle in cycles
            ]
            for phase, cycles in state.get("workflow_registry", {}).items()
            if cycles
        },
    }, ensure_ascii=False, indent=2))
    return 0


def command_ensure(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    try:
        created = ensure_phase(root, state, args.phase)
    except RuntimeError as exc:
        state["blocked_transitions"].append({
            "at": now_iso(),
            "requested_phase": args.phase,
            "reason": str(exc),
        })
        save_state(root, state)
        raise
    print(json.dumps({"phase": args.phase, "created": created}, ensure_ascii=False))
    return 0


def command_open_cycle(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    ensure_phase(root, state, args.phase)
    cycles = state.setdefault("workflow_registry", {}).setdefault(args.phase, [])
    if cycles and cycles[-1].get("status") not in {
        "REVISION_REQUIRED", "REJECTED", "ACCEPTED_BY_DIRECTOR",
    }:
        previous_cycle = cycles[-1]
        changed = changed_cycle_inputs(root, previous_cycle)
        if changed:
            invalidate_stale_cycle(root, state, previous_cycle, changed)
        else:
            raise RuntimeError(
                f"Ciclo anterior ainda aberto em {args.phase}: "
                f"{previous_cycle['cycle_id']}"
            )
    cycle_id = f"CYCLE-{args.phase}-{len(cycles) + 1:03d}"
    input_artifacts: list[dict[str, str]] = []
    prior = previous_phase(args.phase)
    candidates: list[str] = []
    if prior:
        candidates.extend(PHASE_BY_ID[prior]["docs"])
    if PHASE_INDEX[args.phase] >= PHASE_INDEX["03_SCRIPT"]:
        candidates.append(LOCK_NAME)
    for filename in dict.fromkeys(candidates):
        path = root / filename
        if path.is_file():
            input_artifacts.append({"path": filename, "sha256": file_sha256(path)})
    cycle = {
        "cycle_id": cycle_id,
        "phase": args.phase,
        "question": args.question,
        "must_preserve": args.must_preserve,
        "parent_cycle_id": args.parent_cycle,
        "status": "OPEN",
        "opened_at": now_iso(),
        "input_artifacts": input_artifacts,
        "tasks": [],
        "director_review": None,
    }
    cycles.append(cycle)
    append_room(root, f"{cycle_id} — ABERTA", [
        f"Fase: `{args.phase}`",
        f"Pergunta do diretor: {args.question}",
        f"Preservar: {args.must_preserve}",
        f"Ciclo anterior: {args.parent_cycle or 'nenhum'}",
    ])
    save_state(root, state)
    print(json.dumps(cycle, ensure_ascii=False, indent=2))
    return 0


def command_assign_task(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    cycle = find_cycle(state, args.cycle)
    if cycle["status"] not in {"OPEN", "DISPATCHED", "SUBMITTED"}:
        raise RuntimeError(f"Ciclo não aceita assignment: {cycle['status']}")
    if args.actor_type not in ACTOR_TYPES:
        raise ValueError(f"actor-type inválido: {args.actor_type}")
    if args.role == "DIRECTOR":
        raise ValueError("DIRECTOR revisa; não recebe tarefa de especialista")
    allowed_roles = set(PHASE_REQUIRED_ROLES.get(cycle["phase"], ())) | set(
        PHASE_OPTIONAL_ROLES.get(cycle["phase"], ())
    )
    if args.role not in allowed_roles:
        raise ValueError(
            f"Papel {args.role} não pertence à sala de {cycle['phase']}; "
            "respeite a ordem causal dos departamentos"
        )
    if any(task.get("role") == args.role for task in cycle["tasks"]):
        raise RuntimeError(f"Papel já atribuído neste ciclo: {args.role}")
    if args.actor_type == "TEMP_SUBAGENT" and any(
        task.get("actor_type") == "TEMP_SUBAGENT"
        and task.get("actor_id") == args.actor_id
        for task in cycle["tasks"]
    ):
        raise RuntimeError("Cada especialista real deve ter actor_id próprio no ciclo")
    all_tasks = [
        task
        for cycles in state.get("workflow_registry", {}).values()
        for item in cycles
        for task in item.get("tasks", [])
    ]
    task_id = next_registry_id("TASK", all_tasks)
    cycle_dir = root / "collaboration" / "cycles" / cycle["cycle_id"]
    cycle_dir.mkdir(parents=True, exist_ok=True)
    brief_rel = Path("collaboration") / "cycles" / cycle["cycle_id"] / f"{task_id}_{args.role}_BRIEF.md"
    brief = root / brief_rel
    repertoire_rel = brief_rel.with_name(f"{task_id}_{args.role}_REPERTOIRE.json")
    repertoire = build_packet(args.role, f"{args.problem}\n{cycle['question']}")
    source_root_rel = brief_rel.parent / f"{task_id}_{args.role}_SOURCES"
    repertoire['source_root'] = str(root / source_root_rel)
    repertoire['source_root_project_relative'] = str(source_root_rel)
    source_inputs = []
    for source in repertoire['source_files']:
        source_path = SKILL_ROOT / source['skill_relative_path']
        target_rel = source_root_rel / source['source_path']
        target_path = root / target_rel
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        if file_sha256(target_path) != source['sha256']:
            raise RuntimeError(f"Fonte de repertório mudou durante a cópia: {source['source_path']}")
        source['project_relative_path'] = str(target_rel)
        source['resolved_path'] = str(target_path)
        source_inputs.append({'path': str(target_rel), 'sha256': source['sha256']})
    cycle.setdefault('input_artifacts', []).extend(source_inputs)
    repertoire_path = root / repertoire_rel
    repertoire_path.write_text(json.dumps(repertoire, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    repertoire_hash = file_sha256(repertoire_path)
    cycle.setdefault("input_artifacts", []).append({"path": str(repertoire_rel), "sha256": repertoire_hash})
    inputs = "\n".join(
        f"- `{item['path']}` — `{item['sha256']}`"
        for item in cycle.get("input_artifacts", [])
    ) or "- Nenhum artefato canônico anterior; trabalhar apenas com fontes registradas."
    provenance = runtime_provenance()
    brief.write_text(
        f"# {task_id} — {args.role}\n\n"
        f"- Ciclo: `{cycle['cycle_id']}`\n"
        f"- Fase: `{cycle['phase']}`\n"
        f"- Ator: `{args.actor_type}` / `{args.actor_id}`\n"
        f"- Problema a resolver: {args.problem}\n"
        f"- Deve preservar: {args.must_preserve or cycle['must_preserve']}\n"
        f"- Pode propor: {args.may_propose}\n"
        f"- Mudanças proibidas: {args.prohibited_changes}\n"
        f"- Entrega exigida: {args.deliverable}\n"
        f"- Teste de aceite: {args.acceptance_test}\n\n"
        f"## Runtime obrigatório\n\n"
        f"- Path: `{provenance['runtime_path']}`\n"
        f"- Version: `{provenance['runtime_version']}`\n"
        f"- SHA-256: `{provenance['runtime_sha256']}`\n"
        f"- A submissão será recusada se o especialista reportar outro runtime.\n\n"
        f"## Entradas com hash\n\n{inputs}\n\n"
        f"## Conhecimento e repertório do departamento\n\n"
        f"Leia `{repertoire_rel}`: contém contratos da especialidade, formação curricular, "
        f"referências recuperadas e seus limites. Abra as fontes relevantes indicadas no pacote.\n\n"
        f"As fontes desta rodada estão preservadas em `{source_root_rel}`. Use os caminhos "
        f"`project_relative_path`/`resolved_path` do pacote; os caminhos da biblioteca registram "
        f"somente a origem. As cópias do projeto são verificadas na revisão.\n\n"
        f"No parecer, explique qual referência foi consultada, seu nível de evidência, o mecanismo "
        f"considerado, a proposta nova para este filme e a dependência/conflito a discutir com outra área. "
        f"Se não houver referência útil, declare a lacuna e proponha uma hipótese testável. "
        f"Não trate uma leitura parcial como filme assistido; não transforme cautelas documentais "
        f"em substituto da criação. Preserve liberdade para rejeitar um precedente inadequado.\n",
        encoding="utf-8",
    )
    task = {
        "task_id": task_id,
        "role": args.role,
        "actor_type": args.actor_type,
        "actor_id": args.actor_id,
        "problem": args.problem,
        "must_preserve": args.must_preserve or cycle["must_preserve"],
        "may_propose": args.may_propose,
        "prohibited_changes": args.prohibited_changes,
        "required_deliverable": args.deliverable,
        "acceptance_test": args.acceptance_test,
        **provenance,
        "brief_path": str(brief_rel),
        "repertoire_path": str(repertoire_rel),
        "repertoire_sha256": repertoire_hash,
        "status": "ASSIGNED",
        "assigned_at": now_iso(),
    }
    cycle["tasks"].append(task)
    cycle["status"] = "DISPATCHED"
    state.setdefault("role_assignments", []).append({
        "cycle_id": cycle["cycle_id"],
        **{key: task[key] for key in ("task_id", "role", "actor_type", "actor_id", "status")},
    })
    append_room(root, f"{task_id} — ATRIBUÍDA", [
        f"Papel: `{args.role}`",
        f"Ator: `{args.actor_type}` / `{args.actor_id}`",
        f"Problema: {args.problem}",
        f"Brief: `{brief_rel}`",
    ])
    save_state(root, state)
    print(json.dumps(task, ensure_ascii=False, indent=2))
    return 0


def command_submit_task(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    cycle, task = find_task(state, args.task)
    if task["status"] != "ASSIGNED":
        raise RuntimeError(f"Tarefa não aceita submissão: {task['status']}")
    reported_path = str(args.runtime_path.expanduser().resolve())
    expected = {
        "runtime_path": task.get("runtime_path"),
        "runtime_sha256": task.get("runtime_sha256"),
        "runtime_version": task.get("runtime_version"),
    }
    reported = {
        "runtime_path": reported_path,
        "runtime_sha256": args.runtime_sha256,
        "runtime_version": args.runtime_version,
    }
    mismatch = [key for key in expected if expected[key] != reported[key]]
    if mismatch:
        raise RuntimeError(
            "Runtime provenance mismatch: "
            + ", ".join(
                f"{key} esperado={expected[key]!r} reportado={reported[key]!r}"
                for key in mismatch
            )
        )
    submission = args.file.expanduser()
    submission = (submission if submission.is_absolute() else root / submission).resolve()
    try:
        relative = submission.relative_to(root)
    except ValueError as exc:
        raise ValueError("Submissão precisa estar dentro do projeto") from exc
    if not submission.is_file():
        raise FileNotFoundError(f"Submissão ausente: {submission}")
    if submission.stat().st_size < 120:
        raise RuntimeError("Submissão insuficiente; parecer precisa ser verificável")
    task.update({
        "status": "SUBMITTED",
        "submission_path": str(relative),
        "submission_sha256": file_sha256(submission),
        "submitted_at": now_iso(),
        "dissent_or_risk": args.dissent_or_risk,
        "runtime_provenance_reported": reported,
    })
    for assignment in state.get("role_assignments", []):
        if assignment.get("task_id") == task["task_id"]:
            assignment.update({
                "status": "SUBMITTED",
                "submission_path": task["submission_path"],
                "submission_sha256": task["submission_sha256"],
            })
    if all(item.get("status") == "SUBMITTED" for item in cycle["tasks"]):
        cycle["status"] = "SUBMITTED"
    append_room(root, f"{task['task_id']} — SUBMETIDA", [
        f"Papel: `{task['role']}`",
        f"Parecer: `{relative}`",
        f"Hash: `{task['submission_sha256']}`",
        f"Dissenso/risco: {args.dissent_or_risk}",
    ])
    save_state(root, state)
    print(json.dumps(task, ensure_ascii=False, indent=2))
    return 0


def command_director_review(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    cycle = find_cycle(state, args.cycle)
    if cycle.get("status") not in {"OPEN", "DISPATCHED", "SUBMITTED"}:
        raise RuntimeError("Rodada já encerrada; abra uma sucessora para nova revisão")
    tasks = cycle.get("tasks", [])
    if not any(task.get("status") == "SUBMITTED" for task in tasks):
        raise RuntimeError("Revisão exige ao menos um parecer submetido")
    if args.verdict not in {"REVISE", "REJECT"} and any(
        task.get("status") != "SUBMITTED" for task in tasks
    ):
        raise RuntimeError("Este veredito exige todas as submissões do ciclo")
    if args.actor_id in {task.get("actor_id") for task in cycle["tasks"]}:
        raise RuntimeError("Diretor não pode revisar parecer produzido pelo mesmo actor_id")
    changed_inputs = changed_cycle_inputs(root, cycle)
    if changed_inputs:
        invalidate_stale_cycle(root, state, cycle, changed_inputs)
        save_state(root, state)
        raise RuntimeError(
            "Entradas mudaram depois do dispatch; ciclo marcado REVISION_REQUIRED. "
            "Abra nova rodada: "
            + ", ".join(changed_inputs)
        )
    if args.verdict not in DIRECTOR_VERDICTS:
        raise ValueError(f"Veredito inválido: {args.verdict}")
    if args.verdict == "ACCEPT":
        roles = {task["role"] for task in cycle["tasks"]}
        missing = [role for role in PHASE_REQUIRED_ROLES.get(cycle["phase"], ()) if role not in roles]
        if missing:
            raise RuntimeError("Papéis obrigatórios ausentes: " + ", ".join(missing))
        status = "ACCEPTED_BY_DIRECTOR"
    elif args.verdict == "REJECT":
        status = "REJECTED"
    else:
        status = "REVISION_REQUIRED"
    review = {
        "review_id": next_registry_id("REVIEW", state.setdefault("director_reviews", [])),
        "cycle_id": cycle["cycle_id"],
        "phase": cycle["phase"],
        "actor_id": args.actor_id,
        "verdict": args.verdict,
        "reason": args.reason,
        "integration_target": args.integration_target,
        "reviewed_at": now_iso(),
    }
    cancelled = []
    for task in tasks:
        if task.get("status") != "SUBMITTED":
            task["status"] = "CANCELLED_BY_DIRECTOR"
            task["cancelled_at"] = review["reviewed_at"]
            task["cancellation_reason"] = args.reason
            cancelled.append(task["task_id"])
    review["cancelled_task_ids"] = cancelled
    cycle["director_review"] = review
    cycle["status"] = status
    state["director_reviews"].append(review)
    for assignment in state.get("role_assignments", []):
        if assignment.get("cycle_id") == cycle["cycle_id"]:
            assignment["status"] = status
    if args.verdict == "ACCEPT":
        registry = state.setdefault("handoff_registry", {})
        handoff_id = f"HANDOFF-{len(registry) + 1:03d}"
        registry[handoff_id] = {
            "handoff_id": handoff_id,
            "cycle_id": cycle["cycle_id"],
            "phase": cycle["phase"],
            "from_roles": [task["role"] for task in cycle["tasks"]],
            "to_role": "DIRECTOR_CANONICAL_INTEGRATION",
            "input_artifacts": cycle.get("input_artifacts", []),
            "submissions": [
                {
                    "task_id": task["task_id"],
                    "path": task["submission_path"],
                    "sha256": task["submission_sha256"],
                }
                for task in cycle["tasks"]
            ],
            "integration_target": args.integration_target,
            "status": "ACCEPTED_BY_DIRECTOR",
            "accepted_at": now_iso(),
        }
        review["handoff_id"] = handoff_id
    review_dir = root / "collaboration" / "reviews"
    review_dir.mkdir(parents=True, exist_ok=True)
    review_rel = Path("collaboration") / "reviews" / f"{review['review_id']}_{cycle['cycle_id']}.md"
    (root / review_rel).write_text(
        f"# {review['review_id']} — revisão do diretor\n\n"
        f"- Ciclo: `{cycle['cycle_id']}`\n"
        f"- Fase: `{cycle['phase']}`\n"
        f"- Veredito: `{args.verdict}`\n"
        f"- Motivo: {args.reason}\n"
        f"- Integração canônica: {args.integration_target}\n",
        encoding="utf-8",
    )
    append_room(root, f"{review['review_id']} — {args.verdict}", [
        f"Ciclo: `{cycle['cycle_id']}`",
        f"Motivo do diretor: {args.reason}",
        f"Destino de integração: {args.integration_target}",
        f"Estado: `{status}`",
    ])
    save_state(root, state)
    print(json.dumps(review, ensure_ascii=False, indent=2))
    return 0


def command_migrate(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    version = int(state.get("schema_version", 1))
    if version == SCHEMA_VERSION:
        print("UNCHANGED schema já está em v2")
        return 0
    if version != 1:
        raise RuntimeError(f"Schema desconhecido; migração recusada: {version}")
    plan = {
        "from_schema": 1,
        "to_schema": SCHEMA_VERSION,
        "preserve": ["01_BRIEF_STRATEGY", "02_CREATIVE_DIRECTION"],
        "revise_from": "03_SCRIPT",
        "create": [ROOM_NAME, "03_ROTEIRO_LITERARIO.md", "06_ROTEIRO_TECNICO.md", "06_SHOT_LIST.md"],
        "legacy_source": "06_DECUPAGEM_SHOTLIST.md" if (root / "06_DECUPAGEM_SHOTLIST.md").is_file() else None,
    }
    if args.dry_run:
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(root / STATE_NAME, root / f"{STATE_NAME}.v1-backup-{stamp}")
    for directory in (
        "collaboration/cycles", "collaboration/handoffs", "collaboration/reviews",
        "departments/research", "departments/script", "departments/performance",
        "departments/cinematography", "departments/production-design",
        "departments/edit-sound", "departments/production", "departments/storyboard",
        "departments/vfx-ai", "departments/post-qa",
    ):
        (root / directory).mkdir(parents=True, exist_ok=True)
    state["schema_version"] = SCHEMA_VERSION
    state["runtime"] = RUNTIME_VERSION
    state["execution_mode"] = "MULTI_AGENT"
    state["script_mode"] = args.script_mode
    state["workflow_registry"] = {phase["id"]: [] for phase in PHASES}
    state["handoff_registry"] = {}
    state["director_reviews"] = []
    state["role_assignments"] = []
    state["internal_locks"] = {lock: "OPEN" for lock in PHASE_INTERNAL_LOCK.values()}
    state["legacy_acceptance_exemptions"] = ["01_BRIEF_STRATEGY", "02_CREATIVE_DIRECTION"]
    if state.get("phases", {}).get("02_CREATIVE_DIRECTION", {}).get("status") in COMPLETE_STATES:
        state["internal_locks"]["DIRECTION_LOCK"] = "ACCEPTED_LEGACY"
    for phase in PHASES:
        phase_state = state["phases"].setdefault(phase["id"], {})
        phase_state["documents"] = phase["docs"]
    materialize_doc(root, ROOM_NAME, state)
    materialize_doc(root, "03_ROTEIRO_LITERARIO.md", state)
    materialize_doc(root, "06_ROTEIRO_TECNICO.md", state)
    materialize_doc(root, "06_SHOT_LIST.md", state)
    if (root / "06_DECUPAGEM_SHOTLIST.md").is_file():
        state.setdefault("artifact_registry", {}).setdefault("06_DECUPAGEM_SHOTLIST.md", {}).update({
            "status": "LEGACY_SOURCE",
            "sha256": file_sha256(root / "06_DECUPAGEM_SHOTLIST.md"),
        })
    for phase in PHASES[PHASE_INDEX["03_SCRIPT"]:]:
        phase_state = state["phases"][phase["id"]]
        if phase["id"] == "03_SCRIPT" or phase_state.get("status") != "PENDING":
            phase_state["status"] = "REVISE"
            phase_state["approved_at"] = None
            phase_state["approved_by"] = None
        for filename in phase["docs"]:
            if (root / filename).is_file():
                state.setdefault("artifact_registry", {}).setdefault(filename, {}).update({
                    "phase": phase["id"],
                    "status": "STALE" if filename == "03_ROTEIRO_AV.md" else "IN_PROGRESS",
                })
    state["current_phase"] = "03_SCRIPT"
    state["next_action"] = "Abrir ciclo multiagente de roteiro e criar roteiro literário"
    state["revision"] = int(state.get("revision", 1)) + 1
    state.setdefault("revision_log", []).append({
        "at": now_iso(),
        "type": "SCHEMA_MIGRATION",
        "from_schema": 1,
        "to_schema": SCHEMA_VERSION,
        "reason": "Restaurar entregáveis canônicos e sala de direção multiagente",
    })
    save_state(root, state)
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


def command_complete(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    phase_id = args.phase or state["current_phase"]
    phase = state["phases"][phase_id]
    if phase["status"] in COMPLETE_STATES:
        changed: list[str] = []
        for filename in PHASE_BY_ID[phase_id]["docs"]:
            path = root / filename
            registered = state.get("artifact_registry", {}).get(filename, {})
            expected = registered.get("sha256")
            if not path.is_file() or not expected or file_sha256(path) != expected:
                changed.append(filename)
        if changed:
            print(
                "ERRO: fase concluída foi alterada sem change control; execute "
                f"revise-from em {phase_id}: {', '.join(changed)}",
                file=sys.stderr,
            )
            return 6
        print(f"UNCHANGED {phase_id} já está {phase['status']}")
        return 0
    errors = validate_phase(root, state, phase_id)
    if errors:
        print("ERRO: fase não pode ser concluída", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 3
    phase["status"] = "COMPLETE_DRAFT"
    phase["completed_at"] = now_iso()
    state["revision"] = int(state["revision"]) + 1
    for filename in PHASE_BY_ID[phase_id]["docs"]:
        state["artifact_registry"].setdefault(filename, {})
        state["artifact_registry"][filename].update({
            "phase": phase_id,
            "status": "COMPLETE_DRAFT",
            "sha256": file_sha256(root / filename),
            "revision": state["revision"],
        })
    following = next_phase(phase_id)
    if following:
        state["current_phase"] = following
        state["next_action"] = f"Iniciar {following} com ensure-phase"
    else:
        state["next_action"] = "Revisão humana e entrega; não marcar FINAL sem aprovação"
    if phase_id == "02_CREATIVE_DIRECTION":
        state["direction_version"] = max(1, int(state["direction_version"]))
    if phase_id in PHASE_INTERNAL_LOCK:
        state.setdefault("internal_locks", {})[PHASE_INTERNAL_LOCK[phase_id]] = "ACCEPTED_BY_DIRECTOR"
    save_state(root, state)
    print(json.dumps({"completed": phase_id, "next": following}, ensure_ascii=False))
    return 0


def command_approve(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    phase_id = args.phase
    phase = state["phases"][phase_id]
    if phase["status"] not in COMPLETE_STATES:
        print(f"ERRO: {phase_id} ainda não está concluída", file=sys.stderr)
        return 4
    integrity_errors = artifact_integrity_errors(root, state, phase_id)
    if integrity_errors:
        print(
            f"ERRO: {phase_id} foi alterada sem revise-from: "
            + "; ".join(integrity_errors),
            file=sys.stderr,
        )
        return 6
    if phase["status"] == "APPROVED" and phase["approved_by"] == args.by:
        print(f"UNCHANGED {phase_id} já aprovado por {args.by}")
        return 0
    phase["status"] = "APPROVED"
    phase["approved_at"] = now_iso()
    phase["approved_by"] = args.by
    state["revision"] = int(state["revision"]) + 1
    if phase_id in PHASE_GATE:
        state["human_gates"][PHASE_GATE[phase_id]] = "APPROVED"
    for filename in PHASE_BY_ID[phase_id]["docs"]:
        state["artifact_registry"].setdefault(filename, {})
        state["artifact_registry"][filename]["status"] = "APPROVED"
    state["revision_log"].append({
        "at": now_iso(),
        "type": "HUMAN_APPROVAL",
        "phase": phase_id,
        "by": args.by,
        "note": args.note,
    })
    save_state(root, state)
    print(f"APPROVED {phase_id} por {args.by}")
    return 0


def command_revise_from(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    start = PHASE_INDEX[args.phase]
    affected: list[str] = []
    for phase in PHASES[start:]:
        phase_state = state["phases"][phase["id"]]
        if phase_state["status"] != "PENDING":
            phase_state["status"] = "REVISE"
            phase_state["approved_at"] = None
            phase_state["approved_by"] = None
            affected.append(phase["id"])
            if phase["id"] in PHASE_GATE:
                state["human_gates"][PHASE_GATE[phase["id"]]] = "OPEN"
            for filename in phase["docs"]:
                if filename in state["artifact_registry"]:
                    state["artifact_registry"][filename]["status"] = "STALE"
        if phase["id"] in PHASE_INTERNAL_LOCK:
            state.setdefault("internal_locks", {})[PHASE_INTERNAL_LOCK[phase["id"]]] = "OPEN"
    state["current_phase"] = args.phase
    state["next_action"] = f"Revisar {args.phase} e propagar mudança"
    if args.phase in {"01_BRIEF_STRATEGY", "02_CREATIVE_DIRECTION"}:
        state["direction_version"] = int(state["direction_version"]) + 1
    state["revision"] = int(state["revision"]) + 1
    state["revision_log"].append({
        "at": now_iso(),
        "type": "CHANGE_CONTROL",
        "from_phase": args.phase,
        "reason": args.reason,
        "affected": affected,
    })
    save_state(root, state)
    print(json.dumps({"revise_from": args.phase, "affected": affected}, ensure_ascii=False))
    return 0


def command_validate(args: argparse.Namespace) -> int:
    root, state = load_state(args.project_dir)
    errors: list[str] = []
    if int(state.get("schema_version", 1)) != SCHEMA_VERSION:
        errors.append("schema legado; execute migrate antes de continuar")
    if not (root / ROOM_NAME).is_file():
        errors.append(f"arquivo ausente: {ROOM_NAME}")
    saw_open = False
    for phase in PHASES:
        status = state["phases"][phase["id"]]["status"]
        if status in COMPLETE_STATES:
            errors.extend(f"{phase['id']}: {item}" for item in validate_phase(root, state, phase["id"]))
            errors.extend(
                f"{phase['id']}: {item} sem revise-from"
                for item in artifact_integrity_errors(root, state, phase["id"])
            )
            if saw_open:
                errors.append(f"{phase['id']}: fase concluída depois de dependência aberta")
        elif status in {"PENDING", "IN_PROGRESS", "REVISE"}:
            saw_open = True
            if status in {"IN_PROGRESS", "REVISE"}:
                for filename in phase["docs"]:
                    if not (root / filename).is_file():
                        errors.append(f"{phase['id']}: arquivo ausente: {filename}")
        else:
            errors.append(f"{phase['id']}: status desconhecido: {status}")
    active_ids = state.get("id_registry", {}).get("active", [])
    retired_ids = state.get("id_registry", {}).get("retired", [])
    if len(active_ids) != len(set(active_ids)):
        errors.append("id_registry.active contém IDs duplicados")
    if len(retired_ids) != len(set(retired_ids)):
        errors.append("id_registry.retired contém IDs duplicados")
    overlap = sorted(set(active_ids) & set(retired_ids))
    if overlap:
        errors.append(f"IDs simultaneamente ativos e aposentados: {', '.join(overlap)}")
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 5
    print("VALID")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Runtime de projeto commercial-film-director")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Inicializa pacote sem sobrescrever")
    init_parser.add_argument("--project", required=True)
    init_parser.add_argument("--client", default="A CONFIRMAR")
    init_parser.add_argument("--output", required=True, type=Path)
    init_parser.add_argument("--directory-name")
    init_parser.add_argument(
        "--approval-policy",
        choices=["AUTONOMOUS_DRAFT", "HUMAN_LOCK"],
        default="AUTONOMOUS_DRAFT",
    )
    init_parser.set_defaults(func=command_init)

    for name, function in (("status", command_status), ("validate", command_validate)):
        command_parser = subparsers.add_parser(name)
        command_parser.add_argument("--project-dir", required=True, type=Path)
        command_parser.set_defaults(func=function)

    ensure_parser = subparsers.add_parser("ensure-phase")
    ensure_parser.add_argument("--project-dir", required=True, type=Path)
    ensure_parser.add_argument("--phase", required=True, choices=list(PHASE_BY_ID))
    ensure_parser.set_defaults(func=command_ensure)

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("--project-dir", required=True, type=Path)
    complete_parser.add_argument("--phase", choices=list(PHASE_BY_ID))
    complete_parser.set_defaults(func=command_complete)

    approve_parser = subparsers.add_parser("approve")
    approve_parser.add_argument("--project-dir", required=True, type=Path)
    approve_parser.add_argument("--phase", required=True, choices=list(PHASE_BY_ID))
    approve_parser.add_argument("--by", required=True)
    approve_parser.add_argument("--note", default="Aprovação explícita registrada no turno")
    approve_parser.set_defaults(func=command_approve)

    revise_parser = subparsers.add_parser("revise-from")
    revise_parser.add_argument("--project-dir", required=True, type=Path)
    revise_parser.add_argument("--phase", required=True, choices=list(PHASE_BY_ID))
    revise_parser.add_argument("--reason", required=True)
    revise_parser.set_defaults(func=command_revise_from)

    open_cycle = subparsers.add_parser("open-cycle")
    open_cycle.add_argument("--project-dir", required=True, type=Path)
    open_cycle.add_argument("--phase", required=True, choices=list(PHASE_BY_ID))
    open_cycle.add_argument("--question", required=True)
    open_cycle.add_argument("--must-preserve", required=True)
    open_cycle.add_argument("--parent-cycle")
    open_cycle.set_defaults(func=command_open_cycle)

    assign = subparsers.add_parser("assign-task")
    assign.add_argument("--project-dir", required=True, type=Path)
    assign.add_argument("--cycle", required=True)
    assign.add_argument("--role", required=True)
    assign.add_argument("--actor-type", required=True, choices=sorted(ACTOR_TYPES))
    assign.add_argument("--actor-id", required=True)
    assign.add_argument("--problem", required=True)
    assign.add_argument("--must-preserve", default="")
    assign.add_argument("--may-propose", required=True)
    assign.add_argument("--prohibited-changes", required=True)
    assign.add_argument("--deliverable", required=True)
    assign.add_argument("--acceptance-test", required=True)
    assign.set_defaults(func=command_assign_task)

    submit = subparsers.add_parser("submit-task")
    submit.add_argument("--project-dir", required=True, type=Path)
    submit.add_argument("--task", required=True)
    submit.add_argument("--file", required=True, type=Path)
    submit.add_argument("--dissent-or-risk", required=True)
    submit.add_argument("--runtime-path", required=True, type=Path)
    submit.add_argument("--runtime-version", required=True)
    submit.add_argument("--runtime-sha256", required=True)
    submit.set_defaults(func=command_submit_task)

    review = subparsers.add_parser("director-review")
    review.add_argument("--project-dir", required=True, type=Path)
    review.add_argument("--cycle", required=True)
    review.add_argument("--actor-id", required=True)
    review.add_argument("--verdict", required=True, choices=sorted(DIRECTOR_VERDICTS))
    review.add_argument("--reason", required=True)
    review.add_argument("--integration-target", required=True)
    review.set_defaults(func=command_director_review)

    migrate = subparsers.add_parser("migrate")
    migrate.add_argument("--project-dir", required=True, type=Path)
    migrate_mode = migrate.add_mutually_exclusive_group(required=True)
    migrate_mode.add_argument("--dry-run", action="store_true")
    migrate_mode.add_argument("--apply", action="store_true")
    migrate.add_argument(
        "--script-mode",
        choices=["LITERARY_THEN_AV", "AV_ONLY"],
        default="LITERARY_THEN_AV",
    )
    migrate.set_defaults(func=command_migrate)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if hasattr(args, 'project_dir'):
            with project_lock(args.project_dir):
                return int(args.func(args))
        return int(args.func(args))
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
