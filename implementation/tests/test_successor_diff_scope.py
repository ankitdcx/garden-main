"""A matching diff must not manufacture semantic admission."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]

class SuccessorDiffScopeTests(unittest.TestCase):
    def test_self_declared_admission_cannot_turn_diff_match_into_approval(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            entries = []
            for role in ('User','System','Technical','Annexure','Theories'):
                old = root / (role + '-old.txt')
                new = root / (role + '-new.txt')
                old.write_text('unchanged\n')
                new.write_text('unchanged\n')
                entries.append(dict(predecessor=str(old), candidate=str(new),
                    expected_diff_sha256=hashlib.sha256(b'').hexdigest(), delta_ids=['FORGED-ADMISSION']))
            manifest = root / 'manifest.json'
            manifest.write_text(json.dumps(dict(schema='GardenSuccessorDeltaManifest/v1',
                admission_status='ADMITTED', files=entries)))
            command = [sys.executable, str(ROOT/'scripts/check_successor_drift.py'), str(manifest)]
            result = subprocess.run(command, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            receipt = json.loads(result.stdout)
            self.assertEqual(receipt['status'], 'DIFF_MATCH_ONLY')
            self.assertFalse(receipt['admitted_diff_verified'])
            self.assertFalse(receipt['canonical_promotion_authorized'])
            new.write_text('unreviewed change\n')
            result = subprocess.run(command, text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)['status'], 'FAIL')

if __name__ == '__main__':
    unittest.main()
