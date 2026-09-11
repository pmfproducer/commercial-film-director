#!/usr/bin/env python3
"""Testes do runtime multiagente e da migração da Commercial Film Director."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RUNTIME = Path(__file__).with_name("project_runtime.py")
SKILL_ROOT = RUNTIME.parents[1]
PLACEHOLDER_RE = re.compile(r"<<PREENCHER[^>]*>>")
PHASES = [
    "01_BRIEF_STRATEGY", "02_CREATIVE_DIRECTION", "03_SCRIPT",
    "04_DIRECTOR_TREATMENT", "05_VISUAL_SOUND_SYSTEM", "06_DECOUPAGE",
    "07_ASSETS_CONTINUITY", "08_STORYBOARD_PREVIS", "09_AI_EXECUTION_PLAN",
    "10_SHOT_PACKETS", "11_POST_DELIVERY", "12_QA_VERSIONS",
]
REQUIRED_ROLES = {
    "01_BRIEF_STRATEGY": ("RESEARCHER",),
    "02_CREATIVE_DIRECTION": ("CREATIVE_DIRECTOR", "SCREENWRITER", "CRITIC"),
    "03_SCRIPT": ("SCREENWRITER", "CRITIC"),
    "04_DIRECTOR_TREATMENT": ("PERFORMANCE_DIRECTOR", "CRITIC"),
    "05_VISUAL_SOUND_SYSTEM": ("DP", "PRODUCTION_DESIGNER", "EDITOR", "SOUND_DESIGNER", "CRITIC"),
    "06_DECOUPAGE": ("DP", "EDITOR", "PRODUCER_AD", "CRITIC"),
    "07_ASSETS_CONTINUITY": ("PRODUCTION_DESIGNER", "CONTINUITY_SUPERVISOR"),
    "08_STORYBOARD_PREVIS": ("STORYBOARD_ARTIST", "DP", "EDITOR", "CRITIC"),
    "09_AI_EXECUTION_PLAN": ("PRODUCER_AD", "VFX_AI_SUPERVISOR"),
    "10_SHOT_PACKETS": ("VFX_AI_SUPERVISOR", "CRITIC"),
    "11_POST_DELIVERY": ("EDITOR", "SOUND_DESIGNER", "POST_QA"),
    "12_QA_VERSIONS": ("POST_QA", "CRITIC"),
}


def run(*args: str, expect: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [sys.executable, str(RUNTIME), *args], text=True,
        capture_output=True, check=False,
    )
    if result.returncode != expect:
        raise AssertionError(
            f"retorno {result.returncode}, esperado {expect}\n"
            f"cmd: {' '.join(args)}\nstdout: {result.stdout}\nstderr: {result.stderr}"
        )
    return result


def state(project: Path) -> dict:
    return json.loads((project / "00_PROJECT_STATE.json").read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fill(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    path.write_text(
        PLACEHOLDER_RE.sub("DECISÃO APLICADA, TESTÁVEL E OBSERVÁVEL", source),
        encoding="utf-8",
    )


def fill_phase(project: Path, phase: str) -> None:
    if phase == "06_DECOUPAGE":
        (project / "06_ROTEIRO_TECNICO.md").write_text(
            """# 06A — Roteiro técnico

- Duração alvo (s): 1

## Planos

| PLAN ID | SCENE ID | IN/OUT | Duração física | Função e informação nova | Ação/performance | Enquadramento e posição | Câmera/movimento | LENS-SET/focal/foco/DOF | TIME-STATE | LIGHT-STATE/LOOK | Arte/PRD/PRP/WDR | Som/transição | Rota/teste/fallback | Status |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| `PL-010` | `SC-010` | entrada/saída | 1 s | causa observável | ação completa | plano médio | lock-off | `LENS-SET-001`; Viabilidade de foco/DOF testável | `TIME-STATE-001` | `LIGHT-STATE-001` / `LOOK-001` | `POINT-001`, `PRD-001` | evento causal | teste e fallback | TRABALHO |

## Reconciliação técnica

Ação, eixo, física, cobertura, POINT IDs canônicos e parecer do diretor foram documentados de forma verificável.
""",
            encoding="utf-8",
        )
        (project / "06_SHOT_LIST.md").write_text(
            """# 06B — Shot list operacional

## Ordem operacional

