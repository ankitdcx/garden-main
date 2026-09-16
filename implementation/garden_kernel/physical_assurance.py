"""Bounded, deterministic tank-continuity simulation; never interfaces with hardware."""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hmac
import math
from typing import Any


def _finite(value: float, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number")
    return float(value)


@dataclass(frozen=True)
class TankAssumptions:
    """All quantities are SI: level in m and time in s."""
    safe_low: float = 0.0
    safe_high: float = 10.0
    actuator_limit: float = 1.0
    disturbance_limit: float = 0.1
    fallback_magnitude: float = 0.2
    sensor_error_bound: float = 0.05
    sensor_age_bound: float = 0.10
    monitor_period: float = 0.10
    handoff_delay_bound: float = 0.20
    dt: float = 0.01
    max_duration_s: float = 60.0
    transfer_key: str = "bounded-simulation-key-not-a-production-secret"

    def __post_init__(self) -> None:
        for name in ("safe_low", "safe_high", "actuator_limit", "disturbance_limit", "fallback_magnitude", "sensor_error_bound", "sensor_age_bound", "monitor_period", "handoff_delay_bound", "dt", "max_duration_s"):
            _finite(getattr(self, name), name)
        if self.safe_low >= self.safe_high or min(self.actuator_limit, self.disturbance_limit, self.fallback_magnitude, self.sensor_error_bound, self.sensor_age_bound, self.monitor_period, self.handoff_delay_bound) < 0 or self.dt <= 0 or self.max_duration_s <= 0:
            raise ValueError("invalid tank envelope, non-negative bounds, or integration step")
        if self.fallback_magnitude > self.actuator_limit:
            raise ValueError("fallback magnitude exceeds actuator limit")
        if self.dt > self.monitor_period or any(abs((value / self.dt) - round(value / self.dt)) > 1e-12 for value in (self.monitor_period, self.handoff_delay_bound)):
            raise ValueError("dt must divide monitor_period and handoff_delay_bound without exceeding monitor_period")
        if not isinstance(self.transfer_key, str) or not self.transfer_key:
            raise ValueError("transfer_key must be a non-empty string")

    @property
    def worst_outward_speed(self) -> float:
        return self.actuator_limit + self.disturbance_limit

    @property
    def intervention_margin(self) -> float:
        return self.sensor_error_bound + self.worst_outward_speed * (
            self.sensor_age_bound + self.monitor_period + self.handoff_delay_bound
        )

    @property
    def lower_switch_threshold(self) -> float:
        return self.safe_low + self.intervention_margin

    @property
    def upper_switch_threshold(self) -> float:
        return self.safe_high - self.intervention_margin


@dataclass(frozen=True)
class Transfer:
    controller: str
    epoch: int
    observed_level: float
    observed_at: float
    mac: str


def _mac(controller: str, epoch: int, level: float, observed_at: float, key: str) -> str:
    if not isinstance(controller, str) or not controller or isinstance(epoch, bool) or not isinstance(epoch, int) or epoch < 0:
        raise ValueError("controller and epoch are invalid")
    _finite(level, "level"); _finite(observed_at, "observed_at")
    message = f"{controller}|{epoch}|{level:.9f}|{observed_at:.9f}".encode()
    return hmac.new(key.encode(), message, "sha256").hexdigest()


def signed_transfer(controller: str, epoch: int, level: float, observed_at: float, assumptions: TankAssumptions) -> Transfer:
    return Transfer(controller, epoch, level, observed_at, _mac(controller, epoch, level, observed_at, assumptions.transfer_key))


def transfer_is_authenticated(transfer: Transfer, assumptions: TankAssumptions) -> bool:
    if not isinstance(transfer, Transfer) or not isinstance(transfer.mac, str):
        return False
    try:
        expected = _mac(transfer.controller, transfer.epoch, transfer.observed_level, transfer.observed_at, assumptions.transfer_key)
    except ValueError:
        return False
    return hmac.compare_digest(transfer.mac, expected)


def takeover_recoverable_region(remaining_delay: float, estimation_error: float, assumptions: TankAssumptions = TankAssumptions()) -> tuple[float, float] | None:
    """Return allowed estimate-center interval, or None when it is empty.

    The actual initial interval [h-e,h+e] must fit inside the region left
    after worst-case outward motion 1.1*D.
    """
    _finite(remaining_delay, "remaining_delay"); _finite(estimation_error, "estimation_error")
    if remaining_delay < 0 or estimation_error < 0:
        raise ValueError("delay and estimation error must be non-negative")
    lo = assumptions.safe_low + assumptions.worst_outward_speed * remaining_delay + estimation_error
    hi = assumptions.safe_high - assumptions.worst_outward_speed * remaining_delay - estimation_error
    return (lo, hi) if lo <= hi else None


def is_recoverable(estimate: float, remaining_delay: float, estimation_error: float, assumptions: TankAssumptions = TankAssumptions()) -> bool:
    region = takeover_recoverable_region(remaining_delay, estimation_error, assumptions)
    return region is not None and region[0] - 1e-12 <= estimate <= region[1] + 1e-12


STPA_UNSAFE_CONTROL_ACTIONS: dict[str, dict[str, str]] = {
    "UCA-1-missing-or-late-switch": {"constraint": "switch before bounded margin is consumed", "test": "test_late_handoff_records_assurance_loss"},
    "UCA-2-early-return": {"constraint": "return requires dwell, revalidation, and fresh authority", "test": "test_primary_return_requires_revalidation_and_fresh_authority"},
    "UCA-3-conflicting-commands": {"constraint": "one fenced epoch may command the actuator", "test": "test_two_agent_shared_actuator_hazard_is_blocked"},
    "UCA-4-incorrect-transfer": {"constraint": "handoff transfer must authenticate controller, epoch, level, and time", "test": "test_bad_transfer_is_rejected"},
    "UCA-5-stale-sensor-or-command": {"constraint": "old epoch commands are rejected at actuator boundary", "test": "test_stale_primary_command_is_fenced_after_handoff"},
    "UCA-6-unsafe-shutdown": {"constraint": "outside recoverable region enters minimum-risk mode with assurance loss", "test": "test_outside_recoverable_region_records_minimum_risk"},
    "UCA-7-two-agent-shared-actuator": {"constraint": "conflicting valid agents need coordinated exclusive allocation", "test": "test_two_agent_shared_actuator_hazard_is_blocked"},
}


class TankSimulation:
    """Euler-integrated reference model with an explicit actuator fence."""
    def __init__(self, *, initial_level: float, primary_command: float, disturbance: float, sensor_error: float = 0.0,
                 sensor_age: float = 0.10, handoff_delay: float = 0.20, controller_timeout: bool = False,
                 force_handoff_failure: bool = False, assumptions: TankAssumptions = TankAssumptions()):
        if not isinstance(assumptions, TankAssumptions):
            raise ValueError("assumptions must be TankAssumptions")
        self.a = assumptions
        for name, value in (("initial_level", initial_level), ("primary_command", primary_command), ("disturbance", disturbance), ("sensor_error", sensor_error), ("sensor_age", sensor_age), ("handoff_delay", handoff_delay)):
            _finite(value, name)
        if sensor_age < 0 or handoff_delay < 0 or abs((handoff_delay / self.a.dt) - round(handoff_delay / self.a.dt)) > 1e-12 or abs(primary_command) > self.a.actuator_limit or abs(disturbance) > self.a.disturbance_limit or abs(sensor_error) > self.a.sensor_error_bound:
            raise ValueError("input exceeds declared bounded assumptions")
        if not isinstance(controller_timeout, bool) or not isinstance(force_handoff_failure, bool):
            raise ValueError("fault injections must be booleans")
        self.h, self.primary_command, self.disturbance = initial_level, primary_command, disturbance
        self.sensor_error, self.sensor_age, self.handoff_delay = sensor_error, sensor_age, handoff_delay
        self.controller_timeout, self.force_handoff_failure = controller_timeout, force_handoff_failure
        self.time, self.epoch, self.active, self.handoff_at, self.next_monitor_at, self.fallback_entered_at = 0.0, 0, "primary", None, 0.0, None
        self.assurance_loss: list[str] = []
        self.events: list[dict[str, Any]] = []
        self.trajectory: list[dict[str, Any]] = []
        self.rejected_commands: list[dict[str, Any]] = []

    def actuator_command(self, controller: str, epoch: int, command: float) -> bool:
        accepted = isinstance(controller, str) and isinstance(epoch, int) and not isinstance(epoch, bool) and isinstance(command, (int, float)) and not isinstance(command, bool) and math.isfinite(command) and epoch == self.epoch and controller == self.active and abs(command) <= self.a.actuator_limit
        record = {"time_s": round(self.time, 4), "controller": controller, "epoch": epoch, "command": command, "accepted": accepted}
        if not accepted:
            self.rejected_commands.append(record)
        return accepted

    def _fallback_command(self) -> float:
        midpoint = (self.a.safe_low + self.a.safe_high) / 2
        return self.a.fallback_magnitude if self.h <= midpoint else -self.a.fallback_magnitude

    def _start_handoff(self) -> None:
        measured = self.h + self.sensor_error
        transfer = signed_transfer("primary", self.epoch, measured, self.time - self.sensor_age, self.a)
        if not transfer_is_authenticated(transfer, self.a):  # defensive; tests exercise a bad transfer directly
            self.assurance_loss.append("STATE_UNTRUSTED")
            return
        self.handoff_at = self.time + self.handoff_delay
        # A requested delay outside the profile is already an assumption breach;
        # it remains visible even if the plant leaves the envelope before takeover.
        if self.handoff_delay > self.a.handoff_delay_bound:
            self.assurance_loss.append("LATE_HANDOFF")
        self.events.append({"event": "handoff_requested", "time_s": round(self.time, 4), "measured_level_m": measured, "epoch": self.epoch})

    def _complete_handoff(self) -> None:
        self.handoff_at = None
        if self.force_handoff_failure:
            self._minimum_risk("HANDOFF_FAILED")
            return
        self.epoch += 1
        self.active = "fallback"
        self.fallback_entered_at = self.time
        if self.handoff_delay > self.a.handoff_delay_bound and "LATE_HANDOFF" not in self.assurance_loss:
            self.assurance_loss.append("LATE_HANDOFF")
        self.events.append({"event": "handoff_completed", "time_s": round(self.time, 4), "epoch": self.epoch})

    def _minimum_risk(self, reason: str) -> None:
        if reason not in self.assurance_loss:
            self.assurance_loss.append(reason)
        if self.active != "fallback":
            self.active, self.epoch, self.handoff_at, self.fallback_entered_at = "fallback", self.epoch + 1, None, self.time
            self.events.append({"event": "minimum_risk_fallback", "time_s": round(self.time, 4), "reason": reason, "epoch": self.epoch})

    def run(self, duration: float, *, inject_stale_primary: bool = True) -> dict[str, Any]:
        _finite(duration, "duration")
        if duration < 0 or duration > self.a.max_duration_s:
            raise ValueError("duration exceeds declared bounded simulation horizon")
        if self.sensor_age > self.a.sensor_age_bound:
            self._minimum_risk("SENSOR_AGE_EXCEEDS_BOUND")
        elif self.controller_timeout and self.active == "primary":
            self._minimum_risk("CONTROLLER_TIMEOUT")
        elif not is_recoverable(self.h + self.sensor_error, self.handoff_delay, self.a.sensor_error_bound, self.a):
            self._minimum_risk("OUTSIDE_RECOVERABLE_REGION")
        remaining = duration
        while True:
            if self.active == "primary" and self.handoff_at is None and self.time + 1e-12 >= self.next_monitor_at:
                measured = self.h + self.sensor_error
                if measured <= self.a.lower_switch_threshold or measured >= self.a.upper_switch_threshold:
                    self._start_handoff()
                self.next_monitor_at += self.a.monitor_period
            if self.handoff_at is not None and self.time + 1e-12 >= self.handoff_at and self.active == "primary":
                self._complete_handoff()
            if inject_stale_primary and self.active == "fallback":
                self.actuator_command("primary", self.epoch - 1, self.primary_command)
            command = self.primary_command if self.active == "primary" else self._fallback_command()
            self.actuator_command(self.active, self.epoch, command)
            self.trajectory.append({"time_s": round(self.time, 4), "level_m": self.h, "controller": self.active, "epoch": self.epoch, "command_m_per_s": command, "disturbance_m_per_s": self.disturbance})
            if self.h < self.a.safe_low or self.h > self.a.safe_high:
                self._minimum_risk("SAFE_ENVELOPE_VIOLATED")
            if remaining <= 1e-12:
                break
            interval = min(self.a.dt, remaining)
            self.h += interval * (command + self.disturbance)
            self.time += interval
            remaining -= interval
        return self.receipt()

    def request_primary_return(self, *, revalidated: bool, fresh_authorization: bool, dwell_s: float) -> bool:
        _finite(dwell_s, "dwell_s")
        state_recoverable = is_recoverable(self.h + self.sensor_error, 0.0, self.a.sensor_error_bound, self.a)
        actual_dwell = -math.inf if self.fallback_entered_at is None else self.time - self.fallback_entered_at
        if self.active != "fallback" or not isinstance(revalidated, bool) or not isinstance(fresh_authorization, bool) or not revalidated or not fresh_authorization or dwell_s < self.a.handoff_delay_bound or actual_dwell + 1e-12 < self.a.handoff_delay_bound or actual_dwell + 1e-12 < dwell_s or not state_recoverable:
            self.events.append({"event": "primary_return_blocked", "time_s": round(self.time, 4)})
            return False
        self.epoch += 1
        self.active = "primary"
        self.events.append({"event": "primary_return_authorized", "time_s": round(self.time, 4), "epoch": self.epoch})
        return True

    def receipt(self) -> dict[str, Any]:
        levels = [p["level_m"] for p in self.trajectory]
        assumptions = asdict(self.a)
        assumptions["transfer_key"] = "REDACTED_SIMULATION_TOKEN"
        return {"kind": "BOUNDED_REFERENCE_SIMULATION_NOT_HARDWARE", "assumptions": assumptions, "derived": {"worst_outward_speed_m_per_s": self.a.worst_outward_speed, "intervention_margin_m": self.a.intervention_margin, "switch_thresholds_measured_m": [self.a.lower_switch_threshold, self.a.upper_switch_threshold]}, "events": self.events, "trajectory": self.trajectory, "safety_result": {"envelope_held_at_sampled_points": not any(x == "SAFE_ENVELOPE_VIOLATED" for x in self.assurance_loss), "minimum_level_m": min(levels), "maximum_level_m": max(levels), "assurance_loss": self.assurance_loss, "rejected_stale_commands": len(self.rejected_commands), "recorded_horizon_end_s": round(self.time, 12)}, "limitations": ["Euler reference integration, not a continuous-time proof", "No physical actuation or hardware independence claim", "Authenticated transfer uses HMAC-SHA-256 only as a deterministic simulation token, not production key management or cryptography"]}


def shared_actuator_decision(agent_a: tuple[str, int, float], agent_b: tuple[str, int, float], *, actuator_limit: float = 1.0, trusted_coordination: bool = False) -> dict[str, Any]:
    """Fail closed: equality is not coordination without an explicit trusted fixture."""
    valid_limit = isinstance(actuator_limit, (int, float)) and not isinstance(actuator_limit, bool) and math.isfinite(actuator_limit) and actuator_limit > 0
    def valid(proposal: Any) -> bool:
        return isinstance(proposal, tuple) and len(proposal) == 3 and isinstance(proposal[0], str) and bool(proposal[0]) and isinstance(proposal[1], int) and not isinstance(proposal[1], bool) and proposal[1] >= 0 and isinstance(proposal[2], (int, float)) and not isinstance(proposal[2], bool) and math.isfinite(proposal[2]) and valid_limit and abs(proposal[2]) <= actuator_limit
    agents = [agent_a[0] if isinstance(agent_a, tuple) and agent_a else "MALFORMED", agent_b[0] if isinstance(agent_b, tuple) and agent_b else "MALFORMED"]
    if not valid(agent_a) or not valid(agent_b) or not isinstance(trusted_coordination, bool):
        return {"accepted": False, "reason": "MALFORMED_OR_OUT_OF_BOUND_PROPOSAL", "agents": agents}
    if not trusted_coordination:
        return {"accepted": False, "reason": "COORDINATION_NOT_ESTABLISHED", "agents": agents}
    if agent_a[1] != agent_b[1] or agent_a[2] != agent_b[2]:
        return {"accepted": False, "reason": "CONFLICTING_SHARED_ACTUATOR_COMMANDS", "agents": agents}
    return {"accepted": True, "reason": "TRUSTED_IDENTICAL_COORDINATED_COMMAND", "agents": agents}
