from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping, Sequence

from .core import SemanticError

ENTRY_SCHEMA = "GardenEvolutionAuditEntry/v1"
CHAIN_SCHEMA = "GardenEvolutionAuditChainReceipt/v1"
VALIDATION_SCHEMA = "GardenEvolutionAuditValidationReceipt/v1"
GENESIS_HASH = "0" * 64
FORBIDDEN_TRUST_FIELDS = frozenset({
    "allow", "authorization", "authority_grant", "gate_decision",
    "human_signoff", "independent_review", "trusted_attestation",
    "trusted_attestations", "canonical_promotion", "certification",
})


def _canonical_bytes(value: Mapping[str, Any]) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_json(value: Mapping[str, Any]) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _make_audit_entry(
    *,
    sequence: int,
    previous_entry_hash: str,
    record_ref: str,
    record_sha256: str,
    record_schema: str,
    action_id: str,
    design_epoch: str,
    canonical_source_root_sha256: str,
    disposition: str,
) -> dict[str, Any]:
    if sequence < 0:
        raise SemanticError("audit sequence must be non-negative")
    if len(previous_entry_hash) != 64 or any(c not in "0123456789abcdef" for c in previous_entry_hash.lower()):
        raise SemanticError("audit previous_entry_hash must be a SHA-256 hex digest")
    if len(record_sha256) != 64 or any(c not in "0123456789abcdef" for c in record_sha256.lower()):
        raise SemanticError("audit record_sha256 must be a SHA-256 hex digest")
    values = {
        "record_ref": record_ref,
        "record_schema": record_schema,
        "action_id": action_id,
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": canonical_source_root_sha256,
        "disposition": disposition,
    }
    for label, value in values.items():
        if not str(value or "").strip():
            raise SemanticError(f"audit entry requires non-empty {label}")
    body = {
        "schema": ENTRY_SCHEMA,
        "sequence": sequence,
        "previous_entry_hash": previous_entry_hash.lower(),
        "record_ref": str(record_ref),
        "record_sha256": record_sha256.lower(),
        "record_schema": str(record_schema),
        "action_id": str(action_id),
        "design_epoch": str(design_epoch),
        "canonical_source_root_sha256": str(canonical_source_root_sha256),
        "disposition": str(disposition),
        "authorization_effect": "NONE",
    }
    body["entry_hash"] = _sha256_json(body)
    return body


def build_audit_chain(
    records: Sequence[Mapping[str, Any]],
    *,
    chain_id: str,
    design_epoch: str,
    canonical_source_root_sha256: str,
) -> dict[str, Any]:
    if not chain_id.strip():
        raise SemanticError("audit chain_id must be non-empty")
    if not records:
        raise SemanticError("audit chain requires at least one record")
    entries: list[dict[str, Any]] = []
    previous = GENESIS_HASH
    for sequence, record in enumerate(records):
        forbidden = sorted(FORBIDDEN_TRUST_FIELDS.intersection(record))
        if forbidden:
            raise SemanticError("audit record descriptor may not mint trust fields: " + ",".join(forbidden))
        entry = _make_audit_entry(
            sequence=sequence,
            previous_entry_hash=previous,
            record_ref=str(record.get("record_ref", "")),
            record_sha256=str(record.get("record_sha256", "")),
            record_schema=str(record.get("record_schema", "")),
            action_id=str(record.get("action_id", "")),
            design_epoch=design_epoch,
            canonical_source_root_sha256=canonical_source_root_sha256,
            disposition=str(record.get("disposition", "RECORDED")),
        )
        entries.append(entry)
        previous = entry["entry_hash"]
    return {
        "schema": CHAIN_SCHEMA,
        "chain_id": chain_id,
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": canonical_source_root_sha256,
        "genesis_hash": GENESIS_HASH,
        "entry_count": len(entries),
        "head_hash": previous,
        "entries": entries,
        "append_only_linkage": "SHA256_PREDECESSOR_CHAIN",
        "authorization_effect": "NONE",
        "semantic_compliance_proved": False,
    }


def validate_audit_chain(
    chain: Mapping[str, Any],
    *,
    expected_design_epoch: str | None = None,
    expected_source_root_sha256: str | None = None,
) -> dict[str, Any]:
    if chain.get("schema") != CHAIN_SCHEMA:
        raise SemanticError("audit chain schema is not recognized")
    forbidden = sorted(FORBIDDEN_TRUST_FIELDS.intersection(chain))
    if forbidden:
        raise SemanticError("audit chain may not mint trust fields: " + ",".join(forbidden))
    design_epoch = str(chain.get("design_epoch", "")).strip()
    source_root = str(chain.get("canonical_source_root_sha256", "")).strip()
    if expected_design_epoch is not None and design_epoch != expected_design_epoch:
        raise SemanticError("audit chain is stale for current DesignEpoch")
    if expected_source_root_sha256 is not None and source_root != expected_source_root_sha256:
        raise SemanticError("audit chain is stale for current canonical source root")
    if chain.get("genesis_hash") != GENESIS_HASH:
        raise SemanticError("audit chain genesis hash is invalid")
    if chain.get("authorization_effect") != "NONE":
        raise SemanticError("audit chain must declare authorization_effect NONE")
    if chain.get("semantic_compliance_proved") is not False:
        raise SemanticError("audit chain must not claim semantic compliance")
    entries = chain.get("entries")
    if not isinstance(entries, list) or not entries:
        raise SemanticError("audit chain entries must be a non-empty list")
    if chain.get("entry_count") != len(entries):
        raise SemanticError("audit chain entry_count mismatch")
    previous = GENESIS_HASH
    checked: list[str] = []
    for sequence, raw in enumerate(entries):
        if not isinstance(raw, Mapping) or raw.get("schema") != ENTRY_SCHEMA:
            raise SemanticError("audit chain contains an invalid entry schema")
        entry = dict(raw)
        observed_hash = str(entry.pop("entry_hash", ""))
        if entry.get("sequence") != sequence:
            raise SemanticError("audit chain sequence is not contiguous")
        if entry.get("previous_entry_hash") != previous:
            raise SemanticError("audit chain predecessor linkage mismatch")
        if entry.get("design_epoch") != design_epoch or entry.get("canonical_source_root_sha256") != source_root:
            raise SemanticError("audit entry identity does not match chain identity")
        forbidden_entry = sorted(FORBIDDEN_TRUST_FIELDS.intersection(entry))
        if forbidden_entry:
            raise SemanticError("audit entry may not mint trust fields: " + ",".join(forbidden_entry))
        if entry.get("authorization_effect") != "NONE":
            raise SemanticError("audit entry must declare authorization_effect NONE")
        derived_hash = _sha256_json(entry)
        if observed_hash != derived_hash:
            raise SemanticError("audit entry content hash mismatch")
        previous = observed_hash
        checked.append(observed_hash)
    if chain.get("head_hash") != previous:
        raise SemanticError("audit chain head_hash mismatch")
    return {
        "schema": VALIDATION_SCHEMA,
        "chain_id": chain.get("chain_id"),
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": source_root,
        "entry_count": len(entries),
        "head_hash": previous,
        "checked_entry_hashes": checked,
        "tamper_evident": True,
        "authorization_result": "NOT_EVALUATED_HERE",
        "semantic_compliance_proved": False,
    }
