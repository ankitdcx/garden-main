import json
import subprocess
import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.validate_delta_ledger import admission_readiness  # noqa: E402

BOUND_TEST_COMMIT = "0" * 40


class DeltaLedgerTest(unittest.TestCase):
    def test_validator_passes_and_emits_typed_receipt(self):
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "validate_delta_ledger.py"),
                "--repository-commit",
                BOUND_TEST_COMMIT,
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)
        result = json.loads(proc.stdout)
        self.assertEqual(result["schema"], "DeltaAdmissionReadinessReceipt/v1")
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["repository_commit"], BOUND_TEST_COMMIT)
        self.assertEqual(result["rule_trace"]["rule_id"], "RULE-DELTA-ADMISSION-FAIL-CLOSED")
        self.assertEqual(result["rule_trace"]["check_id"], "CHECK-DELTA-ADMISSION-READINESS")
        self.assertEqual(result["record_count"], result["unique_delta_ids"])
        self.assertGreater(result["record_count"], 0)

    def test_no_record_claims_canonical_effect(self):
        ledger = json.loads((ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json").read_text(encoding="utf-8"))
        self.assertTrue(all(record["canonical_effect"] is False for record in ledger["records"]))

    def test_legacy_candidate_marker_never_implies_readiness(self):
        ledger = json.loads((ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json").read_text(encoding="utf-8"))
        candidates = [record for record in ledger["records"] if record["admission_eligible"]]
        self.assertGreater(len(candidates), 0)
        for record in candidates:
            ready, reasons = admission_readiness(record)
            if record["semantic_impact"]["status"] == "NOT_ASSESSED" or record["review"]["quorum_status"] != "SATISFIED" or record["challenger"]["status"] != "PASS":
                self.assertFalse(ready, msg=f"{record['delta_id']} unexpectedly ready: {reasons}")

    def test_not_assessed_states_are_fail_closed(self):
        ledger = json.loads((ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json").read_text(encoding="utf-8"))
        record = deepcopy(ledger["records"][0])
        record["lifecycle_state"] = "ACCEPTED"
        record["semantic_impact"] = {"status": "NOT_ASSESSED", "assessment_ref": None}
        record["review"]["quorum_status"] = "NOT_ASSESSED"
        record["challenger"] = {"status": "NOT_ASSESSED", "decision_ref": None}
        ready, reasons = admission_readiness(record)
        self.assertFalse(ready)
        self.assertIn("SEMANTIC_IMPACT_UNRESOLVED", reasons)
        self.assertIn("INDEPENDENT_REVIEW_QUORUM_NOT_SATISFIED", reasons)
        self.assertIn("CHALLENGER_NOT_PASS", reasons)

    def test_complete_evidence_can_be_ready_without_canonical_effect(self):
        ledger = json.loads((ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json").read_text(encoding="utf-8"))
        record = deepcopy(ledger["records"][0])
        record["lifecycle_state"] = "ACCEPTED"
        record["semantic_impact"] = {"status": "YES", "assessment_ref": "receipt:semantic-impact:test"}
        record["review"]["quorum_status"] = "SATISFIED"
        record["review"]["reviewer_families"] = ["family-a", "family-b", "family-c"]
        record["review"]["blind_review_refs"] = ["blind:a", "blind:b", "blind:c"]
        record["review"]["cross_exam_refs"] = ["cross:a", "cross:b", "cross:c"]
        record["review"]["evidence_conflict_status"] = "NONE_KNOWN"
        record["challenger"] = {"status": "PASS", "decision_ref": "receipt:challenger:test"}
        record["canonical_effect"] = False
        ready, reasons = admission_readiness(record)
        self.assertTrue(ready, msg=reasons)

    def test_no_admitted_record_without_derived_readiness(self):
        ledger = json.loads((ROOT / "design_deltas" / "v15.6" / "DELTA_LEDGER.json").read_text(encoding="utf-8"))
        for record in ledger["records"]:
            if record["lifecycle_state"] == "ADMITTED_FOR_SUCCESSOR":
                ready, reasons = admission_readiness(record)
                self.assertTrue(ready, msg=f"{record['delta_id']}: {reasons}")


if __name__ == "__main__":
    unittest.main()
