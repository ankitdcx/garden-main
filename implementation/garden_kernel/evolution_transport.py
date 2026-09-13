from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
from typing import Any, Iterable, Mapping

from .core import SemanticError
from .evolution_actions import Condition, EvolutionAction, EvolutionVerb
from .evolution_authority import (
    EvolutionAgentRole,
    EvolutionAuthorityEnvelope,
    make_role_envelope,
)
from .evolution_epoch import EvolutionArtifactBinding, EvolutionArtifactKind
from .evolution_gate import (
    EvolutionGateContext,
    EvolutionGateLog,
    GateDecision,
    evaluate_evolution_action,
)
from .evolution_trust import (
    AttestationKind,
    VerifiedAttestationState,
    verify_attestation_receipts,
    verify_governance_receipt,
)


RECEIPT_SCHEMA = "GardenEvolutionProductionGateReceipt/v1"
REQUEST_SCHEMA = "GardenEvolutionProductionAction/v1"
AUTHORITY_REGISTRY_SCHEMA = "GardenEvolutionAuthorityRegistry/v1"


@dataclass(frozen=True)
class CanonicalSourceIdentity:
    release: str
    design_epoch: str
    source_root_sha256: str
    gsl: str


def source_identity_from_manifest(manifest: Mapping[str, Any]) -> CanonicalSourceIdentity:
    if manifest.get("schema") != "GardenCanonicalSourceManifest/v1":
        raise SemanticError("current canonical source manifest schema is not recognized")
    release = str(manifest.get("release", "")).strip()
    root = str(manifest.get("source_root_sha256", "")).strip()
    gsl = str(manifest.get("gsl", "")).strip()
    if not release.startswith("Garden v") or not root or not gsl:
        raise SemanticError("current canonical source manifest is incomplete")
    return CanonicalSourceIdentity(
        release=release,
        design_epoch=release.removeprefix("Garden "),
        source_root_sha256=root,
        gsl=gsl,
    )


def load_source_identity(path: str | Path) -> CanonicalSourceIdentity:
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    return source_identity_from_manifest(manifest)


def authority_registry_from_payload(
    payload: Mapping[str, Any],
    identity: CanonicalSourceIdentity,
) -> dict[str, EvolutionAuthorityEnvelope]:
    if payload.get("schema") != AUTHORITY_REGISTRY_SCHEMA:
        raise SemanticError("evolution authority registry schema is not recognized")
    if str(payload.get("design_epoch", "")) != identity.design_epoch:
        raise SemanticError("evolution authority registry is stale for current DesignEpoch")
    if str(payload.get("canonical_source_root_sha256", "")) != identity.source_root_sha256:
        raise SemanticError("evolution authority registry is stale for current source root")

    grants: dict[str, EvolutionAuthorityEnvelope] = {}
    allowed_fields = {
        "authority_id",
        "subject",
        "role",
        "granted_by",
        "resources",
        "max_delegation_depth",
    }
    for raw_value in payload.get("grants") or []:
        raw = dict(raw_value)
        extras = set(raw) - allowed_fields
        if extras:
            raise SemanticError(
                "authority registry grant contains unsupported fields: "
                + ",".join(sorted(extras))
            )
        authority_id = str(raw.get("authority_id", "")).strip()
        if not authority_id or authority_id in grants:
            raise SemanticError("authority registry ids must be non-empty and unique")
        envelope = make_role_envelope(
            subject=str(raw["subject"]),
            role=EvolutionAgentRole(str(raw["role"])),
            granted_by=str(raw["granted_by"]),
            resources=tuple(str(x) for x in raw.get("resources", ())),
            max_delegation_depth=int(raw.get("max_delegation_depth", 0)),
        )
        grants[authority_id] = envelope
    if not grants:
        raise SemanticError("evolution authority registry contains no grants")
    return grants


def load_authority_registry(
    path: str | Path,
    identity: CanonicalSourceIdentity,
) -> dict[str, EvolutionAuthorityEnvelope]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return authority_registry_from_payload(payload, identity)


def _conditions(values: list[str] | tuple[str, ...]) -> frozenset[Condition]:
    try:
        return frozenset(Condition(value) for value in values)
    except ValueError as exc:
        raise SemanticError(f"unknown evolution condition: {exc}") from exc


