from __future__ import annotations

import json
from pathlib import Path
import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_assurance import validate_assurance_selection

ROOT = Path(__file__).resolve().parents[2]
PROFILE = json.loads((ROOT / "gsl" / "EVOLUTION_AAP_PROFILE.json").read_text())
SOURCE_ROOT = PROFILE["canonical_source_root_sha256"]


def receipt(**impact_overrides):
    impact = {
        "consequence": "MEDIUM",
        "irreversibility": "LOW",
        "authority": "LOW",
        "novelty": "MEDIUM",
        "uncertainty": "MEDIUM",
        "sensitivity": "LOW",
        "dependency_impact": "MEDIUM",
        "disagreement": "LOW",
        "hard_policy": False,
        "constitutional": False,
        "physical_safety": False,
    }
    impact.update(impact_overrides)
    return {
        "schema": "GardenEvolutionAAPSelectionReceipt/v1",
        "action_id": "ACTION-1",
        "design_epoch": "v15.5",
        "canonical_source_root_sha256": SOURCE_ROOT,
        "source_obligation_refs": ["work_packages/WP-009.md#WP-009F"],
        "impact": impact,
        "selected": {
            "reason_tier": "R2",
            "verity_tier": "V2",
            "safety_tier": "S1",
            "modules": PROFILE["baseline_modules"],
        },
        "resource_budget": {"status": "SUFFICIENT"},
        "degradation_disposition": "NONE",
        "authorization_effect": "NONE",
        "semantic_compliance_proved": False,
    }


class AssuranceSelectionTests(unittest.TestCase):
    def validate(self, payload):
        return validate_assurance_selection(
            payload,
            PROFILE,
            expected_action_id="ACTION-1",
            expected_design_epoch="v15.5",
            expected_source_root_sha256=SOURCE_ROOT,
        )

    def test_medium_profile_derives_smallest_bounded_floor(self):
        result = self.validate(receipt())
        self.assertEqual(result["derived_minimum"]["reason_tier"], "R2")
        self.assertEqual(result["derived_minimum"]["verity_tier"], "V2")
        self.assertEqual(result["derived_minimum"]["safety_tier"], "S1")
        self.assertEqual(result["authorization_result"], "NOT_EVALUATED_HERE")

    def test_cannot_understate_derived_tier(self):
        payload = receipt(consequence="HIGH")
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_hard_policy_forces_critical_floor_and_policy_check(self):
        payload = receipt(hard_policy=True)
        payload["selected"].update({"reason_tier": "R4", "verity_tier": "V4", "safety_tier": "S3"})
        payload["selected"]["modules"] = PROFILE["baseline_modules"] + ["POLICY_CHECK"]
        result = self.validate(payload)
        self.assertIn("HARD_POLICY", result["derived_minimum"]["escalators"])

    def test_physical_safety_forces_s4(self):
        payload = receipt(physical_safety=True)
        payload["selected"].update({"reason_tier": "R2", "verity_tier": "V2", "safety_tier": "S4"})
        payload["selected"]["modules"] = PROFILE["baseline_modules"] + ["PHYSICAL_SAFETY_ASSURANCE"]
        result = self.validate(payload)
        self.assertEqual(result["derived_minimum"]["safety_tier"], "S4")

    def test_resource_pressure_cannot_silently_lower_floor(self):
        payload = receipt()
        payload["resource_budget"] = {"status": "INSUFFICIENT"}
        with self.assertRaises(SemanticError):
            self.validate(payload)
        payload["degradation_disposition"] = "REDUCE_AUTHORITY"
        result = self.validate(payload)
        self.assertEqual(result["resource_budget_status"], "INSUFFICIENT")

    def test_missing_required_module_rejected(self):
        payload = receipt()
        payload["selected"]["modules"] = ["AAP"]
        with self.assertRaises(SemanticError):
            self.validate(payload)

    def test_trust_and_authorization_cannot_be_minted(self):
        for field in ("human_signoff", "independent_review", "gate_decision", "authorization"):
            payload = receipt()
            payload[field] = True
            with self.subTest(field=field), self.assertRaises(SemanticError):
                self.validate(payload)

    def test_stale_binding_rejected(self):
        payload = receipt()
        payload["design_epoch"] = "v15.4"
        with self.assertRaises(SemanticError):
            self.validate(payload)


if __name__ == "__main__":
    unittest.main()
