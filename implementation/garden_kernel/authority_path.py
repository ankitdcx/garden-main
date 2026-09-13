from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from typing import Iterable

from .core import SemanticError


@dataclass(frozen=True)
class AuthorityScope:
    subject: str
    actions: frozenset[str]
    resources: frozenset[str]
    source_ref: str

    def __post_init__(self) -> None:
        if not self.subject.strip() or not self.source_ref.strip():
            raise SemanticError("AuthorityScope requires subject and source_ref")


@dataclass(frozen=True)
class AuthorityProvenanceChain:
    chain_id: str
    controlling_scopes: tuple[AuthorityScope, ...]
    provenance_refs: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.chain_id.strip():
            raise SemanticError("authority provenance chain_id is required")
        if not self.controlling_scopes:
            raise SemanticError("authority provenance chain requires controlling scopes")
        if not self.provenance_refs:
            raise SemanticError("authority provenance chain requires provenance")


@dataclass(frozen=True)
class ActionEligibleArtifact:
    artifact_id: str
    target_action: str
    target_resource: str
    authority_chain: AuthorityProvenanceChain

    def __post_init__(self) -> None:
        if not self.artifact_id or not self.target_action or not self.target_resource:
            raise SemanticError("action-eligible artifact requires id/action/resource")


def intersect_authority(scopes: Iterable[AuthorityScope]) -> AuthorityScope:
    items = tuple(scopes)
    if not items:
        raise SemanticError("authority intersection requires at least one scope")
    return AuthorityScope(
        subject="intersection:" + "->".join(item.subject for item in items),
        actions=reduce(frozenset.intersection, (item.actions for item in items)),
        resources=reduce(frozenset.intersection, (item.resources for item in items)),
        source_ref="intersection:" + "->".join(item.source_ref for item in items),
    )


def effective_authority_for_artifact_trigger(
    *,
    acting_scope: AuthorityScope,
    artifact: ActionEligibleArtifact,
) -> AuthorityScope:
    """Compose direct actor authority with all shared-state controlling authority.

    Reading an action-eligible artifact does not reset the authority chain. The
    action is bounded by the intersection of the actor and every authority scope
    that causally controls the artifact's action eligibility.
    """
    return intersect_authority((acting_scope, *artifact.authority_chain.controlling_scopes))


def authorize_artifact_trigger(
    *,
    acting_scope: AuthorityScope,
    artifact: ActionEligibleArtifact,
) -> bool:
    effective = effective_authority_for_artifact_trigger(
        acting_scope=acting_scope,
        artifact=artifact,
    )
    return (
        artifact.target_action in effective.actions
        and artifact.target_resource in effective.resources
    )


def require_artifact_trigger_authority(
    *,
    acting_scope: AuthorityScope,
    artifact: ActionEligibleArtifact,
) -> AuthorityScope:
    effective = effective_authority_for_artifact_trigger(
        acting_scope=acting_scope,
        artifact=artifact,
    )
    if artifact.target_action not in effective.actions:
        raise SemanticError("shared-state authority composition denies target action")
    if artifact.target_resource not in effective.resources:
        raise SemanticError("shared-state authority composition denies target resource")
    return effective
