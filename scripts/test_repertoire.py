#!/usr/bin/env python3
"""Behavioral regressions for recovered knowledge, portability and real assignment."""
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from prepare_repertoire import BUNDLE, ROLE_MAP, SKILL_ROOT, build_packet, verify_bundle
from project_runtime import changed_cycle_inputs


def run(runtime, *args):
    result = subprocess.run([sys.executable, str(runtime), *map(str, args)], capture_output=True, text=True, check=True)
    return json.loads(result.stdout) if result.stdout.lstrip().startswith('{') else result.stdout


class RepertoireTests(unittest.TestCase):
    def test_concurrent_specialists_do_not_lose_assignments(self):
        runtime = SKILL_ROOT / 'scripts/project_runtime.py'
        with tempfile.TemporaryDirectory() as td:
            run(runtime, 'init', '--project', 'Concurrency fixture', '--client', 'Test', '--output', td, '--directory-name', 'film')
            project = Path(td) / 'film'
            cycle = run(runtime, 'open-cycle', '--project-dir', project, '--phase', '01_BRIEF_STRATEGY', '--question', 'montagem arquivo continuidade', '--must-preserve', 'fixture')
            state_path = project / '00_PROJECT_STATE.json'
            state = json.loads(state_path.read_text())
            # Isolated concurrency fixture, not a claimed creative phase completion.
            state['workflow_registry']['01_BRIEF_STRATEGY'][0]['phase'] = '02_CREATIVE_DIRECTION'
            state_path.write_text(json.dumps(state))
            def assign(role):
                return run(runtime, 'assign-task', '--project-dir', project, '--cycle', cycle['cycle_id'], '--role', role, '--actor-type', 'TEMP_SUBAGENT', '--actor-id', role, '--problem', 'montagem arquivo continuidade', '--may-propose', 'referencias', '--prohibited-changes', 'inventar observação', '--deliverable', 'parecer', '--acceptance-test', 'fontes')
            with ThreadPoolExecutor(2) as pool:
                results = list(pool.map(assign, ['CREATIVE_DIRECTOR', 'SCREENWRITER']))
            tasks = json.loads(state_path.read_text())['workflow_registry']['01_BRIEF_STRATEGY'][0]['tasks']
            self.assertEqual(len(tasks), 2)
            self.assertEqual(len({x['task_id'] for x in tasks}), 2)
            self.assertEqual({x['task_id'] for x in results}, {x['task_id'] for x in tasks})

    def test_submission_relative_path_is_resolved_from_project(self):
        runtime = SKILL_ROOT / 'scripts/project_runtime.py'
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / 'film'
            run(runtime, 'init', '--project', 'Relative path fixture', '--client', 'Test', '--output', td, '--directory-name', 'film')
            cycle = run(runtime, 'open-cycle', '--project-dir', project, '--phase', '01_BRIEF_STRATEGY', '--question', 'revelação visual', '--must-preserve', 'fixture')
            task = run(runtime, 'assign-task', '--project-dir', project, '--cycle', cycle['cycle_id'], '--role', 'RESEARCHER', '--actor-type', 'ROLE_SIMULATION', '--actor-id', 'test-researcher', '--problem', 'revelação visual', '--may-propose', 'referências', '--prohibited-changes', 'inventar observação', '--deliverable', 'departments/researcher.md', '--acceptance-test', 'fontes')
            report = project / 'departments/researcher.md'
            report.parent.mkdir(exist_ok=True)
            report.write_text('Fixture de submissão; testa resolução do arquivo, sem alegar qualidade criativa ou trabalho multiagente. ' * 3)
            command = [sys.executable, str(runtime), 'submit-task', '--project-dir', str(project), '--task', task['task_id'], '--file', 'departments/researcher.md', '--dissent-or-risk', 'fixture', '--runtime-path', task['runtime_path'], '--runtime-version', task['runtime_version'], '--runtime-sha256', task['runtime_sha256']]
            # CLI invoked outside project and skill: the documented relative path still works.
            result = subprocess.run(command, cwd=td, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            state = json.loads((project / '00_PROJECT_STATE.json').read_text())
            submitted = state['workflow_registry']['01_BRIEF_STRATEGY'][0]['tasks'][0]
            self.assertEqual(submitted['submission_path'], 'departments/researcher.md')
            self.assertEqual(submitted['submission_sha256'], hashlib.sha256(report.read_bytes()).hexdigest())

    def test_early_return_cancels_pending_work_without_allowing_acceptance(self):
        runtime = SKILL_ROOT / 'scripts/project_runtime.py'
        for verdict in ('REVISE', 'REJECT'):
            with self.subTest(verdict=verdict), tempfile.TemporaryDirectory() as td:
                project = Path(td) / 'film'
                run(runtime, 'init', '--project', 'Early return fixture', '--client', 'Test', '--output', td, '--directory-name', 'film')
                cycle = run(runtime, 'open-cycle', '--project-dir', project, '--phase', '01_BRIEF_STRATEGY', '--question', 'revelação visual', '--must-preserve', 'fixture')
                state_path = project / '00_PROJECT_STATE.json'
                state = json.loads(state_path.read_text())
                # Isolated lifecycle fixture exposing two roles, not creative phase completion.
                state['workflow_registry']['01_BRIEF_STRATEGY'][0]['phase'] = '02_CREATIVE_DIRECTION'
                state_path.write_text(json.dumps(state))
                tasks = [run(runtime, 'assign-task', '--project-dir', project, '--cycle', cycle['cycle_id'], '--role', role, '--actor-type', 'ROLE_SIMULATION', '--actor-id', role, '--problem', 'revelação visual', '--may-propose', 'referências', '--prohibited-changes', 'inventar observação', '--deliverable', 'parecer', '--acceptance-test', 'fontes') for role in ('CREATIVE_DIRECTOR', 'SCREENWRITER')]
                report = project / 'departments/report.md'
                report.parent.mkdir(exist_ok=True)
                report.write_text('Fixture de parecer para teste de devolução antecipada; não comprova filme nem execução criativa. ' * 3)
                def submission(task):
                    return [sys.executable, str(runtime), 'submit-task', '--project-dir', str(project), '--task', task['task_id'], '--file', str(report), '--dissent-or-risk', 'fixture', '--runtime-path', task['runtime_path'], '--runtime-version', task['runtime_version'], '--runtime-sha256', task['runtime_sha256']]
                subprocess.run(submission(tasks[0]), check=True, capture_output=True, text=True)
                def review(value):
                    return subprocess.run([sys.executable, str(runtime), 'director-review', '--project-dir', str(project), '--cycle', cycle['cycle_id'], '--actor-id', 'director', '--verdict', value, '--reason', 'Erro comprovado exige revisão.', '--integration-target', 'fixture'], capture_output=True, text=True)
                self.assertNotEqual(review('ACCEPT').returncode, 0)
                result = review(verdict)
                self.assertEqual(result.returncode, 0, result.stderr)
                current = json.loads(state_path.read_text())['workflow_registry']['01_BRIEF_STRATEGY'][0]
                self.assertEqual(current['tasks'][0]['status'], 'SUBMITTED')
                self.assertEqual(current['tasks'][1]['status'], 'CANCELLED_BY_DIRECTOR')
                self.assertNotEqual(subprocess.run(submission(tasks[1]), capture_output=True).returncode, 0)
                successor = run(runtime, 'open-cycle', '--project-dir', project, '--phase', '01_BRIEF_STRATEGY', '--parent-cycle', cycle['cycle_id'], '--question', 'corrigir erro', '--must-preserve', 'fixture')
                self.assertEqual(successor['parent_cycle_id'], cycle['cycle_id'])

    def test_sources_resolve_and_snapshot_is_unchanged(self):
        self.assertTrue(verify_bundle()['ok'])

    def test_editor_gets_relevant_creative_mechanism_without_watching_claim(self):
        p = build_packet('EDITOR', 'montagem arquivo continuidade gesto uniao')
        self.assertEqual(p['contracts'][0]['contract_id'], 'post.editing')
        self.assertIn('nike-editing-becomes-production-rule', [x['id'] for x in p['creative_reference_candidates'][:3]])
        self.assertEqual(p['evidence_limits']['watched_integrally'], 0)
        self.assertEqual(p['retrieval']['status'], 'ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH')
        self.assertTrue(all(x['exists'] for x in p['source_files']))

    def test_unrelated_question_stays_a_gap(self):
        p = build_packet('DP', 'zygomorphicquasar')
        self.assertEqual(p['retrieval']['status'], 'RESEARCH_GAP')
        self.assertEqual(p['creative_reference_candidates'], [])
        self.assertEqual(p['reading_leads'], [])

    def test_every_runtime_role_resolves_its_department(self):
        for role in ROLE_MAP:
            p = build_packet(role, 'revelação visual e função da câmera')
            self.assertTrue(p['contracts'], role)
            self.assertTrue(all(x['exists'] for x in p['source_files']), role)

    def test_missing_evidence_is_detected_in_portable_copy(self):
        with tempfile.TemporaryDirectory() as td:
            copy = Path(td) / 'portable-skill'
            shutil.copytree(SKILL_ROOT, copy, ignore=shutil.ignore_patterns('__pycache__'))
            script = copy / 'scripts/prepare_repertoire.py'
            result = subprocess.run([sys.executable, str(script), '--check'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            broken = copy / 'references/repertoire/research/sources/2023_MUSE_MEJI_ALABI_BLACK_SHINES_BRIGHTEST_PROCESS.md'
            broken.unlink()
            result = subprocess.run([sys.executable, str(script), '--check'], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(len(json.loads(result.stdout)['broken_evidence']), 3)

    def test_actual_assignment_includes_and_hashes_repertoire(self):
        runtime = SKILL_ROOT / 'scripts/project_runtime.py'
        with tempfile.TemporaryDirectory() as td:
            project = Path(td) / 'film'
            run(runtime, 'init', '--project', 'Teste repertório', '--client', 'Fictício', '--output', td, '--directory-name', 'film')
            cycle = run(runtime, 'open-cycle', '--project-dir', project, '--phase', '01_BRIEF_STRATEGY', '--question', 'Revelar um benefício por montagem de arquivo', '--must-preserve', 'brief fictício')
            task = run(runtime, 'assign-task', '--project-dir', project, '--cycle', cycle['cycle_id'], '--role', 'RESEARCHER', '--actor-type', 'ROLE_SIMULATION', '--actor-id', 'test-researcher', '--problem', 'montagem arquivo continuidade gesto uniao', '--may-propose', 'referências', '--prohibited-changes', 'inventar observação', '--deliverable', 'parecer', '--acceptance-test', 'fontes pertinentes')
            packet = project / task['repertoire_path']
            self.assertTrue(packet.is_file())
            self.assertEqual(hashlib.sha256(packet.read_bytes()).hexdigest(), task['repertoire_sha256'])
            self.assertIn(task['repertoire_path'], (project / task['brief_path']).read_text())
            state = json.loads((project / '00_PROJECT_STATE.json').read_text())
            active = state['workflow_registry']['01_BRIEF_STRATEGY'][0]
            self.assertIn(task['repertoire_path'], [x['path'] for x in active['input_artifacts']])
            payload = json.loads(packet.read_text())
            source_rel = payload['source_files'][0]['project_relative_path']
            source_copy = project / source_rel
            self.assertEqual(hashlib.sha256(source_copy.read_bytes()).hexdigest(), payload['source_files'][0]['sha256'])
            source_copy.write_text(source_copy.read_text() + '\nChanged after dispatch.\n')
            self.assertIn(source_rel, changed_cycle_inputs(project, active))


if __name__ == '__main__':
    unittest.main()
