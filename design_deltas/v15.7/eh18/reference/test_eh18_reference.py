from __future__ import annotations

from dataclasses import replace
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import unittest

from eh18_reference import (
    CommandDisposition,
    EH18Disposition,
    EH18HandoffRequest,
    accept_actuator_command,
    evaluate_handoff,
    primary_return_allowed,
    switching_margin,
    takeover_recoverable_region,
)
from garden_kernel.function_contracts import (
    audit_function_contract_coverage,
    load_function_contract_registry,
    validate_registry_against_manifest,
)


D = Decimal
ROOT = Path(__file__).resolve().parents[4]


def admitted_request(**changes: object) -> EH18HandoffRequest:
    request = EH18HandoffRequest(
        estimated_level=D("5"),
        estimation_error=D("0.05"),
        disturbance_abs_bound=D("0.1"),
        primary_command_abs_bound=D("1"),
        fallback_command_abs=D("0.2"),
        actuator_lower_bound=D("-1"),
        actuator_upper_bound=D("1"),
        sensor_age=D("0.10"),
        monitor_phase=D("0.10"),
        remaining_uncontrolled_delay=D("0.20"),
        transfer_epoch=4,
        current_actuation_epoch=4,
        fresh_authority=True,
        fallback_qualified=True,
        transfer_authenticated=True,
        actuator_trusted=True,
        dependency_roots_current=True,
        timing_evidence_complete=True,
        resource_bounds_known=True,
    )
    return replace(request, **changes)


