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
from garden_kernel.evolution_trust import (
    AttestationKind,
    governance_receipt_from_changed_paths,
    make_attestation_receipt,
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
    }


def governance_for(request: dict, *paths: str) -> dict:
    return governance_receipt_from_changed_paths(
        action_id=request["action"]["action_id"],
        design_epoch=IDENTITY.design_epoch,
        source_root_sha256=IDENTITY.source_root_sha256,
        changed_paths=paths or ("implementation/garden_kernel/evolution_transport.py",),
        base_ref="base",
        head_ref="head",
    )


def evaluate(request: dict, *, paths: tuple[str, ...] = (), attestations=(), attestors=None):
    return evaluate_production_request(
        request,
        IDENTITY,
        trusted_authorities(),
        trusted_governance_receipt=governance_for(request, *paths),
        trusted_attestation_receipts=attestations,
        trusted_attestors=attestors or {},
    )


class ProductionEvolutionTransportTests(unittest.TestCase):
    def test_valid_proposal_uses_trusted_registry_and_derived_governance(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        receipt = evaluate(request)
        self.assertEqual(receipt["decision"], "ALLOW")
        self.assertFalse(receipt["canonical_pointer_changed"])
        self.assertEqual(receipt["authority_ref"], "AUTH-REVIEWER")
        self.assertFalse(receipt["authority"]["can_mint_envelopes"])
        self.assertFalse(receipt["authority"]["can_promote_canon"])
        self.assertFalse(receipt["trusted_attestations"]["human_signoff"])
        self.assertTrue(receipt["governance"]["verified"])
        self.assertEqual(receipt["governance"]["tier"], "ORDINARY")
        require_allowed(receipt)

    def test_request_cannot_self_assert_authority_or_governance(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        request["authority"] = {"role": "REVIEWER"}
        request["governance_tier"] = "ORDINARY"
        receipt = evaluate(request)
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("authority", receipt["reasons"][0])
        self.assertIn("governance_tier", receipt["reasons"][0])

    def test_request_cannot_self_assert_human_signoff_or_review(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        request["human_signoff"] = True
        request["independent_review"] = True
        receipt = evaluate(request)
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("human_signoff", receipt["reasons"][0])
        self.assertIn("independent_review", receipt["reasons"][0])

    def test_missing_trusted_governance_receipt_fails_closed(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        receipt = evaluate_production_request(
            request,
            IDENTITY,
            trusted_authorities(),
            trusted_governance_receipt=None,
        )
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("trusted governance classification receipt is required", receipt["reasons"][0])

    def test_tampered_governance_receipt_fails_closed(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        governance = governance_for(request)
        governance["tier"] = "CONSTITUTIONAL"
        receipt = evaluate_production_request(
            request,
            IDENTITY,
            trusted_authorities(),
            trusted_governance_receipt=governance,
        )
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("governance classification receipt hash mismatch", receipt["reasons"][0])

    def test_protected_policy_change_is_derived_constitutional_and_escalates(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        receipt = evaluate(
            request,
            paths=("implementation/garden_kernel/evolution_gate.py",),
        )
        self.assertEqual(receipt["decision"], "ESCALATE")
        self.assertEqual(receipt["governance"]["tier"], "CONSTITUTIONAL")
        self.assertIn("ACTION_GATE_RULES", receipt["governance"]["domains"])
        self.assertIn("CONSTITUTIONAL_CHANGE_REQUIRES_HUMAN_SIGNOFF", receipt["reasons"])

    def test_constitutional_human_approval_requires_verified_receipt(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        attestation = make_attestation_receipt(
            receipt_id="H-1",
            kind=AttestationKind.HUMAN_SIGNOFF,
            action_id=request["action"]["action_id"],
            design_epoch=IDENTITY.design_epoch,
            source_root_sha256=IDENTITY.source_root_sha256,
            issuer_ref="human:operator",
            evidence_refs=("approval:explicit",),
        )
        receipt = evaluate(
            request,
            paths=("implementation/garden_kernel/evolution_gate.py",),
            attestations=(attestation,),
            attestors={"human:operator": frozenset({AttestationKind.HUMAN_SIGNOFF})},
        )
        self.assertEqual(receipt["decision"], "ALLOW")
        self.assertTrue(receipt["trusted_attestations"]["human_signoff"])
        self.assertEqual(receipt["trusted_attestations"]["verified_receipt_ids"], ["H-1"])

    def test_untrusted_or_tampered_attestation_cannot_enable_signoff(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        attestation = make_attestation_receipt(
            receipt_id="H-1",
            kind=AttestationKind.HUMAN_SIGNOFF,
            action_id=request["action"]["action_id"],
            design_epoch=IDENTITY.design_epoch,
            source_root_sha256=IDENTITY.source_root_sha256,
            issuer_ref="agent:hourly",
            evidence_refs=("self-claim",),
        )
        receipt = evaluate(
            request,
            paths=("implementation/garden_kernel/evolution_gate.py",),
            attestations=(attestation,),
            attestors={},
        )
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("attestation issuer is not trusted", receipt["reasons"][0])

        attestation["issuer_ref"] = "human:operator"
        receipt = evaluate(
            request,
            paths=("implementation/garden_kernel/evolution_gate.py",),
            attestations=(attestation,),
            attestors={"human:operator": frozenset({AttestationKind.HUMAN_SIGNOFF})},
        )
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("trusted attestation receipt hash mismatch", receipt["reasons"][0])

    def test_unknown_authority_reference_fails_closed(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-FABRICATED")
        receipt = evaluate(request)
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertIn("does not resolve in the trusted registry", receipt["reasons"][0])

    def test_role_mismatch_cannot_bypass_gate(self):
        request = base_request(verb="PROPOSE", authority_ref="AUTH-INTEGRATOR")
        receipt = evaluate(request)
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
        receipt = evaluate(request)
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
        receipt = evaluate(request)
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertTrue(receipt["reasons"][0].startswith("TRANSPORT_INVALID:DELTA requires"))

    def test_materialize_is_candidate_only_and_requires_verified_review(self):
        request = base_request(verb="MATERIALIZE", authority_ref="AUTH-MATERIALIZER")
        request["bound_inputs"] = [{
            "artifact_id": "DELTA-1",
            "kind": "DELTA",
            "design_epoch": "v15.5",
            "dependencies": {"canonical_source_root": "root-current"},
            "required_dependencies": ["canonical_source_root"],
            "source_obligation_refs": ["Garden_System:SuccessorMaterialization"],
        }]
        receipt = evaluate(request)
        self.assertEqual(receipt["decision"], "ESCALATE")
        self.assertTrue(receipt["materialization_candidate_only"])
        self.assertFalse(receipt["canonical_pointer_changed"])

        review = make_attestation_receipt(
            receipt_id="R-1",
            kind=AttestationKind.INDEPENDENT_REVIEW,
            action_id=request["action"]["action_id"],
            design_epoch=IDENTITY.design_epoch,
            source_root_sha256=IDENTITY.source_root_sha256,
            issuer_ref="reviewer:independent",
            evidence_refs=("review:receipt:1",),
        )
        reviewed = evaluate(
            request,
            attestations=(review,),
            attestors={"reviewer:independent": frozenset({AttestationKind.INDEPENDENT_REVIEW})},
        )
        self.assertEqual(reviewed["decision"], "ALLOW")
        self.assertTrue(reviewed["trusted_attestations"]["independent_review"])

    def _run_cli(self, request: dict) -> tuple[subprocess.CompletedProcess[str], dict]:
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
                    "--base-ref", "HEAD^",
                    "--head-ref", "HEAD",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertTrue(receipt_path.exists(), proc.stdout + proc.stderr)
            return proc, json.loads(receipt_path.read_text(encoding="utf-8"))

    def test_real_cli_blocks_fabricated_authority_but_writes_receipt(self):
        proc, receipt = self._run_cli(
            base_request(verb="PROPOSE", authority_ref="AUTH-FABRICATED")
        )
        self.assertEqual(proc.returncode, 2, proc.stdout + proc.stderr)
        self.assertEqual(receipt["decision"], "REJECT")
        self.assertFalse(receipt["governance"]["verified"])
        self.assertEqual(receipt["receipt_visibility"], "PRESERVE_ALLOW_REJECT_ESCALATE")

    def test_real_cli_valid_authority_derives_and_verifies_governance(self):
        proc, receipt = self._run_cli(
            base_request(verb="PROPOSE", authority_ref="AUTH-REVIEWER")
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertEqual(receipt["decision"], "ALLOW")
        self.assertTrue(receipt["governance"]["verified"])
        self.assertEqual(receipt["governance"]["evidence_source"], "TRUSTED_GIT_DIFF")
        self.assertFalse(receipt["trusted_attestations"]["human_signoff"])
        self.assertFalse(receipt["trusted_attestations"]["independent_review"])
        self.assertFalse(receipt["canonical_pointer_changed"])


if __name__ == "__main__":
    unittest.main()
