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
    MinimumRiskResponseStatus,
    PrerequisiteStatus,
    PrimaryReturnDisposition,
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
        authority_status=PrerequisiteStatus.PASS,
        fallback_qualification_status=PrerequisiteStatus.PASS,
        transfer_authentication_status=PrerequisiteStatus.PASS,
        actuator_trust_status=PrerequisiteStatus.PASS,
        dependency_status=PrerequisiteStatus.PASS,
        timing_evidence_status=PrerequisiteStatus.PASS,
        resource_status=PrerequisiteStatus.PASS,
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
                "CANONICAL_FUNCTION_RESULT_ALGEBRA",
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
        self.assertEqual(
            receipt.command_disposition,
            CommandDisposition.BLOCKED_HANDOFF_PREREQUISITE,
        )
        self.assertEqual(
            receipt.minimum_risk_response_status,
            MinimumRiskResponseStatus.REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE,
        )
        self.assertFalse(receipt.safety_certified)

    def test_eh18_003_violated_disturbance_profile_invalidates_assumptions(self) -> None:
        receipt = evaluate_handoff(admitted_request(disturbance_abs_bound=D("0.11")))
        self.assertEqual(receipt.disposition, EH18Disposition.ASSUMPTION_INVALID)

    def test_eh18_004_safe_but_not_recoverable_is_not_eligible(self) -> None:
        receipt = evaluate_handoff(admitted_request(estimated_level=D("0.10")))
        self.assertEqual(receipt.disposition, EH18Disposition.OUTSIDE_RECOVERABLE_REGION)
        self.assertEqual(receipt.observed_state_interval.lower, D("0.05"))
        self.assertEqual(
            receipt.command_disposition,
            CommandDisposition.BLOCKED_HANDOFF_PREREQUISITE,
        )
        self.assertEqual(
            receipt.minimum_risk_response_status,
            MinimumRiskResponseStatus.REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE,
        )
        self.assertIsNone(receipt.selected_minimum_risk_action)
        self.assertIsNone(receipt.domain_safety_case_ref)

    def test_eh18_005_outside_envelope_records_assurance_loss(self) -> None:
        receipt = evaluate_handoff(admitted_request(estimated_level=D("-0.01")))
        self.assertEqual(receipt.disposition, EH18Disposition.ASSURANCE_LOST)
        self.assertEqual(
            receipt.command_disposition,
            CommandDisposition.BLOCKED_HANDOFF_PREREQUISITE,
        )
        self.assertEqual(
            receipt.minimum_risk_response_status,
            MinimumRiskResponseStatus.REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE,
        )
        self.assertIsNone(receipt.selected_minimum_risk_action)
        self.assertIsNone(receipt.domain_safety_case_ref)
        self.assertFalse(receipt.safety_certified)

    def test_eh18_006_stale_transfer_and_old_command_are_rejected(self) -> None:
        receipt = evaluate_handoff(admitted_request(transfer_epoch=3))
        self.assertEqual(receipt.disposition, EH18Disposition.STALE)
        self.assertEqual(receipt.command_disposition, CommandDisposition.REJECTED_STALE_EPOCH)
        self.assertEqual(
            accept_actuator_command(3, 4, PrerequisiteStatus.PASS),
            CommandDisposition.REJECTED_STALE_EPOCH,
        )

    def test_eh18_007_primary_return_requires_revalidation_and_fresh_authority(self) -> None:
        self.assertEqual(
            primary_return_allowed(
                root_cause_status=PrerequisiteStatus.PASS,
                revalidation_status=PrerequisiteStatus.PASS,
                authority_status=PrerequisiteStatus.FAIL,
                envelope_status=PrerequisiteStatus.PASS,
            ),
            PrimaryReturnDisposition.BLOCKED_FAILED_PREREQUISITE,
        )
        self.assertEqual(
            primary_return_allowed(
                root_cause_status=PrerequisiteStatus.PASS,
                revalidation_status=PrerequisiteStatus.PASS,
                authority_status=PrerequisiteStatus.PASS,
                envelope_status=PrerequisiteStatus.PASS,
            ),
            PrimaryReturnDisposition.ALLOWED,
        )
        self.assertEqual(
            primary_return_allowed(
                root_cause_status=PrerequisiteStatus.PASS,
                revalidation_status=PrerequisiteStatus.PASS,
                authority_status=PrerequisiteStatus.PASS,
                envelope_status=PrerequisiteStatus.PASS,
                safety_override_requested=True,
            ),
            PrimaryReturnDisposition.BLOCKED_SAFETY_OVERRIDE,
        )

    def test_empty_recoverable_region_is_explicit(self) -> None:
        self.assertIsNone(takeover_recoverable_region(D("5"), D("0.05")))

    def test_incomplete_resource_binding_fails_closed(self) -> None:
        receipt = evaluate_handoff(
            admitted_request(resource_status=PrerequisiteStatus.RESOURCE_UNKNOWN)
        )
        self.assertEqual(receipt.disposition, EH18Disposition.RESOURCE_UNKNOWN)

    def test_unqualified_fallback_and_untrusted_actuator_are_distinct(self) -> None:
        fallback = evaluate_handoff(
            admitted_request(
                fallback_qualification_status=PrerequisiteStatus.FAIL
            )
        )
        actuator = evaluate_handoff(
            admitted_request(actuator_trust_status=PrerequisiteStatus.FAIL)
        )
        self.assertEqual(fallback.disposition, EH18Disposition.BLOCKED_FALLBACK_UNQUALIFIED)
        self.assertEqual(actuator.disposition, EH18Disposition.ACTUATOR_UNTRUSTED)
        self.assertEqual(
            fallback.command_disposition,
            CommandDisposition.BLOCKED_HANDOFF_PREREQUISITE,
        )
        self.assertEqual(
            actuator.command_disposition,
            CommandDisposition.BLOCKED_HANDOFF_PREREQUISITE,
        )

    def test_untyped_authority_is_malformed_not_truthy_authority(self) -> None:
        request = admitted_request(authority_status="yes")
        receipt = evaluate_handoff(request)  # type: ignore[arg-type]
        self.assertEqual(receipt.disposition, EH18Disposition.MALFORMED)
        self.assertEqual(
            receipt.command_disposition,
            CommandDisposition.NOT_EVALUATED_MALFORMED,
        )

    def test_wrong_request_object_returns_malformed_receipt(self) -> None:
        for request in (None, {}, object()):
            with self.subTest(request=request):
                receipt = evaluate_handoff(request)  # type: ignore[arg-type]
                self.assertEqual(receipt.disposition, EH18Disposition.MALFORMED)
                self.assertEqual(
                    receipt.command_disposition,
                    CommandDisposition.NOT_EVALUATED_MALFORMED,
                )
                self.assertFalse(receipt.safety_certified)

    def test_unknown_prerequisites_never_compose_to_command_acceptance(self) -> None:
        for changes in (
            {"dependency_status": PrerequisiteStatus.UNKNOWN},
            {"timing_evidence_status": PrerequisiteStatus.UNKNOWN},
            {"resource_status": PrerequisiteStatus.RESOURCE_UNKNOWN},
        ):
            with self.subTest(changes=changes):
                receipt = evaluate_handoff(admitted_request(**changes))
                self.assertNotEqual(
                    receipt.disposition,
                    EH18Disposition.ELIGIBLE_FOR_BOUNDED_SIMULATION,
                )
                self.assertEqual(
                    receipt.command_disposition,
                    CommandDisposition.BLOCKED_HANDOFF_PREREQUISITE,
                )
                self.assertEqual(
                    receipt.minimum_risk_response_status,
                    MinimumRiskResponseStatus.REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE,
                )

    def test_failed_unknown_stale_and_resource_unknown_remain_distinct(self) -> None:
        cases = (
            (
                {"dependency_status": PrerequisiteStatus.FAIL},
                EH18Disposition.BLOCKED_DEPENDENCY_INVALID,
            ),
            (
                {"dependency_status": PrerequisiteStatus.UNKNOWN},
                EH18Disposition.OUTCOME_UNKNOWN,
            ),
            (
                {"dependency_status": PrerequisiteStatus.STALE},
                EH18Disposition.STALE,
            ),
            (
                {"dependency_status": PrerequisiteStatus.RESOURCE_UNKNOWN},
                EH18Disposition.RESOURCE_UNKNOWN,
            ),
        )
        for changes, expected in cases:
            with self.subTest(changes=changes):
                receipt = evaluate_handoff(admitted_request(**changes))
                self.assertEqual(receipt.disposition, expected)
                self.assertEqual(
                    dict(receipt.prerequisite_statuses)["dependency"],
                    changes["dependency_status"],
                )
                self.assertNotEqual(
                    receipt.command_disposition,
                    CommandDisposition.ACCEPTED,
                )

    def test_each_prerequisite_preserves_nonbinary_status(self) -> None:
        fields = (
            "authority_status",
            "fallback_qualification_status",
            "transfer_authentication_status",
            "actuator_trust_status",
            "dependency_status",
            "timing_evidence_status",
            "resource_status",
        )
        for field in fields:
            for status, expected in (
                (PrerequisiteStatus.UNKNOWN, EH18Disposition.OUTCOME_UNKNOWN),
                (PrerequisiteStatus.STALE, EH18Disposition.STALE),
                (
                    PrerequisiteStatus.RESOURCE_UNKNOWN,
                    EH18Disposition.RESOURCE_UNKNOWN,
                ),
            ):
                with self.subTest(field=field, status=status):
                    receipt = evaluate_handoff(admitted_request(**{field: status}))
                    self.assertEqual(receipt.disposition, expected)
                    self.assertEqual(
                        dict(receipt.prerequisite_statuses)[
                            field.removesuffix("_status")
                        ],
                        status,
                    )

    def test_explicit_prerequisite_failures_remain_owner_specific(self) -> None:
        cases = (
            ("authority_status", EH18Disposition.BLOCKED_AUTHORITY),
            (
                "fallback_qualification_status",
                EH18Disposition.BLOCKED_FALLBACK_UNQUALIFIED,
            ),
            (
                "transfer_authentication_status",
                EH18Disposition.STATE_UNTRUSTED,
            ),
            ("actuator_trust_status", EH18Disposition.ACTUATOR_UNTRUSTED),
            (
                "dependency_status",
                EH18Disposition.BLOCKED_DEPENDENCY_INVALID,
            ),
            (
                "timing_evidence_status",
                EH18Disposition.BLOCKED_TIMING_EVIDENCE_INVALID,
            ),
            (
                "resource_status",
                EH18Disposition.BLOCKED_RESOURCE_INSUFFICIENT,
            ),
        )
        for field, expected in cases:
            with self.subTest(field=field):
                receipt = evaluate_handoff(
                    admitted_request(**{field: PrerequisiteStatus.FAIL})
                )
                self.assertEqual(receipt.disposition, expected)
                self.assertNotEqual(
                    receipt.command_disposition,
                    CommandDisposition.ACCEPTED,
                )

    def test_authority_status_is_preserved_through_command_fencing(self) -> None:
        cases = (
            (PrerequisiteStatus.FAIL, CommandDisposition.REJECTED_AUTHORITY),
            (
                PrerequisiteStatus.UNKNOWN,
                CommandDisposition.BLOCKED_AUTHORITY_UNKNOWN,
            ),
            (
                PrerequisiteStatus.STALE,
                CommandDisposition.REJECTED_AUTHORITY_STALE,
            ),
            (
                PrerequisiteStatus.RESOURCE_UNKNOWN,
                CommandDisposition.BLOCKED_AUTHORITY_RESOURCE_UNKNOWN,
            ),
        )
        for status, expected in cases:
            with self.subTest(status=status):
                self.assertEqual(accept_actuator_command(4, 4, status), expected)

    def test_primary_return_preserves_nonbinary_prerequisite_states(self) -> None:
        for status, expected in (
            (PrerequisiteStatus.UNKNOWN, PrimaryReturnDisposition.BLOCKED_UNKNOWN),
            (PrerequisiteStatus.STALE, PrimaryReturnDisposition.BLOCKED_STALE),
            (
                PrerequisiteStatus.RESOURCE_UNKNOWN,
                PrimaryReturnDisposition.BLOCKED_RESOURCE_UNKNOWN,
            ),
        ):
            with self.subTest(status=status):
                self.assertEqual(
                    primary_return_allowed(
                        root_cause_status=PrerequisiteStatus.PASS,
                        revalidation_status=status,
                        authority_status=PrerequisiteStatus.PASS,
                        envelope_status=PrerequisiteStatus.PASS,
                    ),
                    expected,
                )

    def test_primary_return_rejects_malformed_runtime_values(self) -> None:
        valid = {
            "root_cause_status": PrerequisiteStatus.PASS,
            "revalidation_status": PrerequisiteStatus.PASS,
            "authority_status": PrerequisiteStatus.PASS,
            "envelope_status": PrerequisiteStatus.PASS,
        }
        for malformed_override in (None, 0, "", D("0")):
            with self.subTest(malformed_override=malformed_override):
                self.assertEqual(
                    primary_return_allowed(
                        **valid,
                        safety_override_requested=malformed_override,  # type: ignore[arg-type]
                    ),
                    PrimaryReturnDisposition.MALFORMED,
                )
        self.assertEqual(
            primary_return_allowed(
                **{
                    **valid,
                    "root_cause_status": "PASS",  # type: ignore[dict-item]
                }
            ),
            PrimaryReturnDisposition.MALFORMED,
        )


if __name__ == "__main__":
    unittest.main()
