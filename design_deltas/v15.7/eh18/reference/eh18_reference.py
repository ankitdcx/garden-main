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
    BLOCKED_HANDOFF_PREREQUISITE = "BLOCKED_HANDOFF_PREREQUISITE"
    NOT_EVALUATED_MALFORMED = "NOT_EVALUATED_MALFORMED"


class MinimumRiskResponseStatus(str, Enum):
    NOT_REQUIRED_FOR_ELIGIBILITY = "NOT_REQUIRED_FOR_ELIGIBILITY"
    REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE = (
        "REQUIRED_UNRESOLVED_DOMAIN_SAFETY_CASE"
    )


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
    fresh_authority: bool
    fallback_qualified: bool
    transfer_authenticated: bool
    actuator_trusted: bool
    dependency_roots_current: bool
    timing_evidence_complete: bool
    resource_bounds_known: bool


@dataclass(frozen=True)
class EH18HandoffReceipt:
    disposition: EH18Disposition
    observed_state_interval: Interval | None
    recoverable_center_interval: Interval | None
    delayed_reachable_interval: Interval | None
    command_disposition: CommandDisposition
    minimum_risk_response_status: MinimumRiskResponseStatus
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
    boolean_fields = (
        request.fresh_authority,
        request.fallback_qualified,
        request.transfer_authenticated,
        request.actuator_trusted,
        request.dependency_roots_current,
        request.timing_evidence_complete,
        request.resource_bounds_known,
    )
    epochs_are_ints = all(
        isinstance(value, int) and not isinstance(value, bool) and value >= 0
        for value in (request.transfer_epoch, request.current_actuation_epoch)
    )
    return (
        all(_valid_finite(value) for value in decimal_fields)
        and all(isinstance(value, bool) for value in boolean_fields)
        and epochs_are_ints
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
    authority_current: bool,
) -> CommandDisposition:
    """Fence old/future epochs and commands lacking current authority."""

    if command_epoch != current_actuation_epoch:
        return CommandDisposition.REJECTED_STALE_EPOCH
    if not authority_current:
        return CommandDisposition.REJECTED_AUTHORITY
    return CommandDisposition.ACCEPTED


def primary_return_allowed(
    *,
    root_cause_closed: bool,
    revalidated: bool,
    fresh_authority: bool,
    inside_valid_envelope: bool,
    safety_override_requested: bool = False,
) -> bool:
    """Require all EH-18 return conditions; an override never restores primary."""

    if safety_override_requested:
        return False
    return root_cause_closed and revalidated and fresh_authority and inside_valid_envelope


def _receipt(
    disposition: EH18Disposition,
    observed: Interval | None,
    recoverable: Interval | None,
    reachable: Interval | None,
    command: CommandDisposition,
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
        request.fresh_authority,
    )
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
        return _receipt(EH18Disposition.MALFORMED, None, None, None, command)

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
        return _receipt(EH18Disposition.STALE, observed, recoverable, reachable, command)
    if not request.fresh_authority:
        return _receipt(EH18Disposition.BLOCKED_AUTHORITY, observed, recoverable, reachable, command)
    if not request.dependency_roots_current or not request.timing_evidence_complete:
        return _receipt(EH18Disposition.OUTCOME_UNKNOWN, observed, recoverable, reachable, command)
    if not request.resource_bounds_known:
        return _receipt(EH18Disposition.RESOURCE_UNKNOWN, observed, recoverable, reachable, command)
    if not request.fallback_qualified:
        return _receipt(
            EH18Disposition.BLOCKED_FALLBACK_UNQUALIFIED,
            observed,
            recoverable,
            reachable,
            command,
        )
    if not request.transfer_authenticated:
        return _receipt(EH18Disposition.STATE_UNTRUSTED, observed, recoverable, reachable, command)
    if not request.actuator_trusted:
        return _receipt(EH18Disposition.ACTUATOR_UNTRUSTED, observed, recoverable, reachable, command)
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
        return _receipt(EH18Disposition.ASSUMPTION_INVALID, observed, recoverable, reachable, command)
    if not observed.contained_by(Interval(ZERO, TEN)):
        return _receipt(EH18Disposition.ASSURANCE_LOST, observed, recoverable, reachable, command)
    if recoverable is None or not recoverable.contains(request.estimated_level):
        return _receipt(
            EH18Disposition.OUTSIDE_RECOVERABLE_REGION,
            observed,
            recoverable,
            reachable,
            command,
        )
    if not reachable.contained_by(Interval(ZERO, TEN)):
        return _receipt(
            EH18Disposition.OUTSIDE_RECOVERABLE_REGION,
            observed,
            recoverable,
            reachable,
            command,
        )
    return _receipt(
        EH18Disposition.ELIGIBLE_FOR_BOUNDED_SIMULATION,
        observed,
        recoverable,
        reachable,
        command,
    )
