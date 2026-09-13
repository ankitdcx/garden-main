from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from typing import Any, Iterable, Mapping

from .core import SemanticError
from .evolution_constitution import GovernanceTier


GOVERNANCE_RECEIPT_SCHEMA = "GardenEvolutionGovernanceClassificationReceipt/v1"
ATTESTATION_RECEIPT_SCHEMA = "GardenEvolutionTrustedAttestationReceipt/v1"

PROTECTED_CONSTITUTIONAL_PATHS: dict[str, str] = {
    "implementation/garden_kernel/evolution_gate.py": "ACTION_GATE_RULES",
    "implementation/garden_kernel/evolution_authority.py": "AUTHORITY_ENVELOPE_RULES",
    "implementation/garden_kernel/evolution_epoch.py": "DESIGN_EPOCH_BINDING_RULES",
    "implementation/garden_kernel/evolution_constitution.py": "CONSTITUTIONAL_CLASSIFICATION_RULES",
    "governance/evolution_authority_registry.json": "AUTHORITY_ENVELOPE_RULES",
}
PROTECTED_CONSTITUTIONAL_PREFIXES: dict[str, str] = {
    "canonical/current/": "CANONICAL_SOURCE_POINTER_OR_CONTENT",
}


class AttestationKind(str, Enum):
    HUMAN_SIGNOFF = "HUMAN_SIGNOFF"
    INDEPENDENT_REVIEW = "INDEPENDENT_REVIEW"


@dataclass(frozen=True)
class VerifiedAttestationState:
    human_signoff: bool = False
    independent_review: bool = False
    receipt_ids: tuple[str, ...] = ()


def _stable_json(payload: Mapping[str, Any]) -> str:
    try:
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    except (TypeError, ValueError) as exc:
        raise SemanticError("trusted receipt payload must be deterministic JSON") from exc


def _payload_digest(payload: Mapping[str, Any]) -> str:
    return hashlib.sha256(_stable_json(payload).encode("utf-8")).hexdigest()


def _classification(changed_paths: Iterable[str]) -> tuple[GovernanceTier, tuple[str, ...], tuple[str, ...]]:
    paths = tuple(sorted({str(path).strip() for path in changed_paths if str(path).strip()}))
    domains: set[str] = set()
    for path in paths:
        domain = PROTECTED_CONSTITUTIONAL_PATHS.get(path)
        if domain:
            domains.add(domain)
        for prefix, prefix_domain in PROTECTED_CONSTITUTIONAL_PREFIXES.items():
            if path.startswith(prefix):
                domains.add(prefix_domain)
    if domains:
        return (
            GovernanceTier.CONSTITUTIONAL,
            tuple(sorted(domains)),
            tuple(f"PROTECTED_CHANGE:{domain}" for domain in sorted(domains)),
        )
    return (
        GovernanceTier.ORDINARY,
        (),
        ("NO_PROTECTED_CONSTITUTIONAL_PATH_CHANGED",),
    )


def governance_receipt_from_changed_paths(
    *,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
    changed_paths: Iterable[str],
    base_ref: str,
    head_ref: str,
) -> dict[str, Any]:
    paths = tuple(sorted({str(path).strip() for path in changed_paths if str(path).strip()}))
    tier, domains, reasons = _classification(paths)
    payload: dict[str, Any] = {
        "schema": GOVERNANCE_RECEIPT_SCHEMA,
        "action_id": action_id,
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": source_root_sha256,
        "evidence_source": "TRUSTED_GIT_DIFF",
        "base_ref": base_ref,
        "head_ref": head_ref,
        "changed_paths": list(paths),
        "tier": tier.value,
        "domains": list(domains),
        "reasons": list(reasons),
    }
    payload["receipt_sha256"] = _payload_digest(payload)
    return payload


