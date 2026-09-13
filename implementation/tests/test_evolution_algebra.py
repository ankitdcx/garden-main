from __future__ import annotations

import copy
import json
from pathlib import Path
import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_algebra import validate_algebra_usage


ROOT = Path(__file__).resolve().parents[2]
PROFILE = json.loads((ROOT / "gsl" / "EVOLUTION_ALGEBRA_PROFILE.json").read_text(encoding="utf-8"))
ACTION = "GARDEN-HOURLY-2026-09-13-WP009E-PROPOSE-001"
EPOCH = "v15.5"
ROOT_SHA = "63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598"


def valid_payload() -> dict:
    return {
        "schema": "GardenEvolutionAlgebraUsageReceipt/v1",
        "action_id": ACTION,
        "design_epoch": EPOCH,
        "canonical_source_root_sha256": ROOT_SHA,
        "source_obligation_refs": [
            "work_packages/WP-009.md#WP-009E",
            "canonical/current/Garden_System_v15.5_FULL_2026-09-12.txt:REG-ALGEBRA-001",
        ],
        "entries": [
            {
                "algebra": "Process",
                "status": "APPLIED",
                "operators": ["SEQUENCE", "DO_NOTHING"],
                "law_claims": [],
                "non_law_acknowledgements": ["PARALLEL_EFFECT_COMMUTATIVITY_NOT_UNIVERSAL"],
                "applicability_reason": "The governed evolution path sequences typed action, validation, gate, receipt and effect while Compare carries explicit DO_NOTHING.",
            },
            {
                "algebra": "Policy",
                "status": "FRONTIER",
                "operators": [],
                "law_claims": [],
                "non_law_acknowledgements": [],
                "applicability_reason": "Policy semantics constrain admission, but the current ActionGate is not silently equated with Engine.Policy.",
                "frontier_reason": "No executable Policy Algebra operator binding is yet demonstrated in the evolution kernel.",
            },
            {
                "algebra": "Decision",
                "status": "FRONTIER",
                "operators": [],
                "law_claims": [],
                "non_law_acknowledgements": [],
                "applicability_reason": "Gate and verifier outcomes are typed decisions/results.",
                "frontier_reason": "Exact Decision Algebra executable operator signatures remain outside this bounded profile.",
            },
            {
                "algebra": "Conformance",
                "status": "APPLIED",
                "operators": ["BIND_EVIDENCE", "BIND_PROOF", "GAP", "COVERAGE"],
                "law_claims": [],
                "non_law_acknowledgements": ["CONFORMANCE_IS_NOT_BINARY_ONLY", "AUDIT_IS_NOT_A_SEPARATE_ALGEBRA"],
                "applicability_reason": "WP-009 reasoning and coverage audits explicitly bind evidence/proof and preserve gap/coverage state.",
            },
            {
                "algebra": "Evidence",
                "status": "FRONTIER",
                "operators": [],
                "law_claims": [],
                "non_law_acknowledgements": [],
                "applicability_reason": "Evidence receipts are present, but no dependence-aware composition operator is executed by this path yet.",
                "frontier_reason": "Level-3 executable Evidence Algebra signatures are not yet bound in the private evolution kernel.",
            },
            {
                "algebra": "Bridge",
                "status": "NOT_APPLICABLE",
                "operators": [],
                "law_claims": [],
                "non_law_acknowledgements": [],
                "applicability_reason": "This change uses typed JSON/Python transport only and invokes no semantic-to-operator representation transformation.",
            },
        ],
        "semantic_compliance_proved": False,
    }


class EvolutionAlgebraTests(unittest.TestCase):
    def validate(self, payload: dict) -> dict:
        return validate_algebra_usage(
            payload,
            PROFILE,
            expected_action_id=ACTION,
            expected_design_epoch=EPOCH,
            expected_source_root_sha256=ROOT_SHA,
        )

    def test_valid_bounded_profile_preserves_frontier(self):
        receipt = self.validate(valid_payload())
        self.assertEqual(receipt["applied"], ["Process", "Conformance"])
        self.assertEqual(receipt["frontier"], ["Policy", "Decision", "Evidence"])
        self.assertEqual(receipt["not_applicable"], ["Bridge"])
        self.assertEqual(receipt["required_frontier_count"], 3)
        self.assertFalse(receipt["semantic_compliance_proved"])
        self.assertEqual(receipt["authorization_result"], "NOT_EVALUATED_HERE")

    def test_undeclared_law_is_rejected(self):
        payload = valid_payload()
        payload["entries"][0]["law_claims"] = ["COMMUTATIVE"]
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_unregistered_operator_is_rejected(self):
        payload = valid_payload()
        payload["entries"][3]["operators"].append("MAGIC_UNION")
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_required_algebra_cannot_be_not_applicable(self):
        payload = valid_payload()
        policy = payload["entries"][1]
        policy["status"] = "NOT_APPLICABLE"
        policy.pop("frontier_reason")
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_level3_frontier_cannot_claim_applied(self):
        payload = valid_payload()
        decision = payload["entries"][2]
        decision["status"] = "APPLIED"
        decision["operators"] = []
        decision.pop("frontier_reason")
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_applied_algebra_must_acknowledge_non_laws(self):
        payload = valid_payload()
        payload["entries"][0]["non_law_acknowledgements"] = []
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_receipt_cannot_mint_authority(self):
        payload = valid_payload()
        payload["authority"] = {"role": "INTEGRATOR"}
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_stale_epoch_is_rejected(self):
        payload = valid_payload()
        payload["design_epoch"] = "v15.4"
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_profile_cannot_claim_semantic_compliance(self):
        profile = copy.deepcopy(PROFILE)
        profile["semantic_compliance_proved"] = True
        with self.assertRaises(SemanticError):
            validate_algebra_usage(valid_payload(), profile)


if __name__ == "__main__":
    unittest.main()
