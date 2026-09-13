from __future__ import annotations

from typing import Any, Mapping

from .core import SemanticError


BUNDLE_SCHEMA = "GardenEvolutionReasoningBundle/v1"
COMPARE_SCHEMA = "GardenEvolutionCompareReceipt/v1"
REASON_SCHEMA = "GardenEvolutionReasonReceipt/v1"
PROOF_SCHEMA = "GardenEvolutionProofReceipt/v1"
EVIDENCE_SCHEMA = "GardenEvolutionEvidenceReceipt/v1"

PROOF_RESULTS = frozenset({"PASS", "FAIL", "UNKNOWN"})
FORBIDDEN_TRUST_FIELDS = frozenset({
    "allow",
    "authorization",
    "authority",
    "decision",
    "gate_decision",
    "human_signoff",
    "independent_review",
    "trusted_attestation",
    "trusted_attestations",
})


def _text(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise SemanticError(f"reasoning receipt requires non-empty {label}")
    return text


def _texts(values: Any, label: str, *, allow_empty: bool = False) -> tuple[str, ...]:
    if not isinstance(values, (list, tuple)):
        raise SemanticError(f"reasoning receipt {label} must be a list")
    out = tuple(str(value).strip() for value in values if str(value).strip())
    if not out and not allow_empty:
        raise SemanticError(f"reasoning receipt requires non-empty {label}")
    return out


def _forbid_trust_claims(section: Mapping[str, Any], label: str) -> None:
    found = sorted(FORBIDDEN_TRUST_FIELDS.intersection(section))
    if found:
        raise SemanticError(
            f"{label} may not mint authorization/trust fields: {','.join(found)}"
        )


def _require_identity(
    section: Mapping[str, Any],
    *,
    schema: str,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
    label: str,
) -> None:
    if section.get("schema") != schema:
        raise SemanticError(f"{label} schema is not recognized")
    if _text(section.get("action_id"), f"{label}.action_id") != action_id:
        raise SemanticError(f"{label} action_id does not match bundle")
    if _text(section.get("design_epoch"), f"{label}.design_epoch") != design_epoch:
        raise SemanticError(f"{label} is stale for current DesignEpoch")
    if (
        _text(
            section.get("canonical_source_root_sha256"),
            f"{label}.canonical_source_root_sha256",
        )
        != source_root_sha256
    ):
        raise SemanticError(f"{label} is stale for current canonical source root")
    _forbid_trust_claims(section, label)


def _validate_compare(
    section: Mapping[str, Any],
    *,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
) -> dict[str, Any]:
    _require_identity(
        section,
        schema=COMPARE_SCHEMA,
        action_id=action_id,
        design_epoch=design_epoch,
        source_root_sha256=source_root_sha256,
        label="Compare receipt",
    )
    _text(section.get("predecessor_ref"), "Compare.predecessor_ref")
    alternatives = section.get("alternatives")
    if not isinstance(alternatives, list) or len(alternatives) < 2:
        raise SemanticError("Compare requires at least DO_NOTHING and one candidate alternative")
    ids: list[str] = []
    for raw in alternatives:
        if not isinstance(raw, Mapping):
            raise SemanticError("Compare alternatives must be objects")
        alt_id = _text(raw.get("alternative_id"), "Compare.alternative_id")
        if alt_id in ids:
            raise SemanticError("Compare alternative ids must be unique")
        ids.append(alt_id)
        _text(raw.get("description"), f"Compare.{alt_id}.description")
        _text(raw.get("projected_effect"), f"Compare.{alt_id}.projected_effect")
        _text(raw.get("risk"), f"Compare.{alt_id}.risk")
    if "DO_NOTHING" not in ids:
        raise SemanticError("Compare must include explicit DO_NOTHING alternative")

    gaps = section.get("bidirectional_gaps")
    if not isinstance(gaps, list) or not gaps:
        raise SemanticError("Compare requires bidirectional_gaps")
    gap_pairs: set[tuple[str, str]] = set()
    for raw in gaps:
        if not isinstance(raw, Mapping):
            raise SemanticError("Compare gaps must be objects")
        source = _text(raw.get("from"), "Compare.gap.from")
        target = _text(raw.get("to"), "Compare.gap.to")
        if source not in ids or target not in ids or source == target:
            raise SemanticError("Compare gap endpoints must name distinct declared alternatives")
        _text(raw.get("gap"), "Compare.gap.gap")
        gap_pairs.add((source, target))
    for alt_id in ids:
        if alt_id == "DO_NOTHING":
            continue
        if ("DO_NOTHING", alt_id) not in gap_pairs or (alt_id, "DO_NOTHING") not in gap_pairs:
            raise SemanticError(
                f"Compare lacks bidirectional DO_NOTHING gap coverage for {alt_id}"
            )
    return {"alternative_ids": ids, "gap_pair_count": len(gap_pairs)}


def _validate_reason(
    section: Mapping[str, Any],
    *,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
) -> dict[str, Any]:
    _require_identity(
        section,
        schema=REASON_SCHEMA,
        action_id=action_id,
        design_epoch=design_epoch,
        source_root_sha256=source_root_sha256,
        label="Reason receipt",
    )
    _text(section.get("strategy"), "Reason.strategy")
    _text(section.get("tier"), "Reason.tier")
    _texts(section.get("assumptions"), "Reason.assumptions")
    _text(section.get("uncertainty"), "Reason.uncertainty")
    _texts(section.get("counterexamples"), "Reason.counterexamples")
    dependencies = _texts(section.get("dependency_refs"), "Reason.dependency_refs")
    _text(section.get("conclusion"), "Reason.conclusion")
    if section.get("authorization_effect") != "NONE":
        raise SemanticError("Reason must declare authorization_effect NONE")
    return {"dependency_refs": list(dependencies)}


def _derived_proof_result(results: tuple[str, ...]) -> str:
    if "FAIL" in results:
        return "FAIL"
    if results and all(result == "PASS" for result in results):
        return "PASS"
    return "UNKNOWN"


def _validate_proof(
    section: Mapping[str, Any],
    *,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
) -> dict[str, Any]:
    _require_identity(
        section,
        schema=PROOF_SCHEMA,
        action_id=action_id,
        design_epoch=design_epoch,
        source_root_sha256=source_root_sha256,
        label="Proof receipt",
    )
    obligations = section.get("obligations")
    if not isinstance(obligations, list) or not obligations:
        raise SemanticError("Proof requires explicit proof obligations")
    ids: set[str] = set()
    results: list[str] = []
    for raw in obligations:
        if not isinstance(raw, Mapping):
            raise SemanticError("Proof obligations must be objects")
        obligation_id = _text(raw.get("obligation_id"), "Proof.obligation_id")
        if obligation_id in ids:
            raise SemanticError("Proof obligation ids must be unique")
        ids.add(obligation_id)
        _text(raw.get("statement"), f"Proof.{obligation_id}.statement")
        _text(raw.get("verifier_class"), f"Proof.{obligation_id}.verifier_class")
        result = _text(raw.get("result"), f"Proof.{obligation_id}.result")
        if result not in PROOF_RESULTS:
            raise SemanticError(f"unknown proof result: {result}")
        results.append(result)
        evidence_refs = _texts(
            raw.get("evidence_refs", ()),
            f"Proof.{obligation_id}.evidence_refs",
            allow_empty=result == "UNKNOWN",
        )
        if result != "UNKNOWN" and not evidence_refs:
            raise SemanticError("PASS/FAIL proof obligations require evidence refs")
    derived = _derived_proof_result(tuple(results))
    if section.get("overall_result") != derived:
        raise SemanticError("Proof overall_result must equal the derived obligation result")
    if section.get("authorization_effect") != "NONE":
        raise SemanticError("Proof must declare authorization_effect NONE")
    return {"overall_result": derived, "obligation_count": len(obligations)}


def _validate_evidence(
    section: Mapping[str, Any],
    *,
    action_id: str,
    design_epoch: str,
    source_root_sha256: str,
) -> dict[str, Any]:
    _require_identity(
        section,
        schema=EVIDENCE_SCHEMA,
        action_id=action_id,
        design_epoch=design_epoch,
        source_root_sha256=source_root_sha256,
        label="Evidence receipt",
    )
    items = section.get("items")
    if not isinstance(items, list) or not items:
        raise SemanticError("Evidence requires at least one evidence item")
    refs: list[str] = []
    for raw in items:
        if not isinstance(raw, Mapping):
            raise SemanticError("Evidence items must be objects")
        _text(raw.get("kind"), "Evidence.kind")
        ref = _text(raw.get("ref"), "Evidence.ref")
        _text(raw.get("claim_scope"), "Evidence.claim_scope")
        refs.append(ref)
    if section.get("proof_effect") != "NONE":
        raise SemanticError("Evidence must declare proof_effect NONE")
    if section.get("authorization_effect") != "NONE":
        raise SemanticError("Evidence must declare authorization_effect NONE")
    return {"evidence_refs": refs, "item_count": len(items)}


def validate_reasoning_bundle(
    payload: Mapping[str, Any],
    *,
    expected_action_id: str | None = None,
    expected_design_epoch: str | None = None,
    expected_source_root_sha256: str | None = None,
) -> dict[str, Any]:
    """Validate typed Compare/Reason/Proof/Evidence separation without granting authority."""

    if payload.get("schema") != BUNDLE_SCHEMA:
        raise SemanticError("reasoning bundle schema is not recognized")
    action_id = _text(payload.get("action_id"), "bundle.action_id")
    design_epoch = _text(payload.get("design_epoch"), "bundle.design_epoch")
    source_root = _text(
        payload.get("canonical_source_root_sha256"),
        "bundle.canonical_source_root_sha256",
    )
    if expected_action_id is not None and action_id != expected_action_id:
        raise SemanticError("reasoning bundle action_id does not match production action")
    if expected_design_epoch is not None and design_epoch != expected_design_epoch:
        raise SemanticError("reasoning bundle is stale for current DesignEpoch")
    if (
        expected_source_root_sha256 is not None
        and source_root != expected_source_root_sha256
    ):
        raise SemanticError("reasoning bundle is stale for current canonical source root")

    source_obligations = _texts(
        payload.get("source_obligation_refs"),
        "bundle.source_obligation_refs",
    )
    assertions = payload.get("separation_assertions")
    required_assertions = {
        "compare_is_not_decision",
        "reason_is_not_authorization",
        "evidence_is_not_proof",
        "proof_is_not_authorization",
        "actiongate_owns_authorization",
    }
    if not isinstance(assertions, Mapping) or set(assertions) != required_assertions:
        raise SemanticError("reasoning bundle separation_assertions are incomplete")
    if not all(assertions.get(name) is True for name in required_assertions):
        raise SemanticError("reasoning bundle separation assertions must all be true")

    compare = _validate_compare(
        dict(payload.get("compare") or {}),
        action_id=action_id,
        design_epoch=design_epoch,
        source_root_sha256=source_root,
    )
    reason = _validate_reason(
        dict(payload.get("reason") or {}),
        action_id=action_id,
        design_epoch=design_epoch,
        source_root_sha256=source_root,
    )
    proof = _validate_proof(
        dict(payload.get("proof") or {}),
        action_id=action_id,
        design_epoch=design_epoch,
        source_root_sha256=source_root,
    )
    evidence = _validate_evidence(
        dict(payload.get("evidence") or {}),
        action_id=action_id,
        design_epoch=design_epoch,
        source_root_sha256=source_root,
    )
    return {
        "schema": "GardenEvolutionReasoningValidationReceipt/v1",
        "action_id": action_id,
        "design_epoch": design_epoch,
        "canonical_source_root_sha256": source_root,
        "source_obligation_refs": list(source_obligations),
        "compare": compare,
        "reason": reason,
        "proof": proof,
        "evidence": evidence,
        "authorization_result": "NOT_EVALUATED_HERE",
        "semantic_compliance_proved": False,
    }
