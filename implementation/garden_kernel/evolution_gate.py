from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping

from .core import SemanticError
from .evolution_actions import EvolutionAction, EvolutionVerb, validate_action_shape
from .evolution_authority import EvolutionAuthorityEnvelope, can_execute
from .evolution_epoch import EvolutionArtifactBinding, require_current_for_accumulation


class GateDecision(str, Enum):
    ALLOW = "ALLOW"
    REJECT = "REJECT"
    ESCALATE = "ESCALATE"


@dataclass(frozen=True)
class EvolutionGateContext:
    current_design_epoch: str
    current_dependencies: Mapping[str, str]
    authority_envelopes: tuple[EvolutionAuthorityEnvelope, ...]
    bound_inputs: tuple[EvolutionArtifactBinding, ...] = ()
    independent_review: bool = False
    human_signoff: bool = False


@dataclass(frozen=True)
class EvolutionGateReceipt:
    action_id: str
    verb: EvolutionVerb
    decision: GateDecision
    reasons: tuple[str, ...]
    design_epoch: str


def evaluate_evolution_action(action: EvolutionAction, context: EvolutionGateContext) -> EvolutionGateReceipt:
    reasons: list[str] = []

    try:
        validate_action_shape(action)
    except SemanticError as exc:
        return EvolutionGateReceipt(
            action.action_id, action.verb, GateDecision.REJECT,
            (f"ACTION_SHAPE_INVALID:{exc}",), context.current_design_epoch,
        )

    if not context.authority_envelopes:
        return EvolutionGateReceipt(
            action.action_id, action.verb, GateDecision.ESCALATE,
            ("AUTHORITY_ENVELOPE_UNKNOWN",), context.current_design_epoch,
        )

    if not can_execute(
        context.authority_envelopes,
        verb=action.verb,
        resource=action.subject_ref,
    ):
        return EvolutionGateReceipt(
            action.action_id, action.verb, GateDecision.REJECT,
            ("AUTHORITY_SCOPE_DENIED",), context.current_design_epoch,
        )

    if action.verb in {EvolutionVerb.ACCUMULATE, EvolutionVerb.MATERIALIZE}:
        try:
            require_current_for_accumulation(
                context.bound_inputs,
                current_design_epoch=context.current_design_epoch,
                current_dependencies=context.current_dependencies,
            )
        except SemanticError as exc:
            return EvolutionGateReceipt(
                action.action_id, action.verb, GateDecision.REJECT,
                (f"STALE_OR_UNKNOWN_INPUT:{exc}",), context.current_design_epoch,
            )

    if action.verb is EvolutionVerb.MATERIALIZE and not (
        context.independent_review or context.human_signoff
    ):
        return EvolutionGateReceipt(
            action.action_id, action.verb, GateDecision.ESCALATE,
            ("MATERIALIZATION_REQUIRES_INDEPENDENT_REVIEW_OR_HUMAN_SIGNOFF",),
            context.current_design_epoch,
        )

    reasons.append("ACTION_CONTRACT_PASS")
    reasons.append("AUTHORITY_PASS")
    if action.verb in {EvolutionVerb.ACCUMULATE, EvolutionVerb.MATERIALIZE}:
        reasons.append("EPOCH_BINDINGS_CURRENT")
    if action.verb is EvolutionVerb.MATERIALIZE:
        reasons.append("FRESH_REVIEW_OR_HUMAN_SIGNOFF_PRESENT")
    return EvolutionGateReceipt(
        action.action_id, action.verb, GateDecision.ALLOW,
        tuple(reasons), context.current_design_epoch,
    )
