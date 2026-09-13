from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from garden_kernel.core import SemanticError
from garden_kernel.evolution_transport import (
    CanonicalSourceIdentity,
    authority_registry_from_payload,
    evaluate_production_request,
    require_allowed,
)


ROOT = Path(__file__).resolve().parents[2]
IDENTITY = CanonicalSourceIdentity(
    release="Garden v15.5",
    design_epoch="v15.5",
    source_root_sha256="root-current",
    gsl="v45.1",
)
RESOURCE = "repo:ankitdcx/garden-main"


def registry_payload() -> dict:
    return {
        "schema": "GardenEvolutionAuthorityRegistry/v1",
        "design_epoch": "v15.5",
        "canonical_source_root_sha256": "root-current",
        "grants": [
            {
                "authority_id": "AUTH-REVIEWER",
                "subject": "agent:hourly",
                "role": "REVIEWER",
                "granted_by": "human:operator",
                "resources": [RESOURCE],
                "max_delegation_depth": 0,
            },
            {
                "authority_id": "AUTH-INTEGRATOR",
                "subject": "agent:hourly",
                "role": "INTEGRATOR",
                "granted_by": "human:operator",
                "resources": [RESOURCE],
                "max_delegation_depth": 0,
            },
            {
                "authority_id": "AUTH-ACCUMULATOR",
                "subject": "agent:hourly",
                "role": "ACCUMULATOR",
                "granted_by": "human:operator",
                "resources": [RESOURCE],
                "max_delegation_depth": 0,
            },
            {
                "authority_id": "AUTH-MATERIALIZER",
                "subject": "agent:hourly",
                "role": "MATERIALIZER",
                "granted_by": "human:operator",
                "resources": [RESOURCE],
                "max_delegation_depth": 0,
            },
        ],
    }


def trusted_authorities():
    return authority_registry_from_payload(registry_payload(), IDENTITY)


def base_request(*, verb: str, authority_ref: str) -> dict:
    action_shapes = {
        "PROPOSE": (
            ["ACTOR_IDENTIFIED", "SUBJECT_IDENTIFIED", "PROVENANCE_PRESENT", "INPUT_REFS_TYPED"],
            ["CANDIDATE_RECORDED", "NO_AUTHORITY_EXPANSION", "CANONICAL_POINTER_UNCHANGED"],
        ),
        "ACCUMULATE": (
            ["ACTOR_IDENTIFIED", "TRIAGE_DISPOSITION_EXISTS", "ADMISSION_EVIDENCE_EXISTS", "DEPENDENCIES_EXPLICIT", "PROVENANCE_PRESENT"],
            ["DELTA_ACCUMULATED", "NO_AUTHORITY_EXPANSION", "CANONICAL_POINTER_UNCHANGED"],
        ),
        "MATERIALIZE": (
            ["ACTOR_IDENTIFIED", "ACCUMULATED_DELTA_SET_EXISTS", "CONSISTENCY_CHECK_EXISTS", "PREDECESSOR_IDENTITY_PINNED", "SUCCESSOR_TARGET_DECLARED", "PROVENANCE_PRESENT"],
            ["SUCCESSOR_CANDIDATE_COMPLETE", "PREDECESSOR_UNCHANGED", "CANONICAL_POINTER_UNCHANGED", "NO_AUTHORITY_EXPANSION"],
        ),
    }
    pre, post = action_shapes[verb]
    return {
        "schema": "GardenEvolutionProductionAction/v1",
        "design_epoch": "v15.5",
        "dependencies": {"canonical_source_root": "root-current"},
        "action": {
            "action_id": f"A-{verb}",
            "verb": verb,
            "actor_ref": "agent:hourly",
            "subject_ref": RESOURCE,
            "input_refs": ["input:1"],
            "provenance_refs": ["work_packages/WP-007.md"],
            "satisfied_preconditions": pre,
            "claimed_postconditions": post,
        },
        "authority_ref": authority_ref,
        "bound_inputs": [],
        "governance_tier": "ORDINARY",
    }