class EH18ReferenceTests(unittest.TestCase):
    def test_review_source_anchors_match_bound_source_bytes(self) -> None:
        anchor_path = ROOT / "reviews" / "v15.7" / "eh18" / "SOURCE_ANCHORS.json"
        payload = json.loads(anchor_path.read_text(encoding="utf-8"))
        self.assertEqual(payload["schema"], "GardenBoundedSourceAnchorSet/v1")
        self.assertEqual(
            {row["anchor_id"] for row in payload["anchors"]},
            {
                "T-EH-18_PROFILE_INVARIANTS_BINDING",
                "T-EH-18_TESTS",
                "CANONICAL_CONTINUITY_CONTRACT",
                "CCC-001..010",
                "TEST-CCC-001..006",
            },
        )
        for row in payload["anchors"]:
            source_bytes = (ROOT / row["source_path"]).read_bytes()
            self.assertEqual(hashlib.sha256(source_bytes).hexdigest(), row["source_sha256"])
            source_lines = source_bytes.decode("utf-8").splitlines(keepends=True)
            excerpt = "".join(source_lines[row["start_line"] - 1 : row["end_line"]])
            self.assertEqual(excerpt, row["text"])
            self.assertEqual(
                hashlib.sha256(excerpt.encode("utf-8")).hexdigest(),
                row["excerpt_sha256"],
            )

    def test_candidate_contract_is_bound_and_has_explicit_frontier(self) -> None:
        registry = load_function_contract_registry(
            ROOT / "design_deltas" / "v15.7" / "eh18" / "FUNCTION_CONTRACT.json"
        )
        manifest = json.loads(
            (ROOT / "canonical" / "candidates" / "v15.7" / "SOURCE_MANIFEST.json").read_text(
                encoding="utf-8"
            )
        )
        validate_registry_against_manifest(registry, manifest)
        report = audit_function_contract_coverage(ROOT, registry)
        records = {record.identity: record for record in report.functions}
        declared = (
            "design_deltas/v15.7/eh18/reference/eh18_reference.py::evaluate_handoff"
        )
        self.assertEqual(records[declared].contract_id, "FC-EH18-REFERENCE-001")
        self.assertGreater(report.frontier_function_count, 0)
        self.assertFalse(report.semantic_compliance_proved)

    def test_eh18_001_candidate_margin_and_boundary_reachability(self) -> None:
        self.assertEqual(
            switching_margin(D("0.05"), D("0.10"), D("0.10"), D("0.20")),
            D("0.49"),
        )
        lower = admitted_request(estimated_level=D("0.27"))
        receipt = evaluate_handoff(lower)
        self.assertEqual(receipt.disposition, EH18Disposition.ELIGIBLE_FOR_BOUNDED_SIMULATION)
        self.assertEqual(receipt.delayed_reachable_interval.lower, D("0.00"))
        self.assertFalse(receipt.safety_certified)

    def test_eh18_002_failed_or_excessive_handoff_never_passes(self) -> None:
        receipt = evaluate_handoff(
            admitted_request(remaining_uncontrolled_delay=D("0.21"))
        )
        self.assertEqual(receipt.disposition, EH18Disposition.ASSUMPTION_INVALID)
        self.assertFalse(receipt.safety_certified)

    def test_eh18_003_violated_disturbance_profile_invalidates_assumptions(self) -> None:
        receipt = evaluate_handoff(admitted_request(disturbance_abs_bound=D("0.11")))
        self.assertEqual(receipt.disposition, EH18Disposition.ASSUMPTION_INVALID)

    def test_eh18_004_safe_but_not_recoverable_is_not_eligible(self) -> None:
        receipt = evaluate_handoff(admitted_request(estimated_level=D("0.10")))
        self.assertEqual(receipt.disposition, EH18Disposition.OUTSIDE_RECOVERABLE_REGION)
        self.assertEqual(receipt.observed_state_interval.lower, D("0.05"))

    def test_eh18_005_outside_envelope_records_assurance_loss(self) -> None:
        receipt = evaluate_handoff(admitted_request(estimated_level=D("-0.01")))
        self.assertEqual(receipt.disposition, EH18Disposition.ASSURANCE_LOST)
        self.assertFalse(receipt.safety_certified)

    def test_eh18_006_stale_transfer_and_old_command_are_rejected(self) -> None:
        receipt = evaluate_handoff(admitted_request(transfer_epoch=3))
        self.assertEqual(receipt.disposition, EH18Disposition.STALE)
        self.assertEqual(receipt.command_disposition, CommandDisposition.REJECTED_STALE_EPOCH)
        self.assertEqual(
            accept_actuator_command(3, 4, True),
            CommandDisposition.REJECTED_STALE_EPOCH,
        )

    def test_eh18_007_primary_return_requires_revalidation_and_fresh_authority(self) -> None:
        self.assertFalse(
            primary_return_allowed(
                root_cause_closed=True,
                revalidated=True,
                fresh_authority=False,
                inside_valid_envelope=True,
            )
        )
        self.assertTrue(
            primary_return_allowed(
                root_cause_closed=True,
                revalidated=True,
                fresh_authority=True,
                inside_valid_envelope=True,
            )
        )
        self.assertFalse(
            primary_return_allowed(
                root_cause_closed=True,
                revalidated=True,
                fresh_authority=True,
                inside_valid_envelope=True,
                safety_override_requested=True,
            )
        )

    def test_empty_recoverable_region_is_explicit(self) -> None:
        self.assertIsNone(takeover_recoverable_region(D("5"), D("0.05")))

    def test_incomplete_resource_binding_fails_closed(self) -> None:
        receipt = evaluate_handoff(admitted_request(resource_bounds_known=False))
        self.assertEqual(receipt.disposition, EH18Disposition.RESOURCE_UNKNOWN)

    def test_unqualified_fallback_and_untrusted_actuator_are_distinct(self) -> None:
        fallback = evaluate_handoff(admitted_request(fallback_qualified=False))
        actuator = evaluate_handoff(admitted_request(actuator_trusted=False))
        self.assertEqual(fallback.disposition, EH18Disposition.BLOCKED_FALLBACK_UNQUALIFIED)
        self.assertEqual(actuator.disposition, EH18Disposition.ACTUATOR_UNTRUSTED)

    def test_untyped_authority_is_malformed_not_truthy_authority(self) -> None:
        request = admitted_request(fresh_authority="yes")
        receipt = evaluate_handoff(request)  # type: ignore[arg-type]
        self.assertEqual(receipt.disposition, EH18Disposition.MALFORMED)


if __name__ == "__main__":
    unittest.main()
