from __future__ import annotations

from typing import Any, Mapping

from .core import SemanticError

PROFILE_SCHEMA = "GardenEvolutionAAPProfile/v1"
SELECTION_SCHEMA = "GardenEvolutionAAPSelectionReceipt/v1"
VALIDATION_SCHEMA = "GardenEvolutionAAPValidationReceipt/v1"

SIGNALS = (
    "consequence",
    "irreversibility",
    "authority",
    "novelty",
    "uncertainty",
    "sensitivity",
    "dependency_impact",
    "disagreement",
)
LEVELS = {"LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}
FORBIDDEN_TRUST_FIELDS = frozenset({
    "allow", "authorization", "authority_grant", "gate_decision",
    "human_signoff", "independent_review", "trusted_attestation",
    "trusted_attestations",
})


def _text(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise SemanticError(f"AAP receipt requires non-empty {label}")
    return text


def _texts(value: Any, label: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        raise SemanticError(f"AAP receipt {label} must be a list")
    out = tuple(str(x).strip() for x in value if str(x).strip())
    if not out:
        raise SemanticError(f"AAP receipt requires non-empty {label}")
    return out


def _tier(prefix: str, level: int) -> str:
    return f"{prefix}{max(0, min(4, level))}"


def derive_assurance_floor(payload: Mapping[str, Any], profile: Mapping[str, Any]) -> dict[str, Any]:
    if profile.get("schema") != PROFILE_SCHEMA:
        raise SemanticError("AAP profile schema is not recognized")
    impact = payload.get("impact")
    if not isinstance(impact, Mapping):
        raise SemanticError("AAP receipt impact must be an object")

    ranks: list[int] = []
    normalized: dict[str, str] = {}
    for signal in SIGNALS:
        value = str(impact.get(signal, "")).strip().upper()
        if value not in LEVELS:
            raise SemanticError(f"AAP impact.{signal} must be LOW|MEDIUM|HIGH|CRITICAL")
        normalized[signal] = value
        ranks.append(LEVELS[value])

    level = max(ranks, default=1)
    reason = level
    verity = level
    safety = max(0, level - 1)
    escalators: list[str] = []

    if bool(impact.get("hard_policy")):
        reason = max(reason, 4)
        verity = max(verity, 4)
        safety = max(safety, 3)
        escalators.append("HARD_POLICY")
    if bool(impact.get("constitutional")):
        reason = max(reason, 4)
        verity = max(verity, 4)
        safety = max(safety, 3)
        escalators.append("CONSTITUTIONAL")
    if bool(impact.get("physical_safety")):
        safety = 4
        escalators.append("PHYSICAL_SAFETY")

    modules = list(profile.get("baseline_modules") or ())
    triggers = profile.get("module_triggers") or {}
    for key in ("hard_policy", "constitutional", "physical_safety"):
        if bool(impact.get(key)):
            modules.extend(str(x) for x in triggers.get(key, ()))
    if level >= 3:
        modules.extend(str(x) for x in triggers.get("high_or_critical", ()))
    if normalized["novelty"] in {"HIGH", "CRITICAL"} or normalized["uncertainty"] in {"HIGH", "CRITICAL"}:
        modules.extend(str(x) for x in triggers.get("high_novelty_or_uncertainty", ()))

    return {
        "impact": normalized,
        "reason_tier": _tier("R", reason),
        "verity_tier": _tier("V", verity),
        "safety_tier": _tier("S", safety),
        "required_modules": sorted(set(modules)),
        "escalators": escalators,
    }


def validate_assurance_selection(
    payload: Mapping[str, Any],
    profile: Mapping[str, Any],
    *,
    expected_action_id: str | None = None,
    expected_design_epoch: str | None = None,
    expected_source_root_sha256: str | None = None,
) -> dict[str, Any]:
    if payload.get("schema") != SELECTION_SCHEMA:
        raise SemanticError("AAP selection receipt schema is not recognized")
    forbidden = sorted(FORBIDDEN_TRUST_FIELDS.intersection(payload))
    if forbidden:
        raise SemanticError("AAP receipt may not mint trust/authorization fields: " + ",".join(forbidden))

    action_id = _text(payload.get("action_id"), "action_id")
    design_epoch = _text(payload.get("design_epoch"), "design_epoch")
    source_root = _text(payload.get("canonical_source_root_sha256"), "canonical_source_root_sha256")
    if expected_action_id is not None and action_id != expected_action_id:
        raise SemanticError("AAP action_id does not match production action")
    if expected_design_epoch is not None and design_epoch != expected_design_epoch:
        raise SemanticError("AAP receipt is stale for current DesignEpoch")
    if expected_source_root_sha256 is not None and source_root != expected_source_root_sha256:
        raise SemanticError("AAP receipt is stale for current canonical source root")

    source_obligations = _texts(payload.get("source_obligation_refs"), "source_obligation_refs")
    derived = derive_assurance_floor(payload, profile)
    selected = payload.get("selected")
    if not isinstance(selected, Mapping):
        raise SemanticError("AAP receipt selected must be an object")
    for key in ("reason_tier", "verity_tier", "safety_tier"):
        if str(selected.get(key, "")).strip() != derived[key]:
            raise SemanticError(f"AAP selected.{key} is below or different from derived minimum floor")
    selected_modules = sorted({str(x).strip() for x in selected.get("modules", ()) if str(x).strip()})
    missing = sorted(set(derived["required_modules"]) - set(selected_modules))
    if missing:
        raise SemanticError("AAP selected module subset omits required modules: " + ",".join(missing))

    budget = payload.get("resource_budget")
    if not isinstance(budget, Mapping):
        raise SemanticError("AAP resource_budget must be an object")
    budget_status = str(budget.get("status", "")).strip().upper()
    if budget_status not in {"SUFFICIENT", "INSUFFICIENT"}:
        raise SemanticError("AAP resource_budget.status must be SUFFICIENT|INSUFFICIENT")
    if budget_status == "INSUFFICIENT" and payload.get("degradation_disposition") not in {
        "REDUCE_AUTHORITY", "TRANSFER_TO_QUALIFIED_MINIMUM_RISK_PATH", "ESCALATE"
    }:
        raise SemanticError("insufficient assurance budget must reduce authority, transfer control, or escalate")
    if budget_status == "SUFFICIENT" and payload.get("degradation_disposition") != "NONE":
        raise SemanticError("sufficient assurance budget must use degradation_disposition NONE")

    if payload.get("authorization_effect") != "NONE":
        raise SemanticError("AAP selection must declare authorization_effect NONE")
    if payload.get("semantic_compliance_proved") is not False:
        raise SemanticError("AAP selection must not claim semantic compliance")

    return {
        "schema": VALIDATION_SCHEMA,
        "action_id": action_id,
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": source_root,
        "source_obligation_refs": list(source_obligations),
        "derived_minimum": derived,
        "selected": {
            "reason_tier": selected["reason_tier"],
            "verity_tier": selected["verity_tier"],
            "safety_tier": selected["safety_tier"],
            "modules": selected_modules,
        },
        "resource_budget_status": budget_status,
        "degradation_disposition": payload.get("degradation_disposition"),
        "authorization_result": "NOT_EVALUATED_HERE",
        "semantic_compliance_proved": False,
    }