def _binding(raw: Mapping[str, Any]) -> EvolutionArtifactBinding:
    required = raw.get("required_dependencies")
    return EvolutionArtifactBinding(
        artifact_id=str(raw["artifact_id"]),
        kind=EvolutionArtifactKind(str(raw["kind"])),
        design_epoch=str(raw["design_epoch"]),
        dependencies={str(k): str(v) for k, v in dict(raw.get("dependencies", {})).items()},
        required_dependencies=None if required is None else frozenset(str(x) for x in required),
        derived_from_refs=tuple(str(x) for x in raw.get("derived_from_refs", ())),
        source_obligation_refs=tuple(str(x) for x in raw.get("source_obligation_refs", ())),
    )


def _receipt(
    *,
    request: Mapping[str, Any],
    identity: CanonicalSourceIdentity,
    decision: str,
    reasons: list[str] | tuple[str, ...],
    action_id: str,
    verb: str,
    authority_ref: str | None = None,
    authority: Mapping[str, Any] | None = None,
    governance_receipt: Mapping[str, Any] | None = None,
    attestations: VerifiedAttestationState | None = None,
) -> dict[str, Any]:
    attestation_state = attestations or VerifiedAttestationState()
    governance = dict(governance_receipt or {})
    return {
        "schema": RECEIPT_SCHEMA,
        "request_schema": request.get("schema"),
        "action_id": action_id,
        "verb": verb,
        "decision": decision,
        "reasons": list(reasons),
        "current_design_epoch": identity.design_epoch,
        "current_dependencies": {"canonical_source_root": identity.source_root_sha256},
        "canonical_release": identity.release,
        "gsl": identity.gsl,
        "authority_ref": authority_ref,
        "authority": dict(authority or {}),
        "trusted_attestations": {
            "human_signoff": attestation_state.human_signoff,
            "independent_review": attestation_state.independent_review,
            "verified_receipt_ids": list(attestation_state.receipt_ids),
            "source": "VERIFIED_TRUSTED_RECEIPTS_ONLY",
        },
        "governance": {
            "verified": bool(governance),
            "schema": governance.get("schema"),
            "tier": governance.get("tier"),
            "domains": list(governance.get("domains", ())),
            "reasons": list(governance.get("reasons", ())),
            "receipt_sha256": governance.get("receipt_sha256"),
            "evidence_source": governance.get("evidence_source"),
            "base_ref": governance.get("base_ref"),
            "head_ref": governance.get("head_ref"),
        },
        "canonical_pointer_changed": False,
        "materialization_candidate_only": verb == EvolutionVerb.MATERIALIZE.value,
        "receipt_visibility": "PRESERVE_ALLOW_REJECT_ESCALATE",
    }


