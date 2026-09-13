from __future__ import annotations

import hashlib
from dataclasses import dataclass
from enum import Enum
from typing import Callable

from .core import ReceiptStatus, SemanticError


class VerifierClass(str, Enum):
    COMPILE = "COMPILE"
    FORMAL_PROOF = "FORMAL_PROOF"
    EMPIRICAL = "EMPIRICAL"
    SECURITY = "SECURITY"
    CONFORMANCE = "CONFORMANCE"


@dataclass(frozen=True)
class VerificationReceipt:
    verifier_id: str
    verifier_class: VerifierClass
    verifier_version: str
    verifier_hash: str
    artifact_ref: str
    artifact_hash: str
    result: ReceiptStatus
    establishes: tuple[str, ...]
    assumptions: tuple[str, ...]
    design_epoch: str | None
    protected_owner: str
    stale: bool = False


VerifierFn = Callable[[bytes], tuple[ReceiptStatus, tuple[str, ...], tuple[str, ...]]]


@dataclass(frozen=True)
class _Verifier:
    verifier_id: str
    verifier_class: VerifierClass
    version: str
    implementation_hash: str
    protected_owner: str
    fn: VerifierFn


class VerifierRegistry:
    def __init__(self, protected_owners: set[str] | None = None) -> None:
        self._verifiers: dict[str, _Verifier] = {}
        self.protected_owners = protected_owners or {"Garden.ProtectedVerifier"}

    def register(self, *, verifier_id: str, verifier_class: VerifierClass, version: str,
                 implementation_bytes: bytes, protected_owner: str, fn: VerifierFn) -> None:
        if protected_owner not in self.protected_owners:
            raise SemanticError("candidate/unprotected owner cannot register an admission verifier")
        if not version.strip():
            raise SemanticError("verifier version is required")
        digest = hashlib.sha256(implementation_bytes).hexdigest()
        self._verifiers[verifier_id] = _Verifier(
            verifier_id, verifier_class, version, digest, protected_owner, fn
        )

    def verify_bytes(self, verifier_id: str, artifact_ref: str, artifact: bytes,
                     *, design_epoch: str | None = None) -> VerificationReceipt:
        verifier = self._verifiers.get(verifier_id)
        if verifier is None:
            raise KeyError(verifier_id)
        result, establishes, assumptions = verifier.fn(artifact)
        return VerificationReceipt(
            verifier_id=verifier.verifier_id,
            verifier_class=verifier.verifier_class,
            verifier_version=verifier.version,
            verifier_hash=verifier.implementation_hash,
            artifact_ref=artifact_ref,
            artifact_hash=hashlib.sha256(artifact).hexdigest(),
            result=result,
            establishes=tuple(establishes),
            assumptions=tuple(assumptions),
            design_epoch=design_epoch,
            protected_owner=verifier.protected_owner,
        )

    def invalidate_if_changed(self, receipt: VerificationReceipt, *, artifact: bytes | None = None,
                              design_epoch: str | None = None,
                              verifier_version: str | None = None,
                              verifier_implementation_bytes: bytes | None = None) -> VerificationReceipt:
        stale = receipt.stale
        if artifact is not None and hashlib.sha256(artifact).hexdigest() != receipt.artifact_hash:
            stale = True
        if design_epoch is not None and receipt.design_epoch is not None and design_epoch != receipt.design_epoch:
            stale = True
        if verifier_version is not None and verifier_version != receipt.verifier_version:
            stale = True
        if verifier_implementation_bytes is not None and hashlib.sha256(verifier_implementation_bytes).hexdigest() != receipt.verifier_hash:
            stale = True
        if not stale:
            return receipt
        return VerificationReceipt(**{**receipt.__dict__, "result": ReceiptStatus.STALE, "stale": True})

    @staticmethod
    def require_class(receipt: VerificationReceipt, expected: VerifierClass) -> None:
        if receipt.verifier_class is not expected:
            raise SemanticError(
                f"verifier class mismatch: {receipt.verifier_class.value} cannot establish {expected.value}"
            )
