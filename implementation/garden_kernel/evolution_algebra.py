from __future__ import annotations

from typing import Any, Mapping

from .core import SemanticError


PROFILE_SCHEMA = "GardenEvolutionAlgebraProfile/v1"
USAGE_SCHEMA = "GardenEvolutionAlgebraUsageReceipt/v1"
ALLOWED_STATUSES = frozenset({"APPLIED", "FRONTIER", "NOT_APPLICABLE"})
ALLOWED_APPLICABILITY = frozenset({"REQUIRED", "CONDITIONAL"})
FORBIDDEN_TRUST_FIELDS = frozenset({
    "allow", "authorization", "authority", "decision", "gate_decision",
    "human_signoff", "independent_review", "trusted_attestation",
    "trusted_attestations",
})


def _text(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise SemanticError(f"algebra conformance requires non-empty {label}")
    return text


def _texts(value: Any, label: str, *, allow_empty: bool = False) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        raise SemanticError(f"{label} must be a list")
    items = tuple(str(item).strip() for item in value if str(item).strip())
    if not items and not allow_empty:
        raise SemanticError(f"algebra conformance requires non-empty {label}")
    if len(items) != len(set(items)):
        raise SemanticError(f"{label} must not contain duplicates")
    return items


def _forbid_trust_claims(value: Mapping[str, Any], label: str) -> None:
    found = sorted(FORBIDDEN_TRUST_FIELDS.intersection(value))
    if found:
        raise SemanticError(f"{label} may not mint trust/authorization fields: {','.join(found)}")


def _validate_profile(
    profile: Mapping[str, Any],
    *,
    design_epoch: str,
    source_root_sha256: str,
) -> dict[str, Mapping[str, Any]]:
    if profile.get("schema") != PROFILE_SCHEMA:
        raise SemanticError("algebra profile schema is not recognized")
    if _text(profile.get("design_epoch"), "profile.design_epoch") != design_epoch:
        raise SemanticError("algebra profile is stale for current DesignEpoch")
    if _text(profile.get("canonical_source_root_sha256"), "profile.source_root") != source_root_sha256:
        raise SemanticError("algebra profile is stale for current canonical source root")
    if profile.get("semantic_compliance_proved") is not False:
        raise SemanticError("bounded algebra profile may not claim semantic compliance")
    if _text(profile.get("registry_ref"), "profile.registry_ref") != "REG-ALGEBRA-001":
        raise SemanticError("algebra profile must bind REG-ALGEBRA-001")
    raw = profile.get("algebras")
    if not isinstance(raw, Mapping):
        raise SemanticError("algebra profile requires an algebras mapping")
    expected = {"Process", "Policy", "Decision", "Conformance", "Evidence", "Bridge"}
    if set(raw) != expected:
        raise SemanticError("algebra profile must declare exactly the six current Garden algebra instances")
    out: dict[str, Mapping[str, Any]] = {}
    for name, entry_raw in raw.items():
        if not isinstance(entry_raw, Mapping):
            raise SemanticError(f"algebra profile entry {name} must be an object")
        entry = dict(entry_raw)
        applicability = _text(entry.get("applicability"), f"profile.{name}.applicability")
        if applicability not in ALLOWED_APPLICABILITY:
            raise SemanticError(f"unknown algebra applicability for {name}: {applicability}")
        _texts(entry.get("canonical_refs"), f"profile.{name}.canonical_refs")
        _text(entry.get("operator_registration"), f"profile.{name}.operator_registration")
        _texts(entry.get("registered_operators", ()), f"profile.{name}.registered_operators", allow_empty=True)
        _texts(entry.get("registered_laws", ()), f"profile.{name}.registered_laws", allow_empty=True)
        _texts(entry.get("registered_non_laws", ()), f"profile.{name}.registered_non_laws", allow_empty=True)
        _text(entry.get("frontier_note"), f"profile.{name}.frontier_note")
        if applicability == "CONDITIONAL":
            _text(entry.get("condition"), f"profile.{name}.condition")
        out[name] = entry
    return out


def validate_algebra_usage(
    payload: Mapping[str, Any],
    profile: Mapping[str, Any],
    *,
    expected_action_id: str | None = None,
    expected_design_epoch: str | None = None,
    expected_source_root_sha256: str | None = None,
) -> dict[str, Any]:
    """Validate bounded pipeline algebra use without inferring omitted laws or authority."""

    if payload.get("schema") != USAGE_SCHEMA:
        raise SemanticError("algebra usage schema is not recognized")
    _forbid_trust_claims(payload, "algebra usage receipt")
    action_id = _text(payload.get("action_id"), "usage.action_id")
    design_epoch = _text(payload.get("design_epoch"), "usage.design_epoch")
    source_root = _text(payload.get("canonical_source_root_sha256"), "usage.source_root")
    if expected_action_id is not None and action_id != expected_action_id:
        raise SemanticError("algebra usage action_id does not match production action")
    if expected_design_epoch is not None and design_epoch != expected_design_epoch:
        raise SemanticError("algebra usage is stale for current DesignEpoch")
    if expected_source_root_sha256 is not None and source_root != expected_source_root_sha256:
        raise SemanticError("algebra usage is stale for current canonical source root")
    if payload.get("semantic_compliance_proved") is not False:
        raise SemanticError("algebra usage may not claim semantic compliance")
    source_obligations = _texts(payload.get("source_obligation_refs"), "usage.source_obligation_refs")
    profile_entries = _validate_profile(profile, design_epoch=design_epoch, source_root_sha256=source_root)

    entries_raw = payload.get("entries")
    if not isinstance(entries_raw, list):
        raise SemanticError("algebra usage entries must be a list")
    if len(entries_raw) != len(profile_entries):
        raise SemanticError("algebra usage must classify every profile algebra exactly once")

    seen: set[str] = set()
    summary: dict[str, dict[str, Any]] = {}
    frontier: list[str] = []
    applied: list[str] = []
    not_applicable: list[str] = []
    for raw in entries_raw:
        if not isinstance(raw, Mapping):
            raise SemanticError("algebra usage entries must be objects")
        entry = dict(raw)
        _forbid_trust_claims(entry, "algebra usage entry")
        name = _text(entry.get("algebra"), "entry.algebra")
        if name not in profile_entries or name in seen:
            raise SemanticError(f"unknown or duplicate algebra usage entry: {name}")
        seen.add(name)
        spec = profile_entries[name]
        status = _text(entry.get("status"), f"entry.{name}.status")
        if status not in ALLOWED_STATUSES:
            raise SemanticError(f"unknown algebra usage status for {name}: {status}")
        reason = _text(entry.get("applicability_reason"), f"entry.{name}.applicability_reason")
        operators = _texts(entry.get("operators", ()), f"entry.{name}.operators", allow_empty=True)
        law_claims = _texts(entry.get("law_claims", ()), f"entry.{name}.law_claims", allow_empty=True)
        non_laws = _texts(
            entry.get("non_law_acknowledgements", ()),
            f"entry.{name}.non_law_acknowledgements",
            allow_empty=True,
        )
        frontier_reason = str(entry.get("frontier_reason") or "").strip()

        registered_ops = set(spec.get("registered_operators", ()))
        registered_laws = set(spec.get("registered_laws", ()))
        required_non_laws = set(spec.get("registered_non_laws", ()))
        if set(operators) - registered_ops:
            raise SemanticError(f"{name} usage claims an unregistered operator")
        if set(law_claims) - registered_laws:
            raise SemanticError(f"{name} usage claims an undeclared algebra law")

        if status == "APPLIED":
            if spec.get("operator_registration") == "LEVEL3_FRONTIER":
                raise SemanticError(f"{name} cannot be APPLIED while executable operators remain FRONTIER")
            if not operators:
                raise SemanticError(f"APPLIED algebra {name} requires at least one registered operator")
            if not required_non_laws.issubset(set(non_laws)):
                raise SemanticError(f"APPLIED algebra {name} must acknowledge all registered non-laws")
            if frontier_reason:
                raise SemanticError(f"APPLIED algebra {name} may not carry frontier_reason")
            applied.append(name)
        elif status == "FRONTIER":
            if operators or law_claims:
                raise SemanticError(f"FRONTIER algebra {name} may not claim executable operators or laws")
            if not frontier_reason:
                raise SemanticError(f"FRONTIER algebra {name} requires frontier_reason")
            frontier.append(name)
        else:
            if spec.get("applicability") != "CONDITIONAL":
                raise SemanticError(f"required algebra {name} cannot be NOT_APPLICABLE")
            if operators or law_claims or frontier_reason:
                raise SemanticError(f"NOT_APPLICABLE algebra {name} may not claim operators, laws, or frontier")
            not_applicable.append(name)

        summary[name] = {
            "status": status,
            "operator_count": len(operators),
            "law_claim_count": len(law_claims),
            "applicability_reason": reason,
        }

    return {
        "schema": "GardenEvolutionAlgebraValidationReceipt/v1",
        "action_id": action_id,
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": source_root,
        "source_obligation_refs": list(source_obligations),
        "algebras": summary,
        "applied": applied,
        "frontier": frontier,
        "not_applicable": not_applicable,
        "required_frontier_count": sum(
            1 for name in frontier if profile_entries[name].get("applicability") == "REQUIRED"
        ),
        "authorization_result": "NOT_EVALUATED_HERE",
        "semantic_compliance_proved": False,
        "boundary": "Algebra validation checks declared operator/law/non-law use only; it grants no authority and does not prove Garden certification.",
    }
