from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from typing import Mapping

from .core import SemanticError


class ProvenanceDisposition(str, Enum):
    PRESENT = "PRESENT"
    REDACTED = "REDACTED"
    PROVENANCE_GAP = "PROVENANCE_GAP"
    NOT_APPLICABLE = "NOT_APPLICABLE"


@dataclass(frozen=True)
class ProvenanceClassManifest:
    manifest_id: str
    expected_node_classes: frozenset[str]
    expected_edge_kinds: frozenset[str]
    protected_node_classes: frozenset[str] = frozenset()
    protected_edge_kinds: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        if not self.manifest_id.strip():
            raise SemanticError("provenance manifest id is required")
        if not self.expected_node_classes:
            raise SemanticError("provenance manifest requires expected node classes")
        if not self.protected_node_classes <= self.expected_node_classes:
            raise SemanticError("protected node classes must be expected node classes")
        if not self.protected_edge_kinds <= self.expected_edge_kinds:
            raise SemanticError("protected edge kinds must be expected edge kinds")

    @property
    def commitment(self) -> str:
        payload = {
            "manifest_id": self.manifest_id,
            "expected_node_classes": sorted(self.expected_node_classes),
            "expected_edge_kinds": sorted(self.expected_edge_kinds),
            "protected_node_classes": sorted(self.protected_node_classes),
            "protected_edge_kinds": sorted(self.protected_edge_kinds),
        }
        encoded = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class AuthorizedProvenanceView:
    manifest_commitment: str
    visible_node_counts: Mapping[str, int]
    redacted_node_classes: frozenset[str]
    visible_edge_counts: Mapping[str, int]
    redacted_edge_kinds: frozenset[str]


def classify_node_class(
    manifest: ProvenanceClassManifest,
    view: AuthorizedProvenanceView,
    node_class: str,
) -> ProvenanceDisposition:
    if view.manifest_commitment != manifest.commitment:
        raise SemanticError("authorized provenance view does not match manifest commitment")
    if node_class not in manifest.expected_node_classes:
        return ProvenanceDisposition.NOT_APPLICABLE
    if int(view.visible_node_counts.get(node_class, 0)) > 0:
        return ProvenanceDisposition.PRESENT
    if node_class in view.redacted_node_classes:
        if node_class not in manifest.protected_node_classes:
            raise SemanticError("view claims redaction for a class not declared protected")
        return ProvenanceDisposition.REDACTED
    return ProvenanceDisposition.PROVENANCE_GAP


def classify_edge_kind(
    manifest: ProvenanceClassManifest,
    view: AuthorizedProvenanceView,
    edge_kind: str,
) -> ProvenanceDisposition:
    if view.manifest_commitment != manifest.commitment:
        raise SemanticError("authorized provenance view does not match manifest commitment")
    if edge_kind not in manifest.expected_edge_kinds:
        return ProvenanceDisposition.NOT_APPLICABLE
    if int(view.visible_edge_counts.get(edge_kind, 0)) > 0:
        return ProvenanceDisposition.PRESENT
    if edge_kind in view.redacted_edge_kinds:
        if edge_kind not in manifest.protected_edge_kinds:
            raise SemanticError("view claims redaction for an edge kind not declared protected")
        return ProvenanceDisposition.REDACTED
    return ProvenanceDisposition.PROVENANCE_GAP