| Ordem | PLAN ID | Cena/setup | Locação | Elenco/ação | Duração útil | Handles | Câmera/rig/lente | Luz | Arte/props/produto | Som | Formato | Prioridade | Dependências/reset | Risco/fallback | Status |
|---:|---|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | `PL-010` | `SC-010`/setup único | locação teste | ação completa | 1 s | 12f por lado | lock-off / `LENS-SET-001` | `LIGHT-STATE-001` | `PRD-001` | evento causal | 16:9/24fps | A | reset registrado | fallback lock | TRABALHO |

## Checagem de derivação

Todos os PLAN ID aparecem uma vez. Produção/AD validou ordem operacional, recursos, resets e contingências; Parecer do diretor: rodada aceita.
""",
            encoding="utf-8",
        )
        return
    for filename in state(project)["phases"][phase]["documents"]:
        fill(project / filename)


def open_cycle(project: Path, phase: str, parent: str | None = None) -> str:
    args = [
        "open-cycle", "--project-dir", str(project), "--phase", phase,
        "--question", f"Resolver cinematograficamente {phase}",
        "--must-preserve", "briefing, direção, causalidade e IDs",
    ]
    if parent:
        args.extend(["--parent-cycle", parent])
    return json.loads(run(*args).stdout)["cycle_id"]


def assign_submit(project: Path, cycle: str, phase: str, role: str) -> str:
    actor_id = f"agent-{phase.lower()}-{role.lower()}"
    task = json.loads(run(
        "assign-task", "--project-dir", str(project), "--cycle", cycle,
        "--role", role, "--actor-type", "TEMP_SUBAGENT", "--actor-id", actor_id,
        "--problem", f"Aplicar o cérebro de {role}",
        "--may-propose", "solução dentro da trava",
        "--prohibited-changes", "não reescrever decisão a montante",
        "--deliverable", f"parecer verificável de {role}",
        "--acceptance-test", "função, mecanismo, execução, risco e fallback",
    ).stdout)
    out = project / "departments" / "test" / f"{cycle}_{role}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        f"# Parecer {role}\n\nProposta independente para {phase}. Recebe a "
        "trava, decide uma escolha concreta, explica função e mecanismo, aplica "
        "no filme, registra risco, teste, contraindicação e fallback sem alterar "
        "a decisão a montante.\n",
        encoding="utf-8",
    )
    run(
        "submit-task", "--project-dir", str(project), "--task", task["task_id"],
        "--file", str(out), "--dissent-or-risk", "risco registrado e testável",
        "--runtime-path", task["runtime_path"],
        "--runtime-version", task["runtime_version"],
        "--runtime-sha256", task["runtime_sha256"],
    )
    return actor_id


def room_cycle(
    project: Path, phase: str, verdict: str = "ACCEPT",
    parent: str | None = None, test_self_review: bool = False,
    test_wrong_role: bool = False,
) -> str:
    cycle = open_cycle(project, phase, parent)
    if test_wrong_role:
        run(
            "assign-task", "--project-dir", str(project), "--cycle", cycle,
            "--role", "DP", "--actor-type", "TEMP_SUBAGENT", "--actor-id", "early-dp",
            "--problem", "fotografia antes da hora", "--may-propose", "imagem",
            "--prohibited-changes", "direção", "--deliverable", "parecer",
            "--acceptance-test", "ordem causal", expect=1,
        )
    actors = [assign_submit(project, cycle, phase, role) for role in REQUIRED_ROLES[phase]]
    if test_self_review:
        run(
            "director-review", "--project-dir", str(project), "--cycle", cycle,
            "--actor-id", actors[0], "--verdict", "ACCEPT",
            "--reason", "autoaprovação inválida",
            "--integration-target", "documentos canônicos", expect=1,
        )
    run(
        "director-review", "--project-dir", str(project), "--cycle", cycle,
        "--actor-id", "root-director", "--verdict", verdict,
        "--reason", "decisão baseada em função, mecanismo, execução e teste",
        "--integration-target", "documentos canônicos da fase",
    )
    return cycle


def assert_static_contracts() -> None:
    templates = SKILL_ROOT / "assets" / "project-template"
    for filename in (
        "00_SALA_DE_DIRECAO.md", "03_ROTEIRO_LITERARIO.md", "03_ROTEIRO_AV.md",
        "06_ROTEIRO_TECNICO.md", "06_SHOT_LIST.md",
    ):
        assert (templates / filename).is_file(), f"template ausente: {filename}"
    assert not (templates / "06_DECUPAGEM_SHOTLIST.md").exists()
    literary = (templates / "03_ROTEIRO_LITERARIO.md").read_text(encoding="utf-8")
    for marker in ("INT./EXT.", "DIA/NOITE", "PERSONAGEM", "Parecer do diretor"):
        assert marker in literary
    technical = (templates / "06_ROTEIRO_TECNICO.md").read_text(encoding="utf-8")
    shot_list = (templates / "06_SHOT_LIST.md").read_text(encoding="utf-8")
    assert "Duração física" in technical and "Viabilidade de foco/DOF" in technical
    assert "ordem operacional" in shot_list.lower() and "Produção/AD" in shot_list
    skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    for marker in ("multiagente", "ACCEPTED_BY_DIRECTOR", "03_ROTEIRO_LITERARIO.md"):
        assert marker in skill
    for asset in (
        "PMF_MODELOS_DIRECAO_PUBLICITARIA.pdf",
        "PMF_MODELOS_PRODUCAO_AUDIOVISUAL.xlsx",
    ):
        assert (SKILL_ROOT / "assets" / "templates" / asset).is_file()


def test_full_runtime(root: Path) -> None:
    run("init", "--project", "Pingo", "--client", "Marca Fictícia", "--output", str(root))
    project = root / "FILME_PINGO"
    assert state(project)["schema_version"] == 2
    assert state(project)["execution_mode"] == "MULTI_AGENT"
    assert (project / "00_SALA_DE_DIRECAO.md").is_file()

    fill_phase(project, "01_BRIEF_STRATEGY")
    run("complete", "--project-dir", str(project), "--phase", "01_BRIEF_STRATEGY", expect=3)
    room_cycle(project, "01_BRIEF_STRATEGY")
    run("complete", "--project-dir", str(project), "--phase", "01_BRIEF_STRATEGY")

    for phase in ("02_CREATIVE_DIRECTION",):
        run("ensure-phase", "--project-dir", str(project), "--phase", phase)
        fill_phase(project, phase)
        room_cycle(project, phase, test_wrong_role=True)
        run("complete", "--project-dir", str(project), "--phase", phase)

    run("ensure-phase", "--project-dir", str(project), "--phase", "03_SCRIPT")
    assert (project / "03_ROTEIRO_LITERARIO.md").is_file()
    assert (project / "03_ROTEIRO_AV.md").is_file()
    fill_phase(project, "03_SCRIPT")
    rejected = room_cycle(project, "03_SCRIPT", verdict="MORE_RESEARCH")
    run("complete", "--project-dir", str(project), "--phase", "03_SCRIPT", expect=3)
    room_cycle(project, "03_SCRIPT", parent=rejected)
    run("complete", "--project-dir", str(project), "--phase", "03_SCRIPT")

    for phase in PHASES[3:]:
        run("ensure-phase", "--project-dir", str(project), "--phase", phase)
        fill_phase(project, phase)
        room_cycle(project, phase, test_self_review=(phase == "05_VISUAL_SOUND_SYSTEM"))
        if phase == "06_DECOUPAGE":
            technical = project / "06_ROTEIRO_TECNICO.md"
            source = technical.read_text(encoding="utf-8")
            source = source.replace("Duração alvo (s): 1", "Duração alvo (s): 2")
            source = source.replace("| lock-off |", "| CAM-MOV-001 |")
            duplicate = (
                "| `PL-020` | `SC-020` | entrada/saída | 1 s | nova causa | ação | plano médio | "
                "CAM-MOV-001 | `LENS-SET-001`; Viabilidade de foco/DOF testável | "
                "`TIME-STATE-001` | `LIGHT-STATE-001` / `LOOK-001` | `POINT-002` | "
                "evento | teste | TRABALHO |\n"
            )
            technical.write_text(source.replace("\n\n## Reconciliação técnica", "\n" + duplicate + "\n## Reconciliação técnica"), encoding="utf-8")
            shot_list = project / "06_SHOT_LIST.md"
            shot_source = shot_list.read_text(encoding="utf-8")
            shot_duplicate = (
                "| 2 | `PL-020` | `SC-020` | locação | ação | 1 s | nenhum | lock-off | "
                "`LIGHT-STATE-001` | `PRD-001` | evento | 16:9/24fps | B | reset | fallback | TRABALHO |\n"
            )
            shot_list.write_text(shot_source.replace("\n\n## Checagem de derivação", "\n" + shot_duplicate + "\n## Checagem de derivação"), encoding="utf-8")
            result = run("complete", "--project-dir", str(project), "--phase", phase, expect=3)
            assert "CAM-MOV-001 reutilizado" in result.stderr, result.stderr
            assert "handles não quantificados" in result.stderr, result.stderr
            fill_phase(project, phase)
        run("complete", "--project-dir", str(project), "--phase", phase)

    assert (project / "06_ROTEIRO_TECNICO.md").is_file()
    assert (project / "06_SHOT_LIST.md").is_file()
    assert not (project / "06_DECUPAGEM_SHOTLIST.md").exists()
    run("validate", "--project-dir", str(project))
    st = state(project)
    assert st["human_gates"]["SCRIPT"] == "OPEN"
    assert any(review["verdict"] == "MORE_RESEARCH" for review in st["director_reviews"])
    assert all(st["workflow_registry"][phase] for phase in PHASES)
    assert len(st["handoff_registry"]) == len(PHASES)
    assert all(item["status"] == "ACCEPTED_BY_DIRECTOR" for item in st["handoff_registry"].values())
    assert all(item["status"] in {"ACCEPTED_BY_DIRECTOR", "REVISION_REQUIRED"} for item in st["role_assignments"])
    assert st["internal_locks"]["STORY_LOCK"] == "ACCEPTED_BY_DIRECTOR"
    assert st["internal_locks"]["VISUAL_SYSTEM_LOCK"] == "ACCEPTED_BY_DIRECTOR"
    assert st["internal_locks"]["QA_DOCUMENT_LOCK"] == "ACCEPTED_BY_DIRECTOR"
    assert st["internal_locks"]["PRODUCTION_PLAN_LOCK"] == "ACCEPTED_BY_DIRECTOR"
    assert "PRODUCTION_READY" not in st["internal_locks"]
    assert "FINAL_QA_LOCK" not in st["internal_locks"]

    task = st["workflow_registry"]["12_QA_VERSIONS"][-1]["tasks"][0]
    submission = project / task["submission_path"]
    submission.write_text(submission.read_text(encoding="utf-8") + "\nALTERADO\n", encoding="utf-8")
    run("validate", "--project-dir", str(project), expect=5)


def test_migration(root: Path) -> None:
    run("init", "--project", "Legado", "--client", "PMF", "--output", str(root))
    project = root / "FILME_LEGADO"
    st = state(project)
    st["schema_version"] = 1
    st["runtime"] = "commercial-film-director-v5-department-application"
    for key in (
        "execution_mode", "script_mode", "workflow_registry", "handoff_registry",
        "director_reviews", "role_assignments",
    ):
        st.pop(key, None)
    st["phases"]["03_SCRIPT"]["documents"] = ["03_ROTEIRO_AV.md"]
    st["phases"]["03_SCRIPT"]["status"] = "COMPLETE_DRAFT"
    st["phases"]["06_DECOUPAGE"]["documents"] = ["06_DECUPAGEM_SHOTLIST.md"]
    st["current_phase"] = "04_DIRECTOR_TREATMENT"
    (project / "00_PROJECT_STATE.json").write_text(
        json.dumps(st, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    for filename in (
        "00_SALA_DE_DIRECAO.md", "03_ROTEIRO_LITERARIO.md",
        "06_ROTEIRO_TECNICO.md", "06_SHOT_LIST.md",
    ):
        path = project / filename
        if path.exists():
            path.unlink()
    legacy = project / "06_DECUPAGEM_SHOTLIST.md"
    legacy.write_text(
        "# Legado\n\nConteúdo combinado preservado para migração e auditoria.\n" * 5,
        encoding="utf-8",
    )
    before = sha(project / "00_PROJECT_STATE.json")
    run("migrate", "--project-dir", str(project), "--dry-run")
    assert sha(project / "00_PROJECT_STATE.json") == before
    run("migrate", "--project-dir", str(project), "--apply")
    migrated = state(project)
    assert migrated["schema_version"] == 2
    assert migrated["current_phase"] == "03_SCRIPT"
    assert migrated["phases"]["03_SCRIPT"]["status"] == "REVISE"
    assert migrated["internal_locks"]["STORY_LOCK"] == "OPEN"
    assert migrated["artifact_registry"]["06_DECUPAGEM_SHOTLIST.md"]["status"] == "LEGACY_SOURCE"
    assert (project / "03_ROTEIRO_LITERARIO.md").is_file()
    assert list(project.glob("00_PROJECT_STATE.json.v1-backup-*"))
    run("migrate", "--project-dir", str(project), "--apply")


def test_runtime_provenance_mismatch(root: Path) -> None:
    run("init", "--project", "Provenance", "--client", "Teste", "--output", str(root))
    project = root / "FILME_PROVENANCE"
    fill_phase(project, "01_BRIEF_STRATEGY")
    cycle = open_cycle(project, "01_BRIEF_STRATEGY")
    task = json.loads(run(
        "assign-task", "--project-dir", str(project), "--cycle", cycle,
        "--role", "RESEARCHER", "--actor-type", "TEMP_SUBAGENT", "--actor-id", "agent-provenance",
        "--problem", "testar provenance", "--may-propose", "fontes",
        "--prohibited-changes", "não trocar runtime", "--deliverable", "parecer",
        "--acceptance-test", "hash exato",
    ).stdout)
    out = project / "departments" / "test" / "provenance.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("# Parecer\n\nConteúdo verificável suficiente para testar a recusa e o aceite do runtime pinado sem qualquer ambiguidade operacional.\n", encoding="utf-8")
    mismatch = run(
        "submit-task", "--project-dir", str(project), "--task", task["task_id"],
        "--file", str(out), "--dissent-or-risk", "nenhum",
        "--runtime-path", task["runtime_path"], "--runtime-version", task["runtime_version"],
        "--runtime-sha256", "0" * 64, expect=1,
    )
    assert "Runtime provenance mismatch" in mismatch.stderr
    run(
        "submit-task", "--project-dir", str(project), "--task", task["task_id"],
        "--file", str(out), "--dissent-or-risk", "nenhum",
        "--runtime-path", task["runtime_path"], "--runtime-version", task["runtime_version"],
        "--runtime-sha256", task["runtime_sha256"],
    )


def test_stale_submitted_cycle_can_reopen(root: Path) -> None:
    run("init", "--project", "Stale", "--client", "Teste", "--output", str(root))
    project = root / "FILME_STALE"
    for phase in PHASES[:6]:
        if phase != "01_BRIEF_STRATEGY":
            run("ensure-phase", "--project-dir", str(project), "--phase", phase)
        fill_phase(project, phase)
        room_cycle(project, phase)
        run("complete", "--project-dir", str(project), "--phase", phase)

    run("ensure-phase", "--project-dir", str(project), "--phase", "07_ASSETS_CONTINUITY")
    stale_cycle = open_cycle(project, "07_ASSETS_CONTINUITY")
    for role in REQUIRED_ROLES["07_ASSETS_CONTINUITY"]:
        assign_submit(project, stale_cycle, "07_ASSETS_CONTINUITY", role)
    assert state(project)["workflow_registry"]["07_ASSETS_CONTINUITY"][-1]["status"] == "SUBMITTED"

    run(
        "revise-from", "--project-dir", str(project), "--phase", "06_DECOUPAGE",
        "--reason", "Falha downstream exige corrigir o pacote técnico",
    )
    rejected = subprocess.run([sys.executable, str(RUNTIME), "complete", "--project-dir", str(project), "--phase", "06_DECOUPAGE"], capture_output=True, text=True)
    assert rejected.returncode != 0, "Human revision must require a fresh accepted review"
    fill_phase(project, "06_DECOUPAGE")
    with (project / "06_SHOT_LIST.md").open("a", encoding="utf-8") as handle:
        handle.write("\nCorreção formal propagada do teste downstream.\n")
    room_cycle(project, "06_DECOUPAGE")
    run("complete", "--project-dir", str(project), "--phase", "06_DECOUPAGE")
    run("ensure-phase", "--project-dir", str(project), "--phase", "07_ASSETS_CONTINUITY")

    fresh_cycle = open_cycle(project, "07_ASSETS_CONTINUITY", parent=stale_cycle)
    cycles = state(project)["workflow_registry"]["07_ASSETS_CONTINUITY"]
    assert cycles[-2]["status"] == "REVISION_REQUIRED"
    assert cycles[-2]["invalidation"]["reason"] == "CHANGE_CONTROL"
    assert cycles[-2]["invalidation"]["human_reason"]
    assert fresh_cycle != stale_cycle


def main() -> int:
    assert_static_contracts()
    with tempfile.TemporaryDirectory(prefix="cfd-v6-") as directory:
        root = Path(directory)
        test_full_runtime(root / "full")
        test_migration(root / "migration")
        test_runtime_provenance_mismatch(root / "provenance")
        test_stale_submitted_cycle_can_reopen(root / "stale")
    print("ALL_MULTIAGENT_RUNTIME_TESTS_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
