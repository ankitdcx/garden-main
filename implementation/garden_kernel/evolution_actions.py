from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping

from .core import SemanticError


class EvolutionVerb(str, Enum):
    """Typed Garden evolution-pipeline actions.

    These are application/profile actions over existing GSL ACTION semantics.
    They do not introduce a new top-level Garden engine or grant authority.
    """

    PROPOSE = "PROPOSE"
    TRIAGE = "TRIAGE"
    TEST = "TEST"
    ACCUMULATE = "ACCUMULATE"
    MATERIALIZE = "MATERIALIZE"


class Condition(str, Enum):
    ACTOR_IDENTIFIED = "ACTOR_IDENTIFIED"
    SUBJECT_IDENTIFIED = "SUBJECT_IDENTIFIED"
    PROVENANCE_PRESENT = "PROVENANCE_PRESENT"
    INPUT_REFS_TYPED = "INPUT_REFS_TYPED"
    PROPOSAL_EXISTS = "PROPOSAL_EXISTS"
    EVIDENCE_AVAILABLE = "EVIDENCE_AVAILABLE"
    TRIAGE_DISPOSITION_EXISTS = "TRIAGE_DISPOSITION_EXISTS"
    TEST_TARGET_EXISTS = "TEST_TARGET_EXISTS"
    TEST_SPEC_EXISTS = "TEST_SPEC_EXISTS"
    ADMISSION_EVIDENCE_EXISTS = "ADMISSION_EVIDENCE_EXISTS"
    DEPENDENCIES_EXPLICIT = "DEPENDENCIES_EXPLICIT"
    ACCUMULATED_DELTA_SET_EXISTS = "ACCUMULATED_DELTA_SET_EXISTS"
    CONSISTENCY_CHECK_EXISTS = "CONSISTENCY_CHECK_EXISTS"
    PREDECESSOR_IDENTITY_PINNED = "PREDECESSOR_IDENTITY_PINNED"
    SUCCESSOR_TARGET_DECLARED = "SUCCESSOR_TARGET_DECLARED"

    CANDIDATE_RECORDED = "CANDIDATE_RECORDED"
    DISPOSITION_RECORDED = "DISPOSITION_RECORDED"
    RATIONALE_RECORDED = "RATIONALE_RECORDED"
    TEST_RECEIPT_RECORDED = "TEST_RECEIPT_RECORDED"
    DELTA_ACCUMULATED = "DELTA_ACCUMULATED"
    SUCCESSOR_CANDIDATE_COMPLETE = "SUCCESSOR_CANDIDATE_COMPLETE"
    PREDECESSOR_UNCHANGED = "PREDECESSOR_UNCHANGED"
    CANONICAL_POINTER_UNCHANGED = "CANONICAL_POINTER_UNCHANGED"
    NO_AUTHORITY_EXPANSION = "NO_AUTHORITY_EXPANSION"


@dataclass(frozen=True)
class EvolutionActionContract:
    verb: EvolutionVerb
    preconditions: frozenset[Condition]
    postconditions: frozenset[Condition]
    description: str


