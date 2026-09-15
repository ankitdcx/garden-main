from __future__ import annotations

import copy
import json
from pathlib import Path
import unittest

from garden_kernel.algebra_bound_update import validate_algebra_bound_update
from garden_kernel.core import SemanticError
from garden_kernel.evolution_algebra import validate_algebra_usage


ROOT = Path(__file__).resolve().parents[2]
PROFILE_REF = "gsl/EVOLUTION_ALGEBRA_PROFILE.json"
PROFILE_BLOB_SHA = "ef1775f9890a4066969ca576cb25e40a9b217102"
PROFILE = json.loads((ROOT / PROFILE_REF).read_text(encoding="utf-8"))
EPOCH = "v15.5"
SOURCE_ROOT = "63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598"
ACTION = "TEST-ALGEBRA-BOUND-UPDATE-001"
REPO = "ankitdcx/garden-main"
REPO_SHA = "aab395031871c35611188d0b95d6aab61555d618"
PROCESS_VERSION = "GardenCanonicalUpdateProcess@1.3-candidate"


def usage() -> dict:
    return {
        "schema": "GardenEvolutionAlgebraUsageReceipt/v1",
        "action_id": ACTION,
        "design_epoch": EPOCH,
        "canonical_source_root_sha256": SOURCE_ROOT,
        "source_obligation_refs": ["issues/41", "canonical/current/Garden_System_v15.5_FULL_2026-09-12.txt:REG-ALGEBRA-001"],
        "entries": [
            {
                "algebra": "Process",
                "status": "APPLIED",
                "operators": ["SEQUENCE", "DO_NOTHING"],
                "law_claims": [],
                "non_law_acknowledgements": ["PARALLEL_EFFECT_COMMUTATIVITY_NOT_UNIVERSAL"],
                "applicability_reason": "The bounded update sequence preserves an explicit DO_NOTHING alternative.",
            },
            {
                "algebra": "Policy",
                "status": "FRONTIER",
                "operators": [],
                "law_claims": [],
                "non_law_acknowledgements": [],
                "applicability_reason": "Protected authority applies but no executable Policy Algebra operator is claimed.",
                "frontier_reason": "ActionGate policy is not silently relabeled as Policy Algebra.",
            },
            {
                "algebra": "Decision",
                "status": "FRONTIER",
                "operators": [],
                "law_claims": [],
                "non_law_acknowledgements": [],
                "applicability_reason": "Typed decisions exist but Level-3 executable operators remain unbound.",
                "frontier_reason": "Decision executable signatures remain frontiered.",
            },
            {
                "algebra": "Conformance",
                "status": "APPLIED",
                "operators": ["BIND_EVIDENCE", "COVERAGE"],
                "law_claims": [],
                "non_law_acknowledgements": ["CONFORMANCE_IS_NOT_BINARY_ONLY", "AUDIT_IS_NOT_A_SEPARATE_ALGEBRA"],
                "applicability_reason": "The update binds exact evidence and preserves explicit coverage state.",
            },
            {
                "algebra": "Evidence",
                "status": "FRONTIER",
                "operators": [],
                "law_claims": [],
                "non_law_acknowledgements": [],
                "applicability_reason": "Evidence is present but no executable Evidence Algebra composition operator is claimed.",
                "frontier_reason": "Evidence executable signatures remain frontiered.",
            },
            {
                "algebra": "Bridge",
                "status": "NOT_APPLICABLE",
                "operators": [],
                "law_claims": [],
                "non_law_acknowledgements": [],
                "applicability_reason": "No semantic-representation bridge is invoked.",
            },
        ],
        "semantic_compliance_proved": False,
    }


def usage_validation() -> dict:
    return validate_algebra_usage(
        usage(),
        PROFILE,
        expected_action_id=ACTION,
        expected_design_epoch=EPOCH,
        expected_source_root_sha256=SOURCE_ROOT,
    )


