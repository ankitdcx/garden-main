import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DeltaLedgerTest(unittest.TestCase):
    def test_validator_passes(self):
        proc = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate_delta_ledger.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        result = json.loads(proc.stdout)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["record_count"], result["unique_delta_ids"])
        self.assertGreater(result["record_count"], 0)

    def test_no_record_claims_canonical_effect(self):
        ledger = json.loads((ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json").read_text(encoding="utf-8"))
        self.assertTrue(all(record["canonical_effect"] is False for record in ledger["records"]))

    def test_no_admitted_record_without_challenger_and_quorum(self):
        ledger = json.loads((ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json").read_text(encoding="utf-8"))
        for record in ledger["records"]:
            if record["lifecycle_state"] == "ADMITTED_FOR_SUCCESSOR":
                self.assertEqual(record["review"]["quorum_status"], "SATISFIED")
                self.assertEqual(record["challenger"]["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