class ProductionEvolutionTransportTests(unittest.TestCase):
    def test_valid_proposal_uses_trusted_registry_and_cannot_promote_canon(self):
        receipt = evaluate_production_request(
            base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER"),
            IDENTITY,
            trusted_authorities(),
        )
        self.assertEqual(receipt["decision"], "ALLOW")
        self.assertFalse(receipt["canonical_pointer_changed"])
        self.assertEqual(receipt["authority_ref"], "AUTH-REVIEWER")
        self.assertFalse(receipt["authority"]["can_mint_envelopes"])
        self.assertFalse(receipt["authority"]["can_promote_canon"])
        self.assertFalse(receipt["trusted_attestations"]["human_signoff"])
        require_allowed(receipt)

    def test_request_cannot_self_assert_authority(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        request["authority"] = {
            "subject": "agent:hourly",
            "role": "REVIEWER",
            "granted_by": "agent:hourly",
            "resources": [RESOURCE],
        }
        receipt = evaluate_production_request(request, IDENTITY, trusted_authorities())
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("self-assert trusted fields: authority", receipt["reasons"][0])

    def test_request_cannot_self_assert_human_signoff_or_review(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        request["human_signoff"] = True
        request["independent_review"] = True
        receipt = evaluate_production_request(request, IDENTITY, trusted_authorities())
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("human_signoff", receipt["reasons"][0])
        self.assertIn("independent_review", receipt["reasons"][0])

    def test_unknown_authority_reference_fails_closed(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-FABRICATED")
        receipt = evaluate_production_request(request, IDENTITY, trusted_authorities())
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("does not resolve in the trusted registry", receipt["reasons"][0])

    def test_role_mismatch_cannot_bypass_gate(self):
        receipt = evaluate_production_request(
            base_request(verb="PROPOSE", authority_ref="AUTH-INTEGRATOR"),
            IDENTITY,
            trusted_authorities(),
        )
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("AUTHORITY_SCOPE_DENIED", receipt["reasons"])
        with self.assertRaises(SemanticError):
            require_allowed(receipt)

    def test_stale_registry_is_rejected_before_action_evaluation(self):
        payload = registry_payload()
        payload["design_epoch"] = "v15.4"
        with self.assertRaises(SemanticError):
            authority_registry_from_payload(payload, IDENTITY)

    def test_stale_delta_accumulation_is_receipt_visible_and_blocked(self):
        request = base_request(verb="ACCUMULATE", authority_ref="AUTH-ACCUMULATOR")
        request["bound_inputs"] = [{
            "artifact_id": "DELTA-1",
            "kind": "DELTA",
            "design_epoch": "v15.4",
            "dependencies": {"canonical_source_root": "root-current"},
            "required_dependencies": ["canonical_source_root"],
            "derived_from_refs": ["FINDING-1"],
            "source_obligation_refs": ["Garden_System:DesignEpoch"],
        }]
        receipt = evaluate_production_request(request, IDENTITY, trusted_authorities())
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertTrue(any(reason.startswith("STALE_OR_UNKNOWN_INPUT:") for reason in receipt["reasons"]))
        with self.assertRaises(SemanticError):
            require_allowed(receipt)

    def test_delta_without_source_obligation_fails_transport(self):
        request = base_request(verb="ACCUMULATE", authority_ref="AUTH-ACCUMULATOR")
        request["bound_inputs"] = [{
            "artifact_id": "DELTA-1",
            "kind": "DELTA",
            "design_epoch": "v15.5",
            "dependencies": {"canonical_source_root": "root-current"},
            "required_dependencies": ["canonical_source_root"],
            "source_obligation_refs": [],
        }]
        receipt = evaluate_production_request(request, IDENTITY, trusted_authorities())
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertTrue(receipt["reasons"][0].startswith("TRANSPORT_INVALID:DELTA requires"))

    def test_constitutional_change_cannot_use_request_signoff(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        request["governance_tier"] = "CONSTITUTIONAL"
        receipt = evaluate_production_request(request, IDENTITY, trusted_authorities())
        self.assertEqual(receipt["decision"], "ESCALATE")
        self.assertIn("CONSTITUTIONAL_CHANGE_REQUIRES_HUMAN_SIGNOFF", receipt["reasons"])

        trusted_receipt = evaluate_production_request(
            request,
            IDENTITY,
            trusted_authorities(),
            trusted_human_signoff=True,
        )
        self.assertEqual(trusted_receipt["decision"], "ALLOW")

    def test_materialize_is_candidate_only_and_requires_trusted_review(self):
        request = base_request(verb="MATERIALIZE", authority_ref="AUTH-MATERIALIZER")
        request["bound_inputs"] = [{
            "artifact_id": "DELTA-1",
            "kind": "DELTA",
            "design_epoch": "v15.5",
            "dependencies": {"canonical_source_root": "root-current"},
            "required_dependencies": ["canonical_source_root"],
            "source_obligation_refs": ["Garden_System:SuccessorMaterialization"],
        }]
        receipt = evaluate_production_request(request, IDENTITY, trusted_authorities())
        self.assertEqual(receipt["decision"], "ESCALATE")
        self.assertTrue(receipt["materialization_candidate_only"])
        self.assertFalse(receipt["canonical_pointer_changed"])

        reviewed = evaluate_production_request(
            request,
            IDENTITY,
            trusted_authorities(),
            trusted_independent_review=True,
        )
        self.assertEqual(reviewed["decision"], "ALLOW")
        self.assertTrue(reviewed["trusted_attestations"]["independent_review"])

    def test_real_cli_blocks_fabricated_authority_but_writes_receipt(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-FABRICATED")
        manifest = {
            "schema": "GardenCanonicalSourceManifest/v1",
            "release": "Garden v15.5",
            "gsl": "v45.1",
            "source_root_sha256": "root-current",
        }
        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            request_path = td_path / "request.json"
            manifest_path = td_path / "manifest.json"
            registry_path = td_path / "authority.json"
            receipt_path = td_path / "receipt.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            registry_path.write_text(json.dumps(registry_payload()), encoding="utf-8")
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "gate_hourly_evolution.py"),
                    "--input", str(request_path),
                    "--output", str(receipt_path),
                    "--manifest", str(manifest_path),
                    "--authority-registry", str(registry_path),
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(proc.returncode, 2)
            self.assertTrue(receipt_path.exists())
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            self.assertEqual(receipt["decision"], "REJECT")
            self.assertEqual(receipt["receipt_visibility"], "PRESERVE_ALLOW_REJECT_ESCALATE")


if __name__ == "__main__":
    unittest.main()
