from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .core import SemanticError


class SanityGateResult(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"


class ReasonMode(str, Enum):
    R1_LOCAL = "R1"
    R2_STRUCTURED = "R2"
    R3_DEEP = "R3"
    R4_SOVEREIGN = "R4"


@dataclass(frozen=True)
class TransitionSanityInput:
    transition_ref: str
    declared_abstraction: str
    input_type: str
    output_type: str
    scope_ref: str
    obvious_contradiction: bool | None = None
    admissibility_known: bool = True

    def __post_init__(self) -> None:
        if not all(
            value.strip()
            for value in (
                self.transition_ref,
                self.declared_abstraction,
                self.input_type,
                self.output_type,
                self.scope_ref,
            )
        ):
            raise SemanticError("SanityGate input requires transition/type/scope/abstraction")


def evaluate_transition_sanity(value: TransitionSanityInput) -> SanityGateResult:
    """R0 base case: deterministic gate, not a recursive Engine.Reason mode."""
    if value.obvious_contradiction is True:
        return SanityGateResult.FAIL
    if value.obvious_contradiction is None or not value.admissibility_known:
        return SanityGateResult.UNKNOWN
    return SanityGateResult.PASS


def parse_reason_mode(tier: str) -> ReasonMode:
    if tier == "R0":
        raise SemanticError("R0_IS_SANITY_GATE_NOT_REASON_MODE")
    try:
        return ReasonMode(tier)
    except ValueError as exc:
        raise SemanticError(f"unknown Reason mode: {tier}") from exc
