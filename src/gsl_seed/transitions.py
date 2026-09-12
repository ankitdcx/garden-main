from __future__ import annotations
from dataclasses import dataclass
from .model import Claim, ClaimStatus

class EpistemicTransitionError(ValueError):
    pass

@dataclass(frozen=True)
class TransitionEvidence:
    transition_kind: str
    evidence_refs: tuple[str, ...]
    scope: str | None = None

_ALLOWED = {
    (ClaimStatus.REPORTED, ClaimStatus.HYPOTHESIS),
    (ClaimStatus.HYPOTHESIS, ClaimStatus.PREDICTION),
    (ClaimStatus.HYPOTHESIS, ClaimStatus.SUPPORTED_WITH_SCOPE),
    (ClaimStatus.PREDICTION, ClaimStatus.SUPPORTED_WITH_SCOPE),
    (ClaimStatus.FORMAL_CONCLUSION, ClaimStatus.SUPPORTED_WITH_SCOPE),
    (ClaimStatus.EMPIRICAL_RESULT, ClaimStatus.SUPPORTED_WITH_SCOPE),
    (ClaimStatus.SUPPORTED_WITH_SCOPE, ClaimStatus.QUALIFIED_KNOWLEDGE),
}

def transition_claim(claim: Claim, target: ClaimStatus, evidence: TransitionEvidence) -> Claim:
    if not evidence.evidence_refs:
        raise EpistemicTransitionError("epistemic promotion requires explicit evidence refs")
    if (claim.status, target) not in _ALLOWED:
        raise EpistemicTransitionError(f"transition {claim.status.value}->{target.value} is not admitted by the seed profile")
    return Claim(
        id=claim.id,
        proposition=claim.proposition,
        status=target,
        context_ref=claim.context_ref,
        evidence_refs=tuple(dict.fromkeys((*claim.evidence_refs, *evidence.evidence_refs))),
        scope=evidence.scope if evidence.scope is not None else claim.scope,
    )