def verify_governance_receipt(
    receipt: Mapping[str, Any],
    *,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
) -> GovernanceTier:
    allowed = {
        "schema",
        "action_id",
        "design_epoch",
        "canonical_source_root_sha256",
        "evidence_source",
        "base_ref",
        "head_ref",
        "changed_paths",
        "tier",
        "domains",
        "reasons",
        "receipt_sha256",
    }
    extras = set(receipt) - allowed
    if extras:
        raise SemanticError(
            "governance receipt contains unsupported fields: " + ",".join(sorted(extras))
        )
    if receipt.get("schema") != GOVERNANCE_RECEIPT_SCHEMA:
        raise SemanticError("governance classification receipt schema is not recognized")
    if str(receipt.get("action_id", "")) != action_id:
        raise SemanticError("governance receipt action_id does not match action")
    if str(receipt.get("design_epoch", "")) != design_epoch:
        raise SemanticError("governance receipt is stale for current DesignEpoch")
    if str(receipt.get("canonical_source_root_sha256", "")) != source_root_sha256:
        raise SemanticError("governance receipt is stale for current source root")
    if receipt.get("evidence_source") != "TRUSTED_GIT_DIFF":
        raise SemanticError("governance classification must come from trusted git diff evidence")
    if not str(receipt.get("base_ref", "")).strip() or not str(receipt.get("head_ref", "")).strip():
        raise SemanticError("governance receipt requires explicit base/head refs")

    unsigned = dict(receipt)
    actual_digest = str(unsigned.pop("receipt_sha256", ""))
    if not actual_digest or actual_digest != _payload_digest(unsigned):
        raise SemanticError("governance classification receipt hash mismatch")

    paths = tuple(str(x) for x in receipt.get("changed_paths", ()))
    tier, domains, reasons = _classification(paths)
    if receipt.get("tier") != tier.value:
        raise SemanticError("governance tier does not match derived trusted change classification")
    if tuple(receipt.get("domains", ())) != domains:
        raise SemanticError("governance domains do not match derived trusted change classification")
    if tuple(receipt.get("reasons", ())) != reasons:
        raise SemanticError("governance reasons do not match derived trusted change classification")
    return tier


def make_attestation_receipt(
    *,
    receipt_id: str,
    kind: AttestationKind,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
    issuer_ref: str,
    evidence_refs: Iterable[str],
    verdict: str = "APPROVED",
) -> dict[str, Any]:
    evidence = tuple(str(x).strip() for x in evidence_refs if str(x).strip())
    if not receipt_id.strip() or not issuer_ref.strip() or not evidence:
        raise SemanticError("trusted attestation requires receipt id, issuer, and evidence refs")
    payload: dict[str, Any] = {
        "schema": ATTESTATION_RECEIPT_SCHEMA,
        "receipt_id": receipt_id,
        "kind": kind.value,
        "action_id": action_id,
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": source_root_sha256,
        "issuer_ref": issuer_ref,
        "verdict": verdict,
        "evidence_refs": list(evidence),
    }
    payload["receipt_sha256"] = _payload_digest(payload)
    return payload


def verify_attestation_receipts(
    receipts: Iterable[Mapping[str, Any]],
    *,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
    trusted_attestors: Mapping[str, frozenset[AttestationKind]],
) -> VerifiedAttestationState:
    human = False
    review = False
    verified_ids: list[str] = []
    allowed = {
        "schema",
        "receipt_id",
        "kind",
        "action_id",
        "design_epoch",
        "canonical_source_root_sha256",
        "issuer_ref",
        "verdict",
        "evidence_refs",
        "receipt_sha256",
    }
    for raw in receipts:
        extras = set(raw) - allowed
        if extras:
            raise SemanticError(
                "attestation receipt contains unsupported fields: " + ",".join(sorted(extras))
            )
        if raw.get("schema") != ATTESTATION_RECEIPT_SCHEMA:
            raise SemanticError("trusted attestation receipt schema is not recognized")
        if str(raw.get("action_id", "")) != action_id:
            raise SemanticError("trusted attestation action_id does not match action")
        if str(raw.get("design_epoch", "")) != design_epoch:
            raise SemanticError("trusted attestation is stale for current DesignEpoch")
        if str(raw.get("canonical_source_root_sha256", "")) != source_root_sha256:
            raise SemanticError("trusted attestation is stale for current source root")
        unsigned = dict(raw)
        actual_digest = str(unsigned.pop("receipt_sha256", ""))
        if not actual_digest or actual_digest != _payload_digest(unsigned):
            raise SemanticError("trusted attestation receipt hash mismatch")

        try:
            kind = AttestationKind(str(raw.get("kind", "")))
        except ValueError as exc:
            raise SemanticError("trusted attestation kind is not recognized") from exc
        issuer = str(raw.get("issuer_ref", "")).strip()
        allowed_kinds = trusted_attestors.get(issuer, frozenset())
        if kind not in allowed_kinds:
            raise SemanticError("attestation issuer is not trusted for requested attestation kind")
        if raw.get("verdict") != "APPROVED":
            continue
        evidence = tuple(str(x).strip() for x in raw.get("evidence_refs", ()) if str(x).strip())
        if not evidence:
            raise SemanticError("approved trusted attestation requires evidence refs")
        receipt_id = str(raw.get("receipt_id", "")).strip()
        if not receipt_id or receipt_id in verified_ids:
            raise SemanticError("trusted attestation receipt ids must be non-empty and unique")
        verified_ids.append(receipt_id)
        if kind is AttestationKind.HUMAN_SIGNOFF:
            human = True
        elif kind is AttestationKind.INDEPENDENT_REVIEW:
            review = True
    return VerifiedAttestationState(
        human_signoff=human,
        independent_review=review,
        receipt_ids=tuple(verified_ids),
    )
