from __future__ import annotations

from dataclasses import dataclass
import hashlib
from typing import Iterable

from .core import SemanticError


@dataclass(frozen=True)
class FrozenVerifierBinding:
    binding_id: str
    verifier_id: str
    verifier_version: str
    verifier_hash: str
    implementation_lineage: str
    test_corpus_root: str
    independent_from_submitter: bool

    def __post_init__(self) -> None:
        for name, value in (
            ("binding_id", self.binding_id),
            ("verifier_id", self.verifier_id),
            ("verifier_version", self.verifier_version),
            ("verifier_hash", self.verifier_hash),
            ("implementation_lineage", self.implementation_lineage),
            ("test_corpus_root", self.test_corpus_root),
        ):
            if not value.strip():
                raise SemanticError(f"{name} is required")
        if len(self.verifier_hash) != 64 or len(self.test_corpus_root) != 64:
            raise SemanticError("verifier_hash and test_corpus_root must be SHA-256 hex digests")
        if not self.independent_from_submitter:
            raise SemanticError("bootstrap frozen verifier must be independent from the submitter")


@dataclass(frozen=True)
class BootstrapTrustRootCeremonyReceipt:
    ceremony_id: str
    candidate_design_epoch: str
    candidate_source_root: str
    submitter_ref: str
    participant_refs: tuple[str, ...]
    witness_refs: tuple[str, ...]
    constitutional_authority_ref: str
    transcript_sha256: str
    frozen_verifiers: tuple[FrozenVerifierBinding, ...]
    result: str

    def __post_init__(self) -> None:
        required = {
            "ceremony_id": self.ceremony_id,
            "candidate_design_epoch": self.candidate_design_epoch,
            "candidate_source_root": self.candidate_source_root,
            "submitter_ref": self.submitter_ref,
            "constitutional_authority_ref": self.constitutional_authority_ref,
            "transcript_sha256": self.transcript_sha256,
        }
        for name, value in required.items():
            if not value.strip():
                raise SemanticError(f"{name} is required")
        if len(self.candidate_source_root) != 64 or len(self.transcript_sha256) != 64:
            raise SemanticError("source root and ceremony transcript must be SHA-256 digests")
        if self.result not in {"PASS", "FAIL", "INCONCLUSIVE", "UNKNOWN"}:
            raise SemanticError("unsupported bootstrap ceremony result")
        if not self.participant_refs:
            raise SemanticError("bootstrap ceremony requires identified participants")
        if len(set(self.participant_refs)) != len(self.participant_refs):
            raise SemanticError("bootstrap ceremony participants must be unique")
        if self.submitter_ref in self.participant_refs and len(self.participant_refs) == 1:
            raise SemanticError("submitter cannot be the sole bootstrap ceremony participant")
        if not self.witness_refs:
            raise SemanticError("bootstrap ceremony requires at least one external/independent witness")
        if not self.frozen_verifiers:
            raise SemanticError("bootstrap ceremony requires at least one frozen verifier binding")


def transcript_digest(transcript: bytes) -> str:
    return hashlib.sha256(transcript).hexdigest()


def require_first_epoch_acceptance(
    *,
    candidate_design_epoch: str,
    candidate_source_root: str,
    receipt: BootstrapTrustRootCeremonyReceipt | None,
) -> None:
    """Fail closed at the root DesignEpoch bootstrap boundary.

    This is a profile over Garden's existing TrustRootCeremony semantics. It does
    not allow a human-source document or the candidate verifier to self-issue an
    ACCEPTED first DesignEpoch.
    """
    if receipt is None:
        raise SemanticError(
            "first DesignEpoch remains SPECIFIED_DESIGNEPOCH_CANDIDATE until a bootstrap trust-root ceremony passes"
        )
    if receipt.result != "PASS":
        raise SemanticError("bootstrap trust-root ceremony did not PASS")
    if receipt.candidate_design_epoch != candidate_design_epoch:
        raise SemanticError("bootstrap ceremony DesignEpoch does not match candidate")
    if receipt.candidate_source_root != candidate_source_root:
        raise SemanticError("bootstrap ceremony source root does not match candidate")
    if not all(v.independent_from_submitter for v in receipt.frozen_verifiers):
        raise SemanticError("bootstrap ceremony includes non-independent verifier")


def verifier_lineages(receipt: BootstrapTrustRootCeremonyReceipt) -> frozenset[str]:
    return frozenset(binding.implementation_lineage for binding in receipt.frozen_verifiers)


def require_diverse_verifier_lineage(
    receipt: BootstrapTrustRootCeremonyReceipt,
    *,
    minimum_independent_lineages: int = 1,
) -> None:
    if minimum_independent_lineages < 1:
        raise SemanticError("minimum_independent_lineages must be positive")
    if len(verifier_lineages(receipt)) < minimum_independent_lineages:
        raise SemanticError("bootstrap ceremony lacks required verifier-lineage diversity")