def evaluate_production_request(
    request: Mapping[str, Any],
    identity: CanonicalSourceIdentity,
    trusted_authorities: Mapping[str, EvolutionAuthorityEnvelope],
    *,
    trusted_governance_receipt: Mapping[str, Any] | None,
    trusted_attestation_receipts: Iterable[Mapping[str, Any]] = (),
    trusted_attestors: Mapping[str, frozenset[AttestationKind]] | None = None,
) -> dict[str, Any]:
    action_raw = dict(request.get("action") or {})
    action_id = str(action_raw.get("action_id", "UNKNOWN"))
    verb_text = str(action_raw.get("verb", "UNKNOWN"))
    authority_ref = str(request.get("authority_ref", "")).strip() or None
    governance_receipt: Mapping[str, Any] | None = None
    attestation_state = VerifiedAttestationState()
    try:
        if request.get("schema") != REQUEST_SCHEMA:
            raise SemanticError("production request schema is not recognized")
        forbidden_self_assertions = {
            key
            for key in (
                "authority",
                "human_signoff",
                "independent_review",
                "governance_tier",
                "governance_classification",
                "changed_paths",
                "change_manifest",
                "trusted_attestations",
            )
            if key in request
        }
        if forbidden_self_assertions:
            raise SemanticError(
                "production request may not self-assert trusted fields: "
                + ",".join(sorted(forbidden_self_assertions))
            )

        explicit_epoch = str(request.get("design_epoch", ""))
        explicit_dependencies = {
            str(k): str(v)
            for k, v in dict(request.get("dependencies", {})).items()
        }
        if explicit_epoch != identity.design_epoch:
            raise SemanticError(
                f"request DesignEpoch is not current: {explicit_epoch!r} != {identity.design_epoch!r}"
            )
        expected_dependencies = {"canonical_source_root": identity.source_root_sha256}
        if explicit_dependencies != expected_dependencies:
            raise SemanticError(
                "request dependency binding does not equal current canonical source identity"
            )

        verb = EvolutionVerb(verb_text)
        action = EvolutionAction(
            action_id=action_id,
            verb=verb,
            actor_ref=str(action_raw["actor_ref"]),
            subject_ref=str(action_raw["subject_ref"]),
            input_refs=tuple(str(x) for x in action_raw.get("input_refs", ())),
            provenance_refs=tuple(str(x) for x in action_raw.get("provenance_refs", ())),
            satisfied_preconditions=_conditions(
                list(action_raw.get("satisfied_preconditions", ()))
            ),
            claimed_postconditions=_conditions(
                list(action_raw.get("claimed_postconditions", ()))
            ),
        )

        if authority_ref is None:
            raise SemanticError("authority_ref is required")
        envelope = trusted_authorities.get(authority_ref)
        if envelope is None:
            raise SemanticError("authority_ref does not resolve in the trusted registry")
        if envelope.subject != action.actor_ref:
            raise SemanticError("trusted authority subject must equal action actor_ref")

        bound_inputs = tuple(
            _binding(dict(item)) for item in request.get("bound_inputs", ())
        )
        for binding in bound_inputs:
            if binding.dependencies.get("canonical_source_root") != identity.source_root_sha256:
                raise SemanticError(
                    f"artifact {binding.artifact_id} is not bound to the current canonical source root"
                )

        if trusted_governance_receipt is None:
            raise SemanticError("trusted governance classification receipt is required")
        governance_receipt = dict(trusted_governance_receipt)
        governance_tier = verify_governance_receipt(
            governance_receipt,
            action_id=action.action_id,
            design_epoch=identity.design_epoch,
            source_root_sha256=identity.source_root_sha256,
        )

        attestation_state = verify_attestation_receipts(
            trusted_attestation_receipts,
            action_id=action.action_id,
            design_epoch=identity.design_epoch,
            source_root_sha256=identity.source_root_sha256,
            trusted_attestors=trusted_attestors or {},
        )

        context = EvolutionGateContext(
            current_design_epoch=identity.design_epoch,
            current_dependencies=expected_dependencies,
            authority_envelopes=(envelope,),
            bound_inputs=bound_inputs,
            independent_review=attestation_state.independent_review,
            human_signoff=attestation_state.human_signoff,
            governance_tier=governance_tier,
        )
        gate_log = EvolutionGateLog()
        gate = evaluate_evolution_action(action, context, gate_log)
        if len(gate_log.receipts) != 1 or gate_log.receipts[0] != gate:
            raise SemanticError(
                "gate decision was not preserved in the append-only receipt log"
            )
        return _receipt(
            request=request,
            identity=identity,
            decision=gate.decision.value,
            reasons=gate.reasons,
            action_id=gate.action_id,
            verb=gate.verb.value,
            authority_ref=authority_ref,
            authority={
                "subject": envelope.subject,
                "role": envelope.role.value,
                "granted_by": envelope.granted_by,
                "actions": sorted(x.value for x in envelope.actions),
                "resources": sorted(envelope.resources),
                "max_delegation_depth": envelope.max_delegation_depth,
                "can_mint_envelopes": envelope.can_mint_envelopes,
                "can_promote_canon": envelope.can_promote_canon,
            },
            governance_receipt=governance_receipt,
            attestations=attestation_state,
        )
    except (KeyError, TypeError, ValueError, SemanticError) as exc:
        return _receipt(
            request=request,
            identity=identity,
            decision=GateDecision.REJECT.value,
            reasons=(f"TRANSPORT_INVALID:{exc}",),
            action_id=action_id,
            verb=verb_text,
            authority_ref=authority_ref,
            governance_receipt=governance_receipt,
            attestations=attestation_state,
        )


def require_allowed(receipt: Mapping[str, Any]) -> None:
    decision = receipt.get("decision")
    if decision != GateDecision.ALLOW.value:
        raise SemanticError(
            f"production evolution transition blocked by ActionGate: {decision}"
        )
