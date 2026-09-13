from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping


class SemanticError(ValueError):
    """Input cannot be represented without inventing semantics."""


class EpistemicStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    ASSERTED = "ASSERTED"
    SUPPORTED = "SUPPORTED"
    VALIDATED = "VALIDATED"
    PROVEN = "PROVEN"
    CONFLICTED = "CONFLICTED"
    RETRACTED = "RETRACTED"


class ReceiptStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNKNOWN = "UNKNOWN"
    INCONCLUSIVE = "INCONCLUSIVE"
    STALE = "STALE"


@dataclass(frozen=True)
class TypedValue:
    type_name: str
    value: Any
    unit: str | None = None
    representation: str | None = None

    def __post_init__(self) -> None:
        if not self.type_name.strip():
            raise SemanticError("TypedValue.type_name is required")


@dataclass(frozen=True)
class Context:
    context_id: str
    scope: tuple[str, ...] = ()
    design_epoch: str | None = None
    attributes: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.context_id.strip():
            raise SemanticError("Context.context_id is required")


@dataclass(frozen=True)
class EvidenceRef:
    evidence_id: str
    kind: str
    source_ref: str
    content_hash: str | None = None

    def __post_init__(self) -> None:
        if not self.evidence_id or not self.kind or not self.source_ref:
            raise SemanticError("EvidenceRef requires id, kind, and source_ref")


@dataclass(frozen=True)
class Dependency:
    source_ref: str
    target_ref: str
    kind: str
    required: bool = True

    def __post_init__(self) -> None:
        if not self.source_ref or not self.target_ref or not self.kind:
            raise SemanticError("Dependency requires source_ref, target_ref, and kind")
        if self.source_ref == self.target_ref and self.kind in {"build", "derivedFrom", "supersedes"}:
            raise SemanticError(f"self-cycle forbidden for dependency kind {self.kind}")


@dataclass(frozen=True)
class Obligation:
    obligation_id: str
    text: str
    source_file: str
    source_anchor: str | None
    owner: str | None = None
    dependency_refs: tuple[str, ...] = ()
    status: str = "UNRESOLVED"

    def __post_init__(self) -> None:
        if not self.obligation_id or not self.text or not self.source_file:
            raise SemanticError("Obligation requires id, text, and source_file")


@dataclass(frozen=True)
class Claim:
    claim_id: str
    subject: str
    predicate: str
    object: TypedValue
    epistemic_status: EpistemicStatus = EpistemicStatus.UNKNOWN
    context_ref: str | None = None
    evidence_refs: tuple[str, ...] = ()
    dependency_refs: tuple[str, ...] = ()
    provenance: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.claim_id or not self.subject or not self.predicate:
            raise SemanticError("Claim requires claim_id, subject, and predicate")


def parse_claim(data: Mapping[str, Any]) -> Claim:
    """Parse the explicitly supported JSON-like CLAIM subset; reject silent extras."""
    allowed = {
        "claim_id", "subject", "predicate", "object", "epistemic_status",
        "context_ref", "evidence_refs", "dependency_refs", "provenance",
    }
    extra = set(data) - allowed
    if extra:
        raise SemanticError(f"unsupported CLAIM fields: {sorted(extra)}")
    missing = {"claim_id", "subject", "predicate", "object"} - set(data)
    if missing:
        raise SemanticError(f"missing CLAIM fields: {sorted(missing)}")
    obj = data["object"]
    if not isinstance(obj, Mapping):
        raise SemanticError("Claim.object must be a typed object")
    obj_allowed = {"type_name", "value", "unit", "representation"}
    obj_extra = set(obj) - obj_allowed
    if obj_extra:
        raise SemanticError(f"unsupported TypedValue fields: {sorted(obj_extra)}")
    if "type_name" not in obj or "value" not in obj:
        raise SemanticError("TypedValue requires type_name and value")
    try:
        status = EpistemicStatus(data.get("epistemic_status", "UNKNOWN"))
    except ValueError as exc:
        raise SemanticError(f"unsupported epistemic status: {data.get('epistemic_status')}") from exc
    return Claim(
        claim_id=str(data["claim_id"]),
        subject=str(data["subject"]),
        predicate=str(data["predicate"]),
        object=TypedValue(
            type_name=str(obj["type_name"]),
            value=obj["value"],
            unit=None if obj.get("unit") is None else str(obj["unit"]),
            representation=None if obj.get("representation") is None else str(obj["representation"]),
        ),
        epistemic_status=status,
        context_ref=None if data.get("context_ref") is None else str(data["context_ref"]),
        evidence_refs=tuple(map(str, data.get("evidence_refs", ()))),
        dependency_refs=tuple(map(str, data.get("dependency_refs", ()))),
        provenance=tuple(map(str, data.get("provenance", ()))),
    )
