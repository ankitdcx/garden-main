from __future__ import annotations

import re
from typing import Any, Mapping

from .core import SemanticError
from .evolution_algebra import FORBIDDEN_TRUST_FIELDS, validate_algebra_usage


BOUND_SCHEMA = "AlgebraBoundUpdateReceipt/v1"
BOUND_VALIDATION_SCHEMA = "AlgebraBoundUpdateValidationReceipt/v1"
USAGE_VALIDATION_SCHEMA = "GardenEvolutionAlgebraValidationReceipt/v1"
ALLOWED_TARGET_KINDS = frozenset({"PUBLIC_REPO", "PRIVATE_IMPLEMENTATION", "CANONICAL_DESIGN"})
ALLOWED_RESULTS = frozenset({"APPLIED", "DO_NOTHING", "TERMINATED", "ROLLED_BACK", "COMPENSATED", "FRONTIER_BLOCKED"})
_SHA40 = re.compile(r"^[0-9a-f]{40}$")


def _text(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise SemanticError(f"algebra-bound update requires non-empty {label}")
    return text


def _texts(value: Any, label: str, *, allow_empty: bool = False) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        raise SemanticError(f"{label} must be a list")
    items = tuple(str(item).strip() for item in value if str(item).strip())
    if not items and not allow_empty:
        raise SemanticError(f"algebra-bound update requires non-empty {label}")
    if len(items) != len(set(items)):
        raise SemanticError(f"{label} must not contain duplicates")
    return items


def _forbid_trust_claims(value: Mapping[str, Any], label: str) -> None:
    found = sorted(FORBIDDEN_TRUST_FIELDS.intersection(value))
    if found:
        raise SemanticError(f"{label} may not mint trust/authorization fields: {','.join(found)}")


def _same(label: str, actual: Any, expected: Any) -> None:
    if actual != expected:
        raise SemanticError(f"{label} does not match bound evidence")


def _usage_process_entry(usage: Mapping[str, Any]) -> Mapping[str, Any]:
    entries = usage.get("entries")
    if not isinstance(entries, list):
        raise SemanticError("algebra usage entries must be a list")
    matches = [entry for entry in entries if isinstance(entry, Mapping) and entry.get("algebra") == "Process"]
    if len(matches) != 1:
        raise SemanticError("algebra usage must contain exactly one Process entry")
    return matches[0]


def validate_algebra_bound_update(
    payload: Mapping[str, Any],
    usage_receipt: Mapping[str, Any],
    usage_validation_receipt: Mapping[str, Any],
    profile: Mapping[str, Any],
    *,
    expected_repo: str | None = None,
    expected_repo_sha: str | None = None,
    expected_target_kind: str | None = None,
    expected_process_version: str | None = None,
    expected_design_epoch: str | None = None,
    expected_source_root_sha256: str | None = None,
    expected_profile_ref: str | None = None,
    expected_profile_blob_sha: str | None = None,
) -> dict[str, Any]:
    """Validate an update's algebra binding without granting merge/admission/promotion authority."""

    if payload.get("schema") != BOUND_SCHEMA:
        raise SemanticError("algebra-bound update schema is not recognized")
    _forbid_trust_claims(payload, "algebra-bound update receipt")

    action_id = _text(payload.get("action_id"), "receipt.action_id")
    cycle_id = _text(payload.get("cycle_id"), "receipt.cycle_id")
    process_version = _text(payload.get("process_version"), "receipt.process_version")
    design_epoch = _text(payload.get("design_epoch"), "receipt.design_epoch")
    source_root = _text(payload.get("canonical_source_root_sha256"), "receipt.canonical_source_root_sha256")
    target_kind = _text(payload.get("target_kind"), "receipt.target_kind")
    repo = _text(payload.get("repo"), "receipt.repo")
    repo_sha = _text(payload.get("repo_sha"), "receipt.repo_sha")
    registry_ref = _text(payload.get("registry_ref"), "receipt.registry_ref")
    profile_ref = _text(payload.get("algebra_profile_ref"), "receipt.algebra_profile_ref")
    profile_blob_sha = _text(payload.get("algebra_profile_blob_sha"), "receipt.algebra_profile_blob_sha")
    result = _text(payload.get("result"), "receipt.result")
    operator_trace = _texts(payload.get("process_operator_trace"), "receipt.process_operator_trace")
    non_laws = _texts(payload.get("process_non_law_acknowledgements"), "receipt.process_non_law_acknowledgements")
    conformance_refs = _texts(payload.get("conformance_refs"), "receipt.conformance_refs")
    policy_gate_refs = _texts(payload.get("policy_gate_refs", ()), "receipt.policy_gate_refs", allow_empty=True)
    frontier_claim = _texts(payload.get("remaining_algebra_frontiers", ()), "receipt.remaining_algebra_frontiers", allow_empty=True)
    _text(payload.get("algebra_usage_receipt_ref"), "receipt.algebra_usage_receipt_ref")
    _text(payload.get("algebra_validation_receipt_ref"), "receipt.algebra_validation_receipt_ref")

    if target_kind not in ALLOWED_TARGET_KINDS:
        raise SemanticError(f"unknown target_kind: {target_kind}")
    if result not in ALLOWED_RESULTS:
        raise SemanticError(f"unknown algebra-bound update result: {result}")
    if "/" not in repo:
        raise SemanticError("repo must be owner/name")
    if not _SHA40.fullmatch(repo_sha):
        raise SemanticError("repo_sha must be an exact 40-character lowercase git SHA")
    if registry_ref != "REG-ALGEBRA-001" or profile.get("registry_ref") != registry_ref:
        raise SemanticError("algebra-bound update must bind current REG-ALGEBRA-001 profile")
    if payload.get("semantic_compliance_proved") is not False:
        raise SemanticError("algebra-bound update may not claim semantic compliance while the current bounded profile remains frontiered")

    expected_pairs = (
        ("repo", repo, expected_repo),
        ("repo_sha", repo_sha, expected_repo_sha),
        ("target_kind", target_kind, expected_target_kind),
        ("process_version", process_version, expected_process_version),
        ("design_epoch", design_epoch, expected_design_epoch),
        ("source_root", source_root, expected_source_root_sha256),
        ("profile_ref", profile_ref, expected_profile_ref),
        ("profile_blob_sha", profile_blob_sha, expected_profile_blob_sha),
    )
    for label, actual, expected in expected_pairs:
        if expected is not None and actual != expected:
            raise SemanticError(f"algebra-bound update {label} is stale or mismatched")

    computed = validate_algebra_usage(
        usage_receipt,
        profile,
        expected_action_id=action_id,
        expected_design_epoch=design_epoch,
        expected_source_root_sha256=source_root,
    )
    if usage_validation_receipt.get("schema") != USAGE_VALIDATION_SCHEMA:
        raise SemanticError("stored algebra usage validation receipt schema is not recognized")
    _forbid_trust_claims(usage_validation_receipt, "algebra usage validation receipt")
    for key in (
        "action_id",
        "design_epoch",
        "canonical_source_root_sha256",
        "applied",
        "frontier",
        "not_applicable",
        "required_frontier_count",
        "authorization_result",
        "semantic_compliance_proved",
    ):
        _same(f"stored usage validation {key}", usage_validation_receipt.get(key), computed.get(key))

    process_spec = profile.get("algebras", {}).get("Process")
    if not isinstance(process_spec, Mapping):
        raise SemanticError("algebra profile is missing Process specification")
    registered_ops = set(process_spec.get("registered_operators", ()))
    required_non_laws = set(process_spec.get("registered_non_laws", ()))
    if set(operator_trace) - registered_ops:
        raise SemanticError("algebra-bound update claims an unregistered Process operator")
    if not required_non_laws.issubset(set(non_laws)):
        raise SemanticError("algebra-bound update is missing a required Process non-law acknowledgement")

    process_usage = _usage_process_entry(usage_receipt)
    if process_usage.get("status") != "APPLIED":
        raise SemanticError("algebra-bound update requires Process Algebra APPLIED in the bound usage receipt")
    usage_ops = set(process_usage.get("operators", ()))
    usage_non_laws = set(process_usage.get("non_law_acknowledgements", ()))
    if not set(operator_trace).issubset(usage_ops):
        raise SemanticError("process_operator_trace is not supported by the bound usage receipt")
    if not set(non_laws).issubset(usage_non_laws):
        raise SemanticError("Process non-law acknowledgement is not supported by the bound usage receipt")

    if set(frontier_claim) != set(computed.get("frontier", ())):
        raise SemanticError("remaining_algebra_frontiers does not match validated algebra frontier")
    if computed.get("required_frontier_count", 0) > 0 and payload.get("semantic_compliance_proved") is not False:
        raise SemanticError("required algebra frontier forbids semantic-compliance claim")

    return {
        "schema": BOUND_VALIDATION_SCHEMA,
        "action_id": action_id,
        "cycle_id": cycle_id,
        "process_version": process_version,
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": source_root,
        "target_kind": target_kind,
        "repo": repo,
        "repo_sha": repo_sha,
        "registry_ref": registry_ref,
        "algebra_profile_ref": profile_ref,
        "algebra_profile_blob_sha": profile_blob_sha,
        "process_operator_trace": list(operator_trace),
        "process_non_law_acknowledgements": list(non_laws),
        "conformance_refs": list(conformance_refs),
        "policy_gate_refs": list(policy_gate_refs),
        "remaining_algebra_frontiers": list(computed.get("frontier", ())),
        "result": result,
        "authorization_result": "NOT_EVALUATED_HERE",
        "semantic_compliance_proved": False,
        "boundary": "This validator proves only exact update-to-algebra evidence binding. It grants no merge, admission, promotion, delegation, policy, or canonical authority.",
    }
