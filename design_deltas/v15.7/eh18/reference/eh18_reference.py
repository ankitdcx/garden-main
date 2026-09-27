"""Candidate-contained executable reference for Garden v15.7 EH-18.

This module checks the bounded single-tank handoff profile.  It is not an
actuator driver, deployment controller, safety certificate, or authority
source.  A positive result means only that the supplied case is eligible for
the bounded simulation/verification step described by T-EH-18.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from enum import Enum


ZERO = Decimal("0")
TEN = Decimal("10")
MAX_OUTWARD_SPEED = Decimal("1.1")
MAX_ESTIMATION_ERROR = Decimal("0.05")
MAX_DISTURBANCE = Decimal("0.1")
MAX_SENSOR_AGE = Decimal("0.10")
MAX_MONITOR_PHASE = Decimal("0.10")
MAX_REMAINING_HANDOFF_DELAY = Decimal("0.20")


class EH18Disposition(str, Enum):
    ELIGIBLE_FOR_BOUNDED_SIMULATION = "ELIGIBLE_FOR_BOUNDED_SIMULATION"
    BLOCKED_AUTHORITY = "BLOCKED_AUTHORITY"
    BLOCKED_FALLBACK_UNQUALIFIED = "BLOCKED_FALLBACK_UNQUALIFIED"
    BLOCKED_DEPENDENCY_INVALID = "BLOCKED_DEPENDENCY_INVALID"
    BLOCKED_TIMING_EVIDENCE_INVALID = "BLOCKED_TIMING_EVIDENCE_INVALID"
    BLOCKED_RESOURCE_INSUFFICIENT = "BLOCKED_RESOURCE_INSUFFICIENT"
    STATE_UNTRUSTED = "STATE_UNTRUSTED"
    OUTSIDE_RECOVERABLE_REGION = "OUTSIDE_RECOVERABLE_REGION"
    ACTUATOR_UNTRUSTED = "ACTUATOR_UNTRUSTED"
    ASSUMPTION_INVALID = "ASSUMPTION_INVALID"
    ASSURANCE_LOST = "ASSURANCE_LOST"
    STALE = "STALE"
    OUTCOME_UNKNOWN = "OUTCOME_UNKNOWN"
    RESOURCE_UNKNOWN = "RESOURCE_UNKNOWN"
    MALFORMED = "MALFORMED"


class CommandDisposition(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED_STALE_EPOCH = "REJECTED_STALE_EPOCH"
    REJECTED_AUTHORITY = "REJECTED_AUTHORITY"
    REJECTED_AUTHORITY_STALE = "REJECTED_AUTHORITY_STALE"
    BLOCKED_AUTHORITY_UNKNOWN = "BLOCKED_AUTHORITY_UNKNOWN"
    BLOCKED_AUTHORITY_RESOURCE_UNKNOWN = "BLOCKED_AUTHORITY_RESOURCE_UNKNOWN"
    BLOCKED_HANDOFF_PREREQUISITE = "BLOCKED_HANDOFF_PREREQUISITE"
    NOT_EVALUATED_MALFORMED = "NOT_EVALUATED_MALFORMED"


class MinimumRiskResponseStatus(str, Enum):
    NOT_REQUIRED_FOR_ELIGIBILITY = "NOT_REQUIRED_FOR_ELIGIBILITY"
    REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE = (
        "REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE"
    )


class PrerequisiteStatus(str, Enum):
    """Non-binary status retained for each handoff prerequisite."""

    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"
    STALE = "STALE"
    RESOURCE_UNKNOWN = "RESOURCE_UNKNOWN"


class PrimaryReturnDisposition(str, Enum):
    ALLOWED = "ALLOWED"
    BLOCKED_SAFETY_OVERRIDE = "BLOCKED_SAFETY_OVERRIDE"
    BLOCKED_FAILED_PREREQUISITE = "BLOCKED_FAILED_PREREQUISITE"
    BLOCKED_UNKNOWN = "BLOCKED_UNKNOWN"
    BLOCKED_STALE = "BLOCKED_STALE"
    BLOCKED_RESOURCE_UNKNOWN = "BLOCKED_RESOURCE_UNKNOWN"


@dataclass(frozen=True)
class Interval:
    lower: Decimal
    upper: Decimal

    def contains(self, value: Decimal) -> bool:
        return self.lower <= value <= self.upper

    def contained_by(self, outer: "Interval") -> bool:
        return outer.lower <= self.lower and self.upper <= outer.upper


@dataclass(frozen=True)
class EH18HandoffRequest:
    estimated_level: Decimal
    estimation_error: Decimal
    disturbance_abs_bound: Decimal
    primary_command_abs_bound: Decimal
    fallback_command_abs: Decimal
    actuator_lower_bound: Decimal
    actuator_upper_bound: Decimal
    sensor_age: Decimal
    monitor_phase: Decimal
    remaining_uncontrolled_delay: Decimal
    transfer_epoch: int
    current_actuation_epoch: int
    authority_status: PrerequisiteStatus
    fallback_qualification_status: PrerequisiteStatus
    transfer_authentication_status: PrerequisiteStatus
    actuator_trust_status: PrerequisiteStatus
    dependency_status: PrerequisiteStatus
    timing_evidence_status: PrerequisiteStatus
    resource_status: PrerequisiteStatus


@dataclass(frozen=True)
class EH18HandoffReceipt:
    disposition: EH18Disposition
    observed_state_interval: Interval | None
    recoverable_center_interval: Interval | None
    delayed_reachable_interval: Interval | None
    command_disposition: CommandDisposition
    minimum_risk_response_status: MinimumRiskResponseStatus
    prerequisite_statuses: tuple[tuple[str, PrerequisiteStatus], ...]
    selected_minimum_risk_action: str | None = None
    domain_safety_case_ref: str | None = None
    safety_certified: bool = False
    canonical_effect: str = "NONE"


def _valid_nonnegative(value: Decimal) -> bool:
    try:
        return value.is_finite() and value >= ZERO
    except (AttributeError, InvalidOperation):
        return False


def _valid_finite(value: Decimal) -> bool:
    return isinstance(value, Decimal) and value.is_finite()


def _request_types_valid(request: EH18HandoffRequest) -> bool:
    decimal_fields = (
        request.estimated_level,
        request.estimation_error,
        request.disturbance_abs_bound,
        request.primary_command_abs_bound,
        request.fallback_command_abs,
        request.actuator_lower_bound,
        request.actuator_upper_bound,
        request.sensor_age,
        request.monitor_phase,
        request.remaining_uncontrolled_delay,
    )
    prerequisite_fields = (
        request.authority_status,
        request.fallback_qualification_status,
        request.transfer_authentication_status,
        request.actuator_trust_status,
        request.dependency_status,
        request.timing_evidence_status,
        request.resource_status,
    )
    epochs_are_ints = all(
        isinstance(value, int) and not isinstance(value, bool) and value >= 0
        for value in (request.transfer_epoch, request.current_actuation_epoch)
    )
    return (
        all(_valid_finite(value) for value in decimal_fields)
        and all(isinstance(value, PrerequisiteStatus) for value in prerequisite_fields)
        and epochs_are_ints
    )


def _prerequisite_statuses(
    request: EH18HandoffRequest,
) -> tuple[tuple[str, PrerequisiteStatus], ...]:
    return (
        ("authority", request.authority_status),
        ("fallback_qualification", request.fallback_qualification_status),
        ("transfer_authentication", request.transfer_authentication_status),
        ("actuator_trust", request.actuator_trust_status),
        ("dependency", request.dependency_status),
        ("timing_evidence", request.timing_evidence_status),
        ("resource", request.resource_status),
    )


def switching_margin(
    estimation_error: Decimal,
    observation_age: Decimal,
    monitor_phase: Decimal,
    handoff_delay: Decimal,
) -> Decimal:
    """Return e + 1.1 * (age + phase + delay) for the EH-18 profile."""

    values = (estimation_error, observation_age, monitor_phase, handoff_delay)
    if not all(_valid_nonnegative(value) for value in values):
        raise ValueError("EH-18 margin inputs must be finite and nonnegative")
    return estimation_error + MAX_OUTWARD_SPEED * (
        observation_age + monitor_phase + handoff_delay
    )


def takeover_recoverable_region(
    remaining_uncontrolled_delay: Decimal,
    estimation_error: Decimal,
) -> Interval | None:
    """Return the allowed estimated-center interval, or None when it is empty."""

    if not _valid_nonnegative(remaining_uncontrolled_delay) or not _valid_nonnegative(
        estimation_error
    ):
        raise ValueError("EH-18 delay/error inputs must be finite and nonnegative")
    margin = MAX_OUTWARD_SPEED * remaining_uncontrolled_delay + estimation_error
    lower = margin
    upper = TEN - margin
    if lower > upper:
        return None
    return Interval(lower=lower, upper=upper)


def reachable_interval_during_delay(
    estimated_level: Decimal,
    estimation_error: Decimal,
    remaining_uncontrolled_delay: Decimal,
) -> Interval:
    """Closed-form worst-case interval before the fallback has control."""

    if not _valid_nonnegative(estimation_error) or not _valid_nonnegative(
        remaining_uncontrolled_delay
    ):
        raise ValueError("EH-18 delay/error inputs must be finite and nonnegative")
    if not isinstance(estimated_level, Decimal) or not estimated_level.is_finite():
        raise ValueError("EH-18 estimated level must be finite")
    travel = MAX_OUTWARD_SPEED * remaining_uncontrolled_delay
    return Interval(
        lower=estimated_level - estimation_error - travel,
        upper=estimated_level + estimation_error + travel,
    )


def accept_actuator_command(
    command_epoch: int,
    current_actuation_epoch: int,
    authority_status: PrerequisiteStatus,
) -> CommandDisposition:
    """Fence old/future epochs and preserve non-binary authority status."""

    if (
        not isinstance(command_epoch, int)
        or isinstance(command_epoch, bool)
        or command_epoch < 0
        or not isinstance(current_actuation_epoch, int)
        or isinstance(current_actuation_epoch, bool)
        or current_actuation_epoch < 0
        or not isinstance(authority_status, PrerequisiteStatus)
    ):
        return CommandDisposition.NOT_EVALUATED_MALFORMED
    if command_epoch != current_actuation_epoch:
        return CommandDisposition.REJECTED_STALE_EPOCH
    if authority_status is PrerequisiteStatus.FAIL:
        return CommandDisposition.REJECTED_AUTHORITY
    if authority_status is PrerequisiteStatus.STALE:
        return CommandDisposition.REJECTED_AUTHORITY_STALE
    if authority_status is PrerequisiteStatus.UNKNOWN:
        return CommandDisposition.BLOCKED_AUTHORITY_UNKNOWN
    if authority_status is PrerequisiteStatus.RESOURCE_UNKNOWN:
        return CommandDisposition.BLOCKED_AUTHORITY_RESOURCE_UNKNOWN
    return CommandDisposition.ACCEPTED


def primary_return_allowed(
    *,
    root_cause_status: PrerequisiteStatus,
    revalidation_status: PrerequisiteStatus,
    authority_status: PrerequisiteStatus,
    envelope_status: PrerequisiteStatus,
    safety_override_requested: bool = False,
) -> PrimaryReturnDisposition:
    """Preserve non-binary return conditions; an override never restores primary."""

    if safety_override_requested:
        return PrimaryReturnDisposition.BLOCKED_SAFETY_OVERRIDE
    statuses = (
        root_cause_status,
        revalidation_status,
        authority_status,
        envelope_status,
    )
    if not all(isinstance(status, PrerequisiteStatus) for status in statuses):
        return PrimaryReturnDisposition.BLOCKED_UNKNOWN
    if PrerequisiteStatus.STALE in statuses:
        return PrimaryReturnDisposition.BLOCKED_STALE
    if PrerequisiteStatus.RESOURCE_UNKNOWN in statuses:
        return PrimaryReturnDisposition.BLOCKED_RESOURCE_UNKNOWN
    if PrerequisiteStatus.UNKNOWN in statuses:
        return PrimaryReturnDisposition.BLOCKED_UNKNOWN
    if PrerequisiteStatus.FAIL in statuses:
        return PrimaryReturnDisposition.BLOCKED_FAILED_PREREQUISITE
    return PrimaryReturnDisposition.ALLOWED


def _receipt(
    disposition: EH18Disposition,
    observed: Interval | None,
    recoverable: Interval | None,
    reachable: Interval | None,
    command: CommandDisposition,
    prerequisite_statuses: tuple[tuple[str, PrerequisiteStatus], ...] = (),
) -> EH18HandoffReceipt:
    eligible = disposition is EH18Disposition.ELIGIBLE_FOR_BOUNDED_SIMULATION
    if not eligible and command is CommandDisposition.ACCEPTED:
        command = CommandDisposition.BLOCKED_HANDOFF_PREREQUISITE
    return EH18HandoffReceipt(
        disposition=disposition,
        observed_state_interval=observed,
        recoverable_center_interval=recoverable,
        delayed_reachable_interval=reachable,
        command_disposition=command,
        minimum_risk_response_status=(
            MinimumRiskResponseStatus.NOT_REQUIRED_FOR_ELIGIBILITY
            if eligible
            else MinimumRiskResponseStatus.REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE
        ),
        prerequisite_statuses=prerequisite_statuses,
    )


def evaluate_handoff(request: EH18HandoffRequest) -> EH18HandoffReceipt:
    """Fail-closed pre-admission check for the bounded EH-18 simulation.

    The function intentionally does not return SAFE/PASS.  It checks whether a
    request is eligible to proceed to independent trajectory/timing/proof work.
    """

    if not _request_types_valid(request):
        return _receipt(
            EH18Disposition.MALFORMED,
            None,
            None,
            None,
            CommandDisposition.NOT_EVALUATED_MALFORMED,
        )

    command = accept_actuator_command(
        request.transfer_epoch,
        request.current_actuation_epoch,
        request.authority_status,
    )
    prerequisite_statuses = _prerequisite_statuses(request)
    nonnegative_profile_fields = (
        request.estimation_error,
        request.disturbance_abs_bound,
        request.primary_command_abs_bound,
        request.fallback_command_abs,
        request.sensor_age,
        request.monitor_phase,
        request.remaining_uncontrolled_delay,
    )
    if not all(_valid_nonnegative(value) for value in nonnegative_profile_fields):
        return _receipt(
            EH18Disposition.MALFORMED,
            None,
            None,
            None,
            command,
            prerequisite_statuses,
        )

    observed = Interval(
        request.estimated_level - request.estimation_error,
        request.estimated_level + request.estimation_error,
    )
    recoverable = takeover_recoverable_region(
        request.remaining_uncontrolled_delay,
        request.estimation_error,
    )
    reachable = reachable_interval_during_delay(
        request.estimated_level,
        request.estimation_error,
        request.remaining_uncontrolled_delay,
    )

    if request.transfer_epoch != request.current_actuation_epoch:
        return _receipt(
            EH18Disposition.STALE,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if any(status is PrerequisiteStatus.STALE for _, status in prerequisite_statuses):
        return _receipt(
            EH18Disposition.STALE,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if any(
        status is PrerequisiteStatus.RESOURCE_UNKNOWN
        for _, status in prerequisite_statuses
    ):
        return _receipt(
            EH18Disposition.RESOURCE_UNKNOWN,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if any(status is PrerequisiteStatus.UNKNOWN for _, status in prerequisite_statuses):
        return _receipt(
            EH18Disposition.OUTCOME_UNKNOWN,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if request.authority_status is PrerequisiteStatus.FAIL:
        return _receipt(
            EH18Disposition.BLOCKED_AUTHORITY,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if request.fallback_qualification_status is PrerequisiteStatus.FAIL:
        return _receipt(
            EH18Disposition.BLOCKED_FALLBACK_UNQUALIFIED,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if request.transfer_authentication_status is PrerequisiteStatus.FAIL:
        return _receipt(
            EH18Disposition.STATE_UNTRUSTED,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if request.actuator_trust_status is PrerequisiteStatus.FAIL:
        return _receipt(
            EH18Disposition.ACTUATOR_UNTRUSTED,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if request.dependency_status is PrerequisiteStatus.FAIL:
        return _receipt(
            EH18Disposition.BLOCKED_DEPENDENCY_INVALID,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if request.timing_evidence_status is PrerequisiteStatus.FAIL:
        return _receipt(
            EH18Disposition.BLOCKED_TIMING_EVIDENCE_INVALID,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if request.resource_status is PrerequisiteStatus.FAIL:
        return _receipt(
            EH18Disposition.BLOCKED_RESOURCE_INSUFFICIENT,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if (
        request.estimation_error > MAX_ESTIMATION_ERROR
        or request.disturbance_abs_bound > MAX_DISTURBANCE
        or request.primary_command_abs_bound > Decimal("1")
        or request.fallback_command_abs != Decimal("0.2")
        or request.actuator_lower_bound != Decimal("-1")
        or request.actuator_upper_bound != Decimal("1")
        or request.sensor_age > MAX_SENSOR_AGE
        or request.monitor_phase > MAX_MONITOR_PHASE
        or request.remaining_uncontrolled_delay > MAX_REMAINING_HANDOFF_DELAY
    ):
        return _receipt(
            EH18Disposition.ASSUMPTION_INVALID,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if not observed.contained_by(Interval(ZERO, TEN)):
        return _receipt(
            EH18Disposition.ASSURANCE_LOST,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if recoverable is None or not recoverable.contains(request.estimated_level):
        return _receipt(
            EH18Disposition.OUTSIDE_RECOVERABLE_REGION,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    if not reachable.contained_by(Interval(ZERO, TEN)):
        return _receipt(
            EH18Disposition.OUTSIDE_RECOVERABLE_REGION,
            observed,
            recoverable,
            reachable,
            command,
            prerequisite_statuses,
        )
    return _receipt(
        EH18Disposition.ELIGIBLE_FOR_BOUNDED_SIMULATION,
        observed,
        recoverable,
        reachable,
        command,
        prerequisite_statuses,
    )
