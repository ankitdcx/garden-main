from __future__ import annotations

import copy
import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_reasoning import validate_reasoning_bundle


ROOT = "63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598"
ACTION = "TEST-WP009D-001"


def valid_bundle() -> dict:
    identity = {
        "action_id": ACTION,
        "design_epoch": "v15.5",
        "canonical_source_root_sha256": ROOT,
    }
    return {
        "schema": "GardenEvolutionReasoningBundle/v1",
        **identity,
        "source_obligation_refs": [
            "work_packages/WP-009.md#WP-009D",
            "canonical/current/Garden_User_v15.5_FULL_2026-09-12.txt:SAFE_EVOLUTION_LOOP",
        ],
        "compare": {
            "schema": "GardenEvolutionCompareReceipt/v1",
            **identity,
            "predecessor_ref": "git:main",
            "alternatives": [
                {
                    "alternative_id": "DO_NOTHING",
                    "description": "Keep prose-only separation.",
                    "projected_effect": "No new machine enforcement.",
                    "risk": "Reasoning/proof/evidence can remain conflated.",
                },
                {
                    "alternative_id": "CANDIDATE",
                    "description": "Add typed separation validation.",
                    "projected_effect": "Machine-checkable separation.",
                    "risk": "Additional schema and CI complexity.",
                },
            ],
            "bidirectional_gaps": [
                {
                    "from": "DO_NOTHING",
                    "to": "CANDIDATE",
                    "gap": "Missing typed enforcement.",
                },
                {
                    "from": "CANDIDATE",
                    "to": "DO_NOTHING",
                    "gap": "Adds maintenance surface.",
                },
            ],
        },
        "reason": {
            "schema": "GardenEvolutionReasonReceipt/v1",
            **identity,
            "strategy": "BOUNDED_REFERENCE_IMPLEMENTATION",
            "tier": "REFERENCE",
            "assumptions": ["Garden v15.5 remains immutable."],
            "uncertainty": "This closes typed separation only, not full GSL conformance.",
            "counterexamples": [
                "Evidence attempting to claim authorization must fail."
            ],
            "dependency_refs": ["work_packages/WP-009.md#WP-009D"],
            "conclusion": "Implement and test as a bounded candidate.",
            "authorization_effect": "NONE",
        },
        "proof": {
            "schema": "GardenEvolutionProofReceipt/v1",
            **identity,
            "obligations": [
                {
                    "obligation_id": "PO-1",
                    "statement": "Typed separation validator rejects trust-field conflation.",
                    "verifier_class": "UNIT_TEST",
                    "result": "UNKNOWN",
                    "evidence_refs": [],
                }
            ],
            "overall_result": "UNKNOWN",
            "authorization_effect": "NONE",
        },
        "evidence": {
            "schema": "GardenEvolutionEvidenceReceipt/v1",
            **identity,
            "items": [
                {
                    "kind": "SOURCE_REFERENCE",
                    "ref": "work_packages/WP-009.md#WP-009D",
                    "claim_scope": "Defines required separation frontier.",
                }
            ],
            "proof_effect": "NONE",
            "authorization_effect": "NONE",
        },
        "separation_assertions": {
            "compare_is_not_decision": True,
            "reason_is_not_authorization": True,
            "evidence_is_not_proof": True,
            "proof_is_not_authorization": True,
            "actiongate_owns_authorization": True,
        },
    }


class EvolutionReasoningTests(unittest.TestCase):
    def test_valid_bundle_remains_non_authorizing(self) -> None:
        receipt = validate_reasoning_bundle(valid_bundle())
        self.assertEqual(receipt["proof"]["overall_result"], "UNKNOWN")
        self.assertEqual(receipt["authorization_result"], "NOT_EVALUATED_HERE")
        self.assertFalse(receipt["semantic_compliance_proved"])

    def test_compare_requires_do_nothing(self) -> None:
        bundle = valid_bundle()
        bundle["compare"]["alternatives"][0]["alternative_id"] = "BASELINE"
        bundle["compare"]["bidirectional_gaps"][0]["from"] = "BASELINE"
        bundle["compare"]["bidirectional_gaps"][1]["to"] = "BASELINE"
        with self.assertRaisesRegex(SemanticError, "DO_NOTHING"):
            validate_reasoning_bundle(bundle)

    def test_compare_requires_bidirectional_gaps(self) -> None:
        bundle = valid_bundle()
        bundle["compare"]["bidirectional_gaps"].pop()
        with self.assertRaisesRegex(SemanticError, "bidirectional"):
            validate_reasoning_bundle(bundle)

    def test_reason_cannot_claim_gate_decision(self) -> None:
        bundle = valid_bundle()
        bundle["reason"]["decision"] = "ALLOW"
        with self.assertRaisesRegex(SemanticError, "may not mint"):
            validate_reasoning_bundle(bundle)

    def test_evidence_cannot_claim_authority(self) -> None:
        bundle = valid_bundle()
        bundle["evidence"]["authority"] = "self"
        with self.assertRaisesRegex(SemanticError, "may not mint"):
            validate_reasoning_bundle(bundle)

    def test_proof_cannot_authorize(self) -> None:
        bundle = valid_bundle()
        bundle["proof"]["authorization_effect"] = "ALLOW"
        with self.assertRaisesRegex(SemanticError, "authorization_effect NONE"):
            validate_reasoning_bundle(bundle)

    def test_proof_result_is_derived(self) -> None:
        bundle = valid_bundle()
        bundle["proof"]["obligations"][0]["result"] = "PASS"
        bundle["proof"]["obligations"][0]["evidence_refs"] = ["ci:test:pass"]
        with self.assertRaisesRegex(SemanticError, "overall_result"):
            validate_reasoning_bundle(bundle)

        bundle["proof"]["overall_result"] = "PASS"
        receipt = validate_reasoning_bundle(bundle)
        self.assertEqual(receipt["proof"]["overall_result"], "PASS")
        self.assertEqual(receipt["authorization_result"], "NOT_EVALUATED_HERE")

    def test_epoch_and_source_root_are_bound(self) -> None:
        bundle = valid_bundle()
        stale_epoch = copy.deepcopy(bundle)
        stale_epoch["design_epoch"] = "v15.4"
        with self.assertRaisesRegex(SemanticError, "DesignEpoch"):
            validate_reasoning_bundle(stale_epoch, expected_design_epoch="v15.5")

        stale_root = copy.deepcopy(bundle)
        stale_root["canonical_source_root_sha256"] = "stale-root"
        with self.assertRaisesRegex(SemanticError, "canonical source root"):
            validate_reasoning_bundle(stale_root, expected_source_root_sha256=ROOT)


if __name__ == "__main__":
    unittest.main()