def bound() -> dict:
    return {
        "schema": "AlgebraBoundUpdateReceipt/v1",
        "action_id": ACTION,
        "cycle_id": "TEST-CYCLE-001",
        "process_version": PROCESS_VERSION,
        "design_epoch": EPOCH,
        "canonical_source_root_sha256": SOURCE_ROOT,
        "target_kind": "CANONICAL_DESIGN",
        "repo": REPO,
        "repo_sha": REPO_SHA,
        "registry_ref": "REG-ALGEBRA-001",
        "algebra_profile_ref": PROFILE_REF,
        "algebra_profile_blob_sha": PROFILE_BLOB_SHA,
        "process_operator_trace": ["SEQUENCE", "DO_NOTHING"],
        "process_non_law_acknowledgements": ["PARALLEL_EFFECT_COMMUTATIVITY_NOT_UNIVERSAL"],
        "algebra_usage_receipt_ref": "reviews/evolution/algebra/test-usage.json",
        "algebra_validation_receipt_ref": "reviews/evolution/algebra/test-validation.json",
        "conformance_refs": ["issues/41", f"repo:{REPO}@{REPO_SHA}"],
        "policy_gate_refs": [],
        "remaining_algebra_frontiers": ["Policy", "Decision", "Evidence"],
        "semantic_compliance_proved": False,
        "result": "APPLIED",
    }


class AlgebraBoundUpdateTests(unittest.TestCase):
    def validate(self, payload: dict, *, usage_payload: dict | None = None, stored_validation: dict | None = None) -> dict:
        return validate_algebra_bound_update(
            payload,
            usage_payload or usage(),
            stored_validation or usage_validation(),
            PROFILE,
            expected_repo=REPO,
            expected_repo_sha=REPO_SHA,
            expected_target_kind="CANONICAL_DESIGN",
            expected_process_version=PROCESS_VERSION,
            expected_design_epoch=EPOCH,
            expected_source_root_sha256=SOURCE_ROOT,
            expected_profile_ref=PROFILE_REF,
            expected_profile_blob_sha=PROFILE_BLOB_SHA,
        )

    def test_valid_bound_update_is_accepted_without_authority(self):
        receipt = self.validate(bound())
        self.assertEqual(receipt["repo_sha"], REPO_SHA)
        self.assertEqual(receipt["target_kind"], "CANONICAL_DESIGN")
        self.assertEqual(receipt["remaining_algebra_frontiers"], ["Policy", "Decision", "Evidence"])
        self.assertEqual(receipt["authorization_result"], "NOT_EVALUATED_HERE")
        self.assertFalse(receipt["semantic_compliance_proved"])

    def test_unregistered_process_operator_is_rejected(self):
        payload = bound()
        payload["process_operator_trace"].append("MAGIC_UNION")
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_missing_required_process_non_law_is_rejected(self):
        payload = bound()
        payload["process_non_law_acknowledgements"] = []
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_wrong_target_kind_is_rejected(self):
        payload = bound()
        payload["target_kind"] = "UNSCOPED_REPO"
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_stale_repo_sha_is_rejected(self):
        payload = bound()
        payload["repo_sha"] = "0" * 40
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_stale_design_epoch_is_rejected(self):
        payload = bound()
        payload["design_epoch"] = "v15.4"
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_stale_source_root_is_rejected(self):
        payload = bound()
        payload["canonical_source_root_sha256"] = "0" * 64
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_wrong_profile_blob_is_rejected(self):
        payload = bound()
        payload["algebra_profile_blob_sha"] = "0" * 40
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_semantic_compliance_claim_is_rejected_while_frontier_remains(self):
        payload = bound()
        payload["semantic_compliance_proved"] = True
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_receipt_cannot_mint_authority(self):
        payload = bound()
        payload["authority"] = "MERGE"
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_stored_usage_validation_mismatch_is_rejected(self):
        stored = copy.deepcopy(usage_validation())
        stored["frontier"] = ["Decision", "Evidence"]
        with self.assertRaises(SemanticError):
            self.validate(bound(), stored_validation=stored)

    def test_operator_trace_must_be_supported_by_usage_receipt(self):
        payload = bound()
        payload["process_operator_trace"] = ["SEQUENCE", "RETRY"]
        with self.assertRaises(SemanticError):
            self.validate(payload)


if __name__ == "__main__":
    unittest.main()
