#!/usr/bin/env python3
"""Bridge integration tests use a controlled executable; they do not call an AI."""
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dashboard_bridge import JobManager, _process_identity


STUB = r'''
import json, pathlib, sys, time
args = sys.argv[1:]
if args == ['login', 'status']:
    print('Logged in using fixture')
    raise SystemExit(0)
root = pathlib.Path(args[args.index('-C') + 1])
output = pathlib.Path(args[args.index('--output-last-message') + 1])
prompt = sys.stdin.read()
(root / 'observed-args.json').write_text(json.dumps(args))
(root / 'observed-prompt.txt').write_text(prompt)
def emit(event):
    print(json.dumps(event), flush=True)
emit({'type': 'thread.started', 'thread_id': 'fixture-thread'})
emit({'type': 'item.started', 'item': {'type': 'command_execution', 'command': 'PRIVATE_COMMAND token=do-not-expose'}})
print('PRIVATE_STDERR api_key=do-not-expose', file=sys.stderr, flush=True)
if 'STUB_SLOW' in prompt:
    emit({'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'Estudando os materiais.'}})
    time.sleep(20)
if 'STUB_EXIT_ERROR' in prompt:
    emit({'type': 'turn.failed', 'error': {'message': 'PRIVATE_FAILURE token=do-not-expose'}})
    raise SystemExit(2)
if 'STUB_EMPTY' in prompt:
    raise SystemExit(0)
response = 'Resposta real do executável de teste; não representa uma fase aprovada.'
if 'STUB_SECRET' in prompt:
    response += ' api_key=abc123 sk-testabcdefghijklmnop1234567890'
emit({'type': 'item.completed', 'item': {'type': 'agent_message', 'text': response}})
output.write_text(response)
emit({'type': 'turn.completed', 'usage': {'input_tokens': 8, 'output_tokens': 9}})
'''


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.skill = self.root / 'skill'
        self.skill.mkdir()
        (self.skill / 'SKILL.md').write_text('Fixture de skill para testar transporte, não direção criativa.')
        self.project = self.root / 'project'
        self.project.mkdir()
        self.state = {'current_phase': '01_BRIEF_STRATEGY', 'phases': {'01_BRIEF_STRATEGY': {'status': 'DRAFT'}}}
        (self.project / '00_PROJECT_STATE.json').write_text(json.dumps(self.state))
        self.binary = self.root / 'codex-fixture'
        self.binary.write_text('#!' + sys.executable + '\n' + STUB)
        self.binary.chmod(0o700)
        self.managers = []
        self.manager = self.make_manager()

    def make_manager(self, **kwargs):
        manager = JobManager(self.skill, codex_binary=self.binary, **kwargs)
        self.managers.append(manager)
        return manager

    def tearDown(self):
        for manager in self.managers:
            manager.shutdown()
        self.temp.cleanup()

    def wait_finished(self, manager=None, timeout=8):
        manager = manager or self.manager
        end = time.monotonic() + timeout
        while time.monotonic() < end:
            jobs = manager.get_jobs(self.project)
            if jobs and jobs[-1]['status'] not in {'queued', 'running', 'cancelling'}:
                return jobs[-1]
            time.sleep(0.03)
        self.fail('Job did not finish')

    def test_real_process_events_prompt_and_read_only_question(self):
        original = (self.project / '00_PROJECT_STATE.json').read_bytes()
        job = self.manager.start(self.project, 'Qual é a etapa atual?', 'question')
        finished = self.wait_finished()
        self.assertEqual(finished['id'], job['id'])
        self.assertEqual(finished['status'], 'completed')
        self.assertEqual(finished['thread_id'], 'fixture-thread')
        self.assertIn('Resposta real', finished['response'])
        args = json.loads((self.project / 'observed-args.json').read_text())
        self.assertEqual(args[args.index('--sandbox') + 1], 'read-only')
        self.assertEqual(args[-1], '-')
        self.assertNotIn('Qual é a etapa atual?', args)
        self.assertNotIn('--dangerously-bypass-approvals-and-sandbox', args)
        self.assertNotIn('--model', args)
        prompt = (self.project / 'observed-prompt.txt').read_text()
        self.assertIn(str(self.skill / 'SKILL.md'), prompt)
        self.assertIn('Não crie, altere, aprove ou avance', prompt)
        self.assertEqual((self.project / '00_PROJECT_STATE.json').read_bytes(), original)
        chat = self.manager.chat(self.project)
        self.assertEqual([item['role'] for item in chat], ['user', 'assistant'])
        self.assertFalse(list((self.project / '.dashboard').glob('last-*.txt')))

    def test_phase_scope_project_scope_and_conversation_are_explicit(self):
        self.manager.start(self.project, 'Desenvolva esta etapa.', 'phase')
        self.wait_finished()
        prompt = (self.project / 'observed-prompt.txt').read_text()
        args = json.loads((self.project / 'observed-args.json').read_text())
        self.assertEqual(args[args.index('--sandbox') + 1], 'workspace-write')
        self.assertIn('somente a fase atual 01_BRIEF_STRATEGY', prompt)
        self.assertIn('Pare antes de desenvolver a próxima fase', prompt)
        self.assertIn('especialistas temporários reais', prompt)
        self.manager.start(self.project, 'Agora desenvolva toda a jornada.', 'project')
        self.wait_finished()
        prompt = (self.project / 'observed-prompt.txt').read_text()
        self.assertIn('MODO JORNADA COMPLETA', prompt)
        self.assertIn('Desenvolva esta etapa.', prompt)

    def test_error_and_success_without_response_do_not_claim_delivery(self):
        self.manager.start(self.project, 'STUB_EXIT_ERROR', 'question')
        job = self.wait_finished()
        self.assertEqual(job['status'], 'failed')
        self.assertEqual(job['exit_code'], 2)
        self.assertNotIn('PRIVATE_FAILURE', json.dumps(job))
        # Separate project avoids a historic test marker affecting the next stub.
        second = self.root / 'empty'
        second.mkdir()
        (second / '00_PROJECT_STATE.json').write_text(json.dumps(self.state))
        old_project, self.project = self.project, second
        try:
            self.manager.start(second, 'STUB_EMPTY', 'question')
            job = self.wait_finished()
            self.assertEqual(job['status'], 'failed')
            self.assertEqual(job['exit_code'], 0)
            self.assertIn('sem resposta', job['error'])
        finally:
            self.project = old_project

    def test_commands_stderr_and_credentials_are_not_exposed(self):
        self.manager.start(self.project, 'STUB_SECRET', 'question')
        self.wait_finished()
        stored = ''.join(path.read_text() for path in (self.project / '.dashboard').rglob('*.json'))
        self.assertNotIn('PRIVATE_COMMAND', stored)
        self.assertNotIn('PRIVATE_STDERR', stored)
        self.assertNotIn('abc123', stored)
        self.assertNotIn('sk-test', stored)
        self.assertIn('[omitido]', stored)

    def test_concurrency_across_managers_cancel_and_no_automatic_restart(self):
        other = self.make_manager()
        def start(manager):
            try:
                return manager.start(self.project, 'STUB_SLOW', 'phase')
            except RuntimeError:
                return None
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(start, [self.manager, other]))
        self.assertEqual(sum(result is not None for result in results), 1)
        owner = self.manager if results[0] else other
        observer = other if results[0] else self.manager
        self.assertTrue(observer.status(self.project)['busy'])
        job_id = next(result['id'] for result in results if result)
        cancel = owner.cancel(self.project, job_id)
        self.assertTrue(cancel['cancelled'])
        job = self.wait_finished(owner)
        self.assertEqual(job['status'], 'cancelled')
        time.sleep(0.15)
        self.assertEqual(len(owner.get_jobs(self.project)), 1)
        self.assertFalse(owner.status(self.project)['busy'])

    def test_timeout_preserves_project_and_ends_process(self):
        manager = self.make_manager(timeout_seconds=0.25)
        manager.start(self.project, 'STUB_SLOW', 'phase')
        job = self.wait_finished(manager)
        self.assertEqual(job['status'], 'timed_out')
        self.assertIn('limite de tempo', job['error'])
        self.assertTrue((self.project / '00_PROJECT_STATE.json').is_file())

    def test_restart_marks_orphan_interrupted_without_fake_response(self):
        self.manager.status(self.project)
        orphan_id = 'a' * 32
        path = self.project / '.dashboard/jobs' / (orphan_id + '.json')
        path.write_text(json.dumps({'id': orphan_id, 'status': 'running', 'created_at': '2026-01-01', 'response': ''}))
        fresh = self.make_manager()
        result = fresh.status(self.project)
        self.assertFalse(result['busy'])
        self.assertEqual(result['last_job']['status'], 'interrupted')
        self.assertEqual(result['last_job']['response'], '')
        self.assertFalse((self.project / 'observed-args.json').exists())
        self.assertEqual(len(fresh.chat(self.project)), 1)
        fresh.status(self.project)
        self.assertEqual(len(fresh.chat(self.project)), 1)

    def test_missing_cli_and_login_failure_give_configuration_instructions(self):
        missing = JobManager(self.skill, codex_binary=self.root / 'missing')
        self.managers.append(missing)
        self.assertFalse(missing.capability()['available'])
        with self.assertRaisesRegex(RuntimeError, 'Instale'):
            missing.start(self.project, 'Oi', 'question')
        self.binary.write_text('#!' + sys.executable + '\nimport sys\nprint("private account info")\nsys.exit(1)\n')
        cap = self.manager.capability(refresh=True)
        self.assertTrue(cap['available'])
        self.assertFalse(cap['authenticated'])
        self.assertNotIn('private', cap['message'])
        with self.assertRaisesRegex(RuntimeError, 'login'):
            self.manager.start(self.project, 'Oi', 'question')

    @unittest.skipIf(os.name == 'nt', 'POSIX orphan process-group fixture')
    def test_live_orphan_blocks_new_run_and_can_be_cancelled_after_restart(self):
        self.manager.status(self.project)
        child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(20)'], start_new_session=True)
        try:
            orphan_id = 'b' * 32
            path = self.project / '.dashboard/jobs' / (orphan_id + '.json')
            path.write_text(json.dumps({'id': orphan_id, 'status': 'running', 'created_at': '2026-01-01',
                                        'process_pid': child.pid, 'process_identity': _process_identity(child.pid)}))
            fresh = self.make_manager()
            status = fresh.status(self.project)
            self.assertTrue(status['busy'])
            self.assertEqual(status['active_job']['status'], 'interrupted')
            with self.assertRaisesRegex(RuntimeError, 'servidor anterior'):
                fresh.start(self.project, 'Continue', 'phase')
            self.assertTrue(fresh.cancel(self.project, orphan_id)['cancelled'])
            child.wait(timeout=5)
            self.assertFalse(fresh.status(self.project)['busy'])
        finally:
            if child.poll() is None:
                child.kill()
                child.wait(timeout=5)

    def test_pid_reuse_does_not_block_or_cancel_an_unrelated_process(self):
        self.manager.status(self.project)
        orphan_id = 'c' * 32
        path = self.project / '.dashboard/jobs' / (orphan_id + '.json')
        path.write_text(json.dumps({'id': orphan_id, 'status': 'running', 'created_at': '2026-01-01',
                                    'process_pid': os.getpid(), 'process_identity': 'different creation time'}))
        status = self.manager.status(self.project)
        self.assertFalse(status['busy'])
        self.assertFalse(self.manager.cancel(self.project)['cancelled'])

    def test_validation_and_symlink_storage(self):
        for message, mode in [('', 'phase'), ('x' * 12001, 'phase'), ('x', 'invalid')]:
            with self.assertRaises(ValueError):
                self.manager.start(self.project, message, mode)
        if os.name != 'nt':
            (self.project / '.dashboard').symlink_to(self.root / 'outside')
            with self.assertRaisesRegex(ValueError, 'link simbólico'):
                self.manager.status(self.project)


if __name__ == '__main__':
    unittest.main()
