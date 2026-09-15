from __future__ import annotations

import json
from pathlib import Path
import unittest

from garden_kernel.core import SemanticError
from garden_kernel.process_engine import (
    CURRENT_GOVERNING_PROCESS_VERSION,
    CycleBinding,
    MajorDelegableProcess,
    MajorProtectedProcess,
    NonSemanticRepairProcess,
    PatchDeltaProcess,
    ProcessFactory,
    ProcessRoute,
    ProcessState,
    SectionUnitReviewProcess,
)

ROOT = Path(__file__).resolve().parents[2]
PROFILE = json.loads((ROOT / "gsl" / "EVOLUTION_ALGEBRA_PROFILE.json").read_text(encoding="utf-8"))
SOURCE_ROOT = "63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598"
REFS = [
    "governance/PROCESS_CURRENT.json",
    "governance/GardenCanonicalUpdateProcess_v1.4.json",
    "canonical/current/Garden_System_v15.5_FULL_2026-09-12.txt:REG-ALGEBRA-001",
]


def binding(version: str = CURRENT_GOVERNING_PROCESS_VERSION) -> CycleBinding:
    return CycleBinding(
        cycle_id="CYCLE-PROCESS-ENGINE-TEST-001",
        process_version=version,
        design_epoch="v15.5",
        source_root_sha256=SOURCE_ROOT,
        repo_heads={"garden-main": "a" * 40, "garden-swarm": "b" * 40},
    )


def advance(process, target: ProcessState):
    return process.advance(
        target,
        satisfied_gates=sorted(process.required_gates(target)),
        algebra_profile=PROFILE,
        source_obligation_refs=REFS,
    )


class GardenProcessEngineTests(unittest.TestCase):
    def test_factory_covers_all_six_routes(self):
        expected = {
            ProcessRoute.SECTION_UNIT_REVIEW: SectionUnitReviewProcess,
            ProcessRoute.NON_SEMANTIC_REPAIR: NonSemanticRepairProcess,
            ProcessRoute.PATCH_DELTA: PatchDeltaProcess,
            ProcessRoute.MAJOR_DELEGABLE: MajorDelegableProcess,
            ProcessRoute.MAJOR_PROTECTED: MajorProtectedProcess,
        }
        for route in ProcessRoute:
            process = ProcessFactory.create(route, binding=binding(), work_id=route.value)
            if route in expected:
                self.assertIsInstance(process, expected[route])
            self.assertEqual(process.route, route)

    def test_cycle_binding_rejects_wrong_process_version(self):
        with self.assertRaises(SemanticError):
            ProcessFactory.create(
                ProcessRoute.PATCH_DELTA,
                binding=binding("1.3"),
                work_id="wrong-version",
            )

    def test_route_receipt_exposes_light_forbidden_steps(self):
        process = ProcessFactory.create(ProcessRoute.NON_SEMANTIC_REPAIR, binding=binding(), work_id="light")
        receipt = process.route_receipt()
        self.assertIn("semantic_delta_admission", receipt["forbidden_steps"])
        self.assertTrue(receipt["silent_downgrade_forbidden"])

    def test_non_semantic_route_cannot_enter_semantic_admission(self):
        process = ProcessFactory.create(ProcessRoute.NON_SEMANTIC_REPAIR, binding=binding(), work_id="light")
        with self.assertRaises(SemanticError):
            process.required_gates(ProcessState.ADMITTED)

    def test_parallel_review_transition_is_process_algebra_bound(self):
        process = ProcessFactory.create(ProcessRoute.SECTION_UNIT_REVIEW, binding=binding(), work_id="section")
        advance(process, ProcessState.ROUTED)
        advance(process, ProcessState.PACKET_READY)
        receipt = advance(process, ProcessState.BLIND_REVIEW_COMPLETE)
        self.assertEqual(receipt["process_operator"], "PARALLEL")
        self.assertEqual(receipt["algebra_registry_ref"], "REG-ALGEBRA-001")
        self.assertFalse(receipt["semantic_compliance_proved"])
        process_entry = receipt["algebra_usage"]["entries"][0]
        self.assertEqual(process_entry["operators"], ["PARALLEL"])
        self.assertIn("PARALLEL_EFFECT_COMMUTATIVITY_NOT_UNIVERSAL", process_entry["non_law_acknowledgements"])
        self.assertEqual(receipt["algebra_validation"]["authorization_result"], "NOT_EVALUATED_HERE")

    def test_patch_composition_uses_registered_compose_operator(self):
        process = ProcessFactory.create(ProcessRoute.PATCH_DELTA, binding=binding(), work_id="patch")
        for state in (
            ProcessState.ROUTED,
            ProcessState.PACKET_READY,
            ProcessState.BLIND_REVIEW_COMPLETE,
            ProcessState.CROSS_EXAM_COMPLETE,
            ProcessState.VALIDATED,
            ProcessState.ADMITTED,
        ):
            advance(process, state)
        receipt = advance(process, ProcessState.COMPOSED)
        self.assertEqual(receipt["process_operator"], "COMPOSE")
        self.assertEqual(receipt["algebra_validation"]["applied"], ["Process", "Conformance"])

    def test_major_routes_are_siblings_not_authority_inheritance(self):
        self.assertFalse(issubclass(MajorProtectedProcess, MajorDelegableProcess))
        self.assertFalse(issubclass(MajorDelegableProcess, MajorProtectedProcess))

    def test_major_protected_promotion_requires_human_gate(self):
        process = ProcessFactory.create(ProcessRoute.MAJOR_PROTECTED, binding=binding(), work_id="major-protected")
        process._state = ProcessState.PROMOTION_READY
        required = process.required_gates(ProcessState.PROMOTED)
        self.assertIn("HUMAN_PROTECTED_DECISION_VALID", required)
        self.assertIn("CANONICAL_PROMOTION_AUTHORIZED", required)
        with self.assertRaises(SemanticError):
            process.advance(
                ProcessState.PROMOTED,
                satisfied_gates=["CANONICAL_PROMOTION_AUTHORIZED"],
                algebra_profile=PROFILE,
                source_obligation_refs=REFS,
            )

    def test_major_promotion_ready_requires_simplification_and_coverage(self):
        process = ProcessFactory.create(ProcessRoute.MAJOR_DELEGABLE, binding=binding(), work_id="major")
        process._state = ProcessState.VERIFIED
        required = process.required_gates(ProcessState.PROMOTION_READY)
        self.assertIn("SIMPLIFICATION_RECEIPT_VERIFIED", required)
        self.assertIn("RULE_ENFORCEMENT_COVERAGE_SUFFICIENT", required)
        self.assertIn("ROLLBACK_READY", required)


if __name__ == "__main__":
    unittest.main()
