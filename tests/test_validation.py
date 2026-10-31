"""Current integrity must not rebind historical assessment or budget inputs."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'persona'
        shutil.copytree(ROOT, self.root, symlinks=True,
                        ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def validate(self):
        return subprocess.run([sys.executable, '-B', str(self.root / 'scripts/validate.py')],
                              capture_output=True, text=True)

    def test_reviewed_runtime_passes_with_historical_notice(self):
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('current runtime recognition has not been rerun', result.stdout)

    def test_unreviewed_runtime_edit_fails(self):
        path = self.root / 'references/voice.md'
        path.write_text(path.read_text() + '\nUnexpected change.\n')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('runtime bytes changed', result.stderr)

    def test_historical_snapshot_corruption_fails(self):
        path = self.root / 'fidelity-ledger/history/pre-activation/SKILL.md.txt'
        path.write_text(path.read_text() + '\nCorrupted snapshot.\n')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('historical runtime snapshot changed', result.stderr)

    def test_historical_score_corruption_fails(self):
        path = self.root / 'fidelity-ledger/audit/projection-gate-results.json'
        data = json.loads(path.read_text())
        data['overall'] = -1
        path.write_text(json.dumps(data))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('projection arithmetic mismatch', result.stderr)

    def test_missing_current_record_fails(self):
        (self.root / 'fidelity-ledger/audit/current-runtime.json').unlink()
        self.assertNotEqual(self.validate().returncode, 0)

    def test_readme_edit_does_not_rebind_runtime_assessment(self):
        path = self.root / 'README.md'
        path.write_text(path.read_text() + '\nEditorial clarification.\n')
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