CONTRACTS: Mapping[EvolutionVerb, EvolutionActionContract] = {
    EvolutionVerb.PROPOSE: EvolutionActionContract(
        verb=EvolutionVerb.PROPOSE,
        preconditions=frozenset({
            Condition.ACTOR_IDENTIFIED,
            Condition.SUBJECT_IDENTIFIED,
            Condition.PROVENANCE_PRESENT,
            Condition.INPUT_REFS_TYPED,
        }),
        postconditions=frozenset({
            Condition.CANDIDATE_RECORDED,
            Condition.NO_AUTHORITY_EXPANSION,
            Condition.CANONICAL_POINTER_UNCHANGED,
        }),
        description="Create a proposal candidate only; proposal does not itself admit, authorize, or promote it.",
    ),
    EvolutionVerb.TRIAGE: EvolutionActionContract(
        verb=EvolutionVerb.TRIAGE,
        preconditions=frozenset({
            Condition.ACTOR_IDENTIFIED,
            Condition.PROPOSAL_EXISTS,
            Condition.EVIDENCE_AVAILABLE,
            Condition.PROVENANCE_PRESENT,
        }),
        postconditions=frozenset({
            Condition.DISPOSITION_RECORDED,
            Condition.RATIONALE_RECORDED,
            Condition.NO_AUTHORITY_EXPANSION,
            Condition.CANONICAL_POINTER_UNCHANGED,
        }),
        description="Classify/disposition a proposal with reasons; triage is not canonical promotion.",
    ),
    EvolutionVerb.TEST: EvolutionActionContract(
        verb=EvolutionVerb.TEST,
        preconditions=frozenset({
            Condition.ACTOR_IDENTIFIED,
            Condition.TEST_TARGET_EXISTS,
            Condition.TEST_SPEC_EXISTS,
            Condition.PROVENANCE_PRESENT,
        }),
        postconditions=frozenset({
            Condition.TEST_RECEIPT_RECORDED,
            Condition.CANONICAL_POINTER_UNCHANGED,
        }),
        description="Execute or record a bounded test against an explicit target/spec and produce a receipt.",
    ),
    EvolutionVerb.ACCUMULATE: EvolutionActionContract(
        verb=EvolutionVerb.ACCUMULATE,
        preconditions=frozenset({
            Condition.ACTOR_IDENTIFIED,
            Condition.TRIAGE_DISPOSITION_EXISTS,
            Condition.ADMISSION_EVIDENCE_EXISTS,
            Condition.DEPENDENCIES_EXPLICIT,
            Condition.PROVENANCE_PRESENT,
        }),
        postconditions=frozenset({
            Condition.DELTA_ACCUMULATED,
            Condition.NO_AUTHORITY_EXPANSION,
            Condition.CANONICAL_POINTER_UNCHANGED,
        }),
        description="Add an admitted delta candidate to the successor accumulator without changing canon.",
    ),
    EvolutionVerb.MATERIALIZE: EvolutionActionContract(
        verb=EvolutionVerb.MATERIALIZE,
        preconditions=frozenset({
            Condition.ACTOR_IDENTIFIED,
            Condition.ACCUMULATED_DELTA_SET_EXISTS,
            Condition.CONSISTENCY_CHECK_EXISTS,
            Condition.PREDECESSOR_IDENTITY_PINNED,
            Condition.SUCCESSOR_TARGET_DECLARED,
            Condition.PROVENANCE_PRESENT,
        }),
        postconditions=frozenset({
            Condition.SUCCESSOR_CANDIDATE_COMPLETE,
            Condition.PREDECESSOR_UNCHANGED,
            Condition.CANONICAL_POINTER_UNCHANGED,
            Condition.NO_AUTHORITY_EXPANSION,
        }),
        description="Materialize a complete successor candidate; canonical promotion remains a separate human-authorized act.",
    ),
}


@dataclass(frozen=True)
class EvolutionAction:
    action_id: str
    verb: EvolutionVerb
    actor_ref: str
    subject_ref: str
    input_refs: tuple[str, ...]
    provenance_refs: tuple[str, ...]
    satisfied_preconditions: frozenset[Condition]
    claimed_postconditions: frozenset[Condition]

    def __post_init__(self) -> None:
        if not self.action_id.strip():
            raise SemanticError("EvolutionAction.action_id is required")
        if not self.actor_ref.strip():
            raise SemanticError("EvolutionAction.actor_ref is required")
        if not self.subject_ref.strip():
            raise SemanticError("EvolutionAction.subject_ref is required")
        if not self.provenance_refs:
            raise SemanticError("EvolutionAction.provenance_refs must be non-empty")


def contract_for(verb: EvolutionVerb) -> EvolutionActionContract:
    try:
        return CONTRACTS[verb]
    except KeyError as exc:
        raise SemanticError(f"unsupported evolution verb: {verb!r}") from exc


def validate_action_shape(action: EvolutionAction) -> None:
    """Validate Step-1 typing only.

    This does not evaluate authority, DesignEpoch freshness, or ActionGate policy.
    Those are deliberately reserved for Steps 2–4 of WP-007.
    """

    contract = contract_for(action.verb)
    missing_pre = contract.preconditions - action.satisfied_preconditions
    missing_post = contract.postconditions - action.claimed_postconditions
    if missing_pre:
        raise SemanticError(
            f"{action.verb.value} missing preconditions: "
            f"{sorted(x.value for x in missing_pre)}"
        )
    if missing_post:
        raise SemanticError(
            f"{action.verb.value} missing postconditions: "
            f"{sorted(x.value for x in missing_post)}"
        )
