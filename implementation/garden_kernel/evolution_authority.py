from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import reduce
from typing import Iterable

from .core import SemanticError
from .evolution_actions import EvolutionVerb


class EvolutionAgentRole(str, Enum):
    REVIEWER = "REVIEWER"
    TEST_WRITER = "TEST_WRITER"
    INTEGRATOR = "INTEGRATOR"
    ACCUMULATOR = "ACCUMULATOR"
    MATERIALIZER = "MATERIALIZER"


ROLE_ACTIONS: dict[EvolutionAgentRole, frozenset[EvolutionVerb]] = {
    EvolutionAgentRole.REVIEWER: frozenset({EvolutionVerb.PROPOSE}),
    EvolutionAgentRole.TEST_WRITER: frozenset({EvolutionVerb.TEST}),
    EvolutionAgentRole.INTEGRATOR: frozenset({EvolutionVerb.TRIAGE}),
    EvolutionAgentRole.ACCUMULATOR: frozenset({EvolutionVerb.ACCUMULATE}),
    EvolutionAgentRole.MATERIALIZER: frozenset({EvolutionVerb.MATERIALIZE}),
}


@dataclass(frozen=True)
class EvolutionAuthorityEnvelope:
    subject: str
    role: EvolutionAgentRole
    granted_by: str
    actions: frozenset[EvolutionVerb]
    resources: frozenset[str]
    max_delegation_depth: int
    can_mint_envelopes: bool = False
    can_promote_canon: bool = False

    def __post_init__(self) -> None:
        if not self.subject.strip() or not self.granted_by.strip():
            raise SemanticError("authority envelope requires subject and grantor")
        if self.max_delegation_depth < 0:
            raise SemanticError("max_delegation_depth cannot be negative")
        allowed = ROLE_ACTIONS[self.role]
        if not self.actions <= allowed:
            raise SemanticError("role envelope cannot exceed role action profile")
        if self.subject.startswith("agent:") and self.granted_by == self.subject:
            raise SemanticError("agent cannot mint its own authority envelope")
        if self.can_mint_envelopes:
            raise SemanticError("evolution agents cannot mint authority envelopes")
        if self.can_promote_canon:
            raise SemanticError("evolution agents cannot hold canonical-promotion authority")


def make_role_envelope(*, subject: str, role: EvolutionAgentRole, granted_by: str, resources: Iterable[str], max_delegation_depth: int = 0) -> EvolutionAuthorityEnvelope:
    return EvolutionAuthorityEnvelope(
        subject=subject,
        role=role,
        granted_by=granted_by,
        actions=ROLE_ACTIONS[role],
        resources=frozenset(resources),
        max_delegation_depth=max_delegation_depth,
    )


def compose_authority(envelopes: Iterable[EvolutionAuthorityEnvelope]) -> EvolutionAuthorityEnvelope:
    items = tuple(envelopes)
    if not items:
        raise SemanticError("at least one authority envelope is required")
    roles = {item.role for item in items}
    if len(roles) != 1:
        raise SemanticError("authority composition requires one role profile")
    return EvolutionAuthorityEnvelope(
        subject="composition:" + "->".join(item.subject for item in items),
        role=items[0].role,
        granted_by="intersection:" + "->".join(item.granted_by for item in items),
        actions=reduce(frozenset.intersection, (item.actions for item in items)),
        resources=reduce(frozenset.intersection, (item.resources for item in items)),
        max_delegation_depth=min(item.max_delegation_depth for item in items),
    )


def can_execute(envelopes: Iterable[EvolutionAuthorityEnvelope], *, verb: EvolutionVerb, resource: str, depth: int = 0) -> bool:
    effective = compose_authority(envelopes)
    return (
        verb in effective.actions
        and resource in effective.resources
        and depth <= effective.max_delegation_depth
    )


def delegate_within_envelope(parent: EvolutionAuthorityEnvelope, *, child_subject: str, requested_actions: frozenset[EvolutionVerb], requested_resources: frozenset[str]) -> EvolutionAuthorityEnvelope:
    if parent.max_delegation_depth <= 0:
        raise SemanticError("parent envelope does not permit delegation")
    if not requested_actions <= parent.actions:
        raise SemanticError("delegation cannot expand action authority")
    if not requested_resources <= parent.resources:
        raise SemanticError("delegation cannot expand resource authority")
    return EvolutionAuthorityEnvelope(
        subject=child_subject,
        role=parent.role,
        granted_by=parent.subject,
        actions=requested_actions,
        resources=requested_resources,
        max_delegation_depth=parent.max_delegation_depth - 1,
    )
