from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from enum import Enum
import re
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from .core import SemanticError
from .evolution_algebra import validate_algebra_usage

PROCESS_ENGINE_SCHEMA = "GardenProcessEngine/v1"
PROCESS_TRANSITION_RECEIPT_SCHEMA = "GardenProcessTransitionReceipt/v1"
PROCESS_ROUTE_RECEIPT_SCHEMA = "ProcessRouteReceipt/v1"
CURRENT_GOVERNING_PROCESS_VERSION = "1.4"
PROCESS_ALGEBRA_REGISTRY = "REG-ALGEBRA-001"


class ProcessRoute(str, Enum):
    SECTION_UNIT_REVIEW = "SECTION_UNIT_REVIEW"
    NON_SEMANTIC_REPAIR = "NON_SEMANTIC_REPAIR"
    PATCH_DELTA = "PATCH_DELTA"
    MINOR_DELTA = "MINOR_DELTA"
    MAJOR_DELEGABLE = "MAJOR_DELEGABLE"
    MAJOR_PROTECTED = "MAJOR_PROTECTED"


class ProcessState(str, Enum):
    CREATED = "CREATED"
    ROUTED = "ROUTED"
    PACKET_READY = "PACKET_READY"
    BLIND_REVIEW_COMPLETE = "BLIND_REVIEW_COMPLETE"
    CROSS_EXAM_COMPLETE = "CROSS_EXAM_COMPLETE"
    VALIDATED = "VALIDATED"
    IMPLEMENTED = "IMPLEMENTED"
    ADMITTED = "ADMITTED"
    COMPOSED = "COMPOSED"
    VERIFIED = "VERIFIED"
    PROMOTION_READY = "PROMOTION_READY"
    PROMOTED = "PROMOTED"
    CLOSED = "CLOSED"


@dataclass(frozen=True)
class CycleBinding:
    cycle_id: str
    process_version: str
    design_epoch: str
    source_root_sha256: str
    repo_heads: Mapping[str, str]

    def __post_init__(self) -> None:
        for label in ("cycle_id", "process_version", "design_epoch", "source_root_sha256"):
            value = getattr(self, label)
            if not isinstance(value, str) or not value.strip() or value != value.strip():
                raise SemanticError(f"CycleBinding.{label} is required")
        if re.fullmatch(r"[0-9a-f]{64}", self.source_root_sha256) is None:
            raise SemanticError("CycleBinding.source_root_sha256 must be a SHA-256 digest")
        if not isinstance(self.repo_heads, Mapping):
            raise SemanticError("CycleBinding.repo_heads must be a mapping")
        heads = dict(self.repo_heads)
        for name, head in heads.items():
            if not isinstance(name, str) or not name.strip() or name != name.strip():
                raise SemanticError("CycleBinding repository names must be nonempty canonical strings")
            if not isinstance(head, str) or re.fullmatch(r"[0-9a-f]{40}", head) is None:
                raise SemanticError("CycleBinding repository heads must be full commit SHAs")
        if not heads:
            raise SemanticError("CycleBinding.repo_heads must contain at least one repository")
        object.__setattr__(self, "repo_heads", MappingProxyType(heads))


@dataclass(frozen=True)
class TransitionSpec:
    source: ProcessState
    target: ProcessState
    process_operator: str


@dataclass(frozen=True)
class RouteDefinition:
    route: ProcessRoute
    mandatory_steps: tuple[str, ...]
    optional_steps: tuple[str, ...] = ()
    forbidden_steps: tuple[str, ...] = ()


class ProcessPolicy(ABC):
    """Composable process policy. Policies require validated gates; they mint no authority."""
    name: str

    def required_gates(self, process: "GardenProcess", transition: TransitionSpec) -> frozenset[str]:
        return frozenset()


@dataclass(frozen=True)
class GatePolicy(ProcessPolicy):
    name: str
    gates_by_target: Mapping[ProcessState, frozenset[str]]

    def required_gates(self, process: "GardenProcess", transition: TransitionSpec) -> frozenset[str]:
        return self.gates_by_target.get(transition.target, frozenset())


ROUTE_DEFINITIONS: Mapping[ProcessRoute, RouteDefinition] = {
    ProcessRoute.SECTION_UNIT_REVIEW: RouteDefinition(
        ProcessRoute.SECTION_UNIT_REVIEW,
        ("mechanical_section_unit_binding", "risk_tier_assignment", "packet_construction", "packet_completeness_proof", "blind_review_profile_for_tier", "evidence_attribution", "cross_exam_if_required", "whole_source_closure", "coverage_state_update"),
        ("delta_creation", "shadow_or_mirror_validation", "challenger", "implementation_closure"),
        ("successor_promotion_unless_a_delta_is_admitted",),
    ),
    ProcessRoute.NON_SEMANTIC_REPAIR: RouteDefinition(
        ProcessRoute.NON_SEMANTIC_REPAIR,
        ("semantic_touch_check", "LIGHT_NON_SEMANTIC/v1", "reference_closure_where_applicable", "applicable_tests", "post_fix_verification"),
        ("one_qualified_reviewer",),
        ("semantic_delta_admission", "delta_dependency_graph", "successor_classification", "canonical_promotion"),
    ),
    ProcessRoute.PATCH_DELTA: RouteDefinition(
        ProcessRoute.PATCH_DELTA,
        ("semantic_impact", "packet_completeness_proof", "blind_review", "evidence_adjudication", "whole_source_compare", "delta_dependencies", "implementation_validation_as_applicable", "challenger_as_required", "admission", "composition", "retention", "post_composition_verification"),
        ("shadow_implementation", "mirror_validation"),
        ("protected_human_promotion_unless_required_by_touched_semantics",),
    ),
    ProcessRoute.MINOR_DELTA: RouteDefinition(ProcessRoute.MINOR_DELTA, ("all_PATCH_DELTA_steps", "stronger_cross_delta_consistency", "full_affected_closure_review"), ("additional_challenger",)),
    ProcessRoute.MAJOR_DELEGABLE: RouteDefinition(ProcessRoute.MAJOR_DELEGABLE, ("all_MINOR_DELTA_steps", "strongest_review_profile", "shadow_implementation_when_tractable", "global_invariant_consistency", "rollback_readiness", "verified_simplification_receipt"), ("canonical_promotion_only_if_protected_authorization_valid",), ("implicit_human_authority_transfer",)),
    ProcessRoute.MAJOR_PROTECTED: RouteDefinition(ProcessRoute.MAJOR_PROTECTED, ("all_MAJOR_DELEGABLE_steps", "protected_human_decision_for_authority_HSA_rights_constitutional_semantics", "explicit_promotion_receipt"), (), ("automatic_canonical_promotion",)),
}

BINDING_POLICY = GatePolicy("binding", {ProcessState.ROUTED: frozenset({"ROUTE_CLASSIFIED"})})
PACKET_POLICY = GatePolicy("packet", {
    ProcessState.PACKET_READY: frozenset({"PACKET_COMPLETENESS_PROOF_PASS"}),
    ProcessState.BLIND_REVIEW_COMPLETE: frozenset({"BLIND_REVIEW_REQUIREMENTS_MET"}),
    ProcessState.CROSS_EXAM_COMPLETE: frozenset({"CROSS_EXAM_COMPLETE"}),
})
SECTION_POLICY = GatePolicy("section", {ProcessState.VERIFIED: frozenset({"WHOLE_SOURCE_CLOSURE_VERIFIED", "COVERAGE_STATE_UPDATED"})})
LIGHT_POLICY = GatePolicy("light", {
    ProcessState.ROUTED: frozenset({"SEMANTIC_TOUCH_FALSE"}),
    ProcessState.IMPLEMENTED: frozenset({"LIGHT_CHECKS_PASS"}),
    ProcessState.VERIFIED: frozenset({"POST_FIX_VERIFIED"}),
})
SEMANTIC_POLICY = GatePolicy("semantic", {
    ProcessState.VALIDATED: frozenset({"EVIDENCE_REQUIREMENT_MATRIX_PASS", "WHOLE_SOURCE_CLOSURE_VERIFIED", "DELTA_DEPENDENCIES_RESOLVED"}),
    ProcessState.ADMITTED: frozenset({"CHALLENGER_REQUIREMENTS_MET", "ADMISSION_GATES_PASS"}),
    ProcessState.COMPOSED: frozenset({"FIVE_FILE_COMPOSITION_COMPLETE", "RETENTION_VERIFIED"}),
    ProcessState.VERIFIED: frozenset({"POST_COMPOSITION_VERIFIED"}),
    ProcessState.PROMOTED: frozenset({"CANONICAL_PROMOTION_AUTHORIZED"}),
})
MINOR_POLICY = GatePolicy("minor", {ProcessState.VALIDATED: frozenset({"CROSS_DELTA_CONSISTENCY_VERIFIED", "AFFECTED_CLOSURE_REVIEW_COMPLETE"})})
MAJOR_POLICY = GatePolicy("major", {
    ProcessState.VALIDATED: frozenset({"STRONGEST_REVIEW_PROFILE_COMPLETE", "GLOBAL_INVARIANT_CONSISTENCY_VERIFIED"}),
    ProcessState.PROMOTION_READY: frozenset({"ROLLBACK_READY", "SIMPLIFICATION_RECEIPT_VERIFIED", "RULE_ENFORCEMENT_COVERAGE_SUFFICIENT"}),
})
PROTECTED_POLICY = GatePolicy("protected", {ProcessState.PROMOTED: frozenset({"HUMAN_PROTECTED_DECISION_VALID"})})

SECTION_TRANSITIONS = (
    TransitionSpec(ProcessState.CREATED, ProcessState.ROUTED, "BRANCH"),
    TransitionSpec(ProcessState.ROUTED, ProcessState.PACKET_READY, "SEQUENCE"),
    TransitionSpec(ProcessState.PACKET_READY, ProcessState.BLIND_REVIEW_COMPLETE, "PARALLEL"),
    TransitionSpec(ProcessState.BLIND_REVIEW_COMPLETE, ProcessState.CROSS_EXAM_COMPLETE, "SEQUENCE"),
    TransitionSpec(ProcessState.CROSS_EXAM_COMPLETE, ProcessState.VERIFIED, "SEQUENCE"),
    TransitionSpec(ProcessState.VERIFIED, ProcessState.CLOSED, "TERMINATE"),
)
LIGHT_TRANSITIONS = (
    TransitionSpec(ProcessState.CREATED, ProcessState.ROUTED, "BRANCH"),
    TransitionSpec(ProcessState.ROUTED, ProcessState.IMPLEMENTED, "SEQUENCE"),
    TransitionSpec(ProcessState.IMPLEMENTED, ProcessState.VERIFIED, "SEQUENCE"),
    TransitionSpec(ProcessState.VERIFIED, ProcessState.CLOSED, "TERMINATE"),
)
SEMANTIC_TRANSITIONS = (
    TransitionSpec(ProcessState.CREATED, ProcessState.ROUTED, "BRANCH"),
    TransitionSpec(ProcessState.ROUTED, ProcessState.PACKET_READY, "SEQUENCE"),
    TransitionSpec(ProcessState.PACKET_READY, ProcessState.BLIND_REVIEW_COMPLETE, "PARALLEL"),
    TransitionSpec(ProcessState.BLIND_REVIEW_COMPLETE, ProcessState.CROSS_EXAM_COMPLETE, "SEQUENCE"),
    TransitionSpec(ProcessState.CROSS_EXAM_COMPLETE, ProcessState.VALIDATED, "SEQUENCE"),
    TransitionSpec(ProcessState.VALIDATED, ProcessState.ADMITTED, "SEQUENCE"),
    TransitionSpec(ProcessState.ADMITTED, ProcessState.COMPOSED, "COMPOSE"),
    TransitionSpec(ProcessState.COMPOSED, ProcessState.VERIFIED, "SEQUENCE"),
    TransitionSpec(ProcessState.VERIFIED, ProcessState.PROMOTION_READY, "SEQUENCE"),
    TransitionSpec(ProcessState.PROMOTION_READY, ProcessState.PROMOTED, "SEQUENCE"),
    TransitionSpec(ProcessState.PROMOTED, ProcessState.CLOSED, "TERMINATE"),
)


def _strict_strings(values, label):
    if not isinstance(values, (list, tuple)) or any(not isinstance(x, str) or not x or x != x.strip() for x in values):
        raise SemanticError(f"{label} must be a list of canonical strings")
    if len(values) != len(set(values)):
        raise SemanticError(f"{label} must not contain duplicates")
    return list(values)


def _algebra_usage(action_id: str, binding: CycleBinding, operator: str, refs: Sequence[str]) -> dict[str, Any]:
    source_refs = _strict_strings(refs, "source_obligation_refs")
    if not source_refs:
        raise SemanticError("process transition requires source_obligation_refs")
    return {
        "schema": "GardenEvolutionAlgebraUsageReceipt/v1",
        "action_id": action_id,
        "design_epoch": binding.design_epoch,
        "canonical_source_root_sha256": binding.source_root_sha256,
        "source_obligation_refs": source_refs,
        "entries": [
            {"algebra":"Process","status":"APPLIED","operators":[operator],"law_claims":[],"non_law_acknowledgements":["PARALLEL_EFFECT_COMMUTATIVITY_NOT_UNIVERSAL"],"applicability_reason":"A GardenProcess transition executes one registered Process Algebra operator; omitted laws are not inferred."},
            {"algebra":"Policy","status":"FRONTIER","operators":[],"law_claims":[],"non_law_acknowledgements":[],"applicability_reason":"External gates constrain transition eligibility but are not relabeled as executable Policy Algebra.","frontier_reason":"No Policy Algebra operator is executed by GardenProcess."},
            {"algebra":"Decision","status":"FRONTIER","operators":[],"law_claims":[],"non_law_acknowledgements":[],"applicability_reason":"Transition outcomes are typed while executable Decision Algebra signatures remain outside this bounded profile.","frontier_reason":"Decision Algebra executable signatures remain FRONTIER."},
            {"algebra":"Conformance","status":"APPLIED","operators":["BIND_EVIDENCE","COVERAGE"],"law_claims":[],"non_law_acknowledgements":["CONFORMANCE_IS_NOT_BINARY_ONLY","AUDIT_IS_NOT_A_SEPARATE_ALGEBRA"],"applicability_reason":"Required gates are evidence-bound and coverage is recorded without collapsing non-binary states."},
            {"algebra":"Evidence","status":"FRONTIER","operators":[],"law_claims":[],"non_law_acknowledgements":[],"applicability_reason":"Evidence references are carried but no executable Evidence Algebra composition operator is claimed.","frontier_reason":"Evidence Algebra executable signatures remain FRONTIER."},
            {"algebra":"Bridge","status":"NOT_APPLICABLE","operators":[],"law_claims":[],"non_law_acknowledgements":[],"applicability_reason":"Typed Python/JSON transport does not itself invoke a semantic Bridge operator."},
        ],
        "semantic_compliance_proved": False,
    }


class GardenProcess(ABC):
    """Abstract process instance. Concrete routes are siblings and compose shared policies."""
    route: ProcessRoute
    transitions: tuple[TransitionSpec, ...]
    policies: tuple[ProcessPolicy, ...]

    def __init__(self, *, binding: CycleBinding, work_id: str, expected_process_version: str = CURRENT_GOVERNING_PROCESS_VERSION) -> None:
        if binding.process_version != expected_process_version:
            raise SemanticError(f"cycle ProcessVersion {binding.process_version!r} does not match governing version {expected_process_version!r}")
        if not isinstance(work_id, str) or not work_id.strip() or work_id != work_id.strip():
            raise SemanticError("GardenProcess.work_id is required")
        self.binding = binding
        self.work_id = work_id.strip()
        self._state = ProcessState.CREATED

    @property
    def state(self) -> ProcessState:
        return self._state

    @property
    def definition(self) -> RouteDefinition:
        return ROUTE_DEFINITIONS[self.route]

    def route_receipt(self) -> dict[str, Any]:
        return {"schema": PROCESS_ROUTE_RECEIPT_SCHEMA, "cycle_id": self.binding.cycle_id, "work_id": self.work_id, "process_version": self.binding.process_version, "design_epoch": self.binding.design_epoch, "source_root_sha256": self.binding.source_root_sha256, "route": self.route.value, "mandatory_steps": list(self.definition.mandatory_steps), "optional_steps": list(self.definition.optional_steps), "forbidden_steps": list(self.definition.forbidden_steps), "silent_downgrade_forbidden": True}

    def _transition_to(self, target: ProcessState) -> TransitionSpec:
        for spec in self.transitions:
            if spec.source is self.state and spec.target is target:
                return spec
        raise SemanticError(f"{self.route.value} cannot transition {self.state.value}->{target.value}")

    def allowed_transitions(self) -> tuple[ProcessState, ...]:
        return tuple(spec.target for spec in self.transitions if spec.source is self.state)

    def required_gates(self, target: ProcessState) -> frozenset[str]:
        transition = self._transition_to(target)
        out: set[str] = set()
        for policy in self.policies:
            out.update(policy.required_gates(self, transition))
        return frozenset(out)

    def advance(self, target: ProcessState, *, satisfied_gates: Sequence[str], algebra_profile: Mapping[str, Any], source_obligation_refs: Sequence[str]) -> dict[str, Any]:
        transition = self._transition_to(target)
        satisfied = frozenset(_strict_strings(satisfied_gates, "satisfied_gates"))
        required = self.required_gates(target)
        missing = required - satisfied
        if missing:
            raise SemanticError(f"{self.route.value} transition to {target.value} missing gates: {sorted(missing)}")
        previous = self.state
        action_id = f"{self.binding.cycle_id}:{self.work_id}:{previous.value}->{target.value}"
        usage = _algebra_usage(action_id, self.binding, transition.process_operator, source_obligation_refs)
        validation = validate_algebra_usage(usage, algebra_profile, expected_action_id=action_id, expected_design_epoch=self.binding.design_epoch, expected_source_root_sha256=self.binding.source_root_sha256)
        self._state = target
        return {
            "schema": PROCESS_TRANSITION_RECEIPT_SCHEMA,
            "engine_schema": PROCESS_ENGINE_SCHEMA,
            "cycle_id": self.binding.cycle_id,
            "work_id": self.work_id,
            "process_version": self.binding.process_version,
            "design_epoch": self.binding.design_epoch,
            "source_root_sha256": self.binding.source_root_sha256,
            "repo_heads": dict(self.binding.repo_heads),
            "route": self.route.value,
            "from_state": previous.value,
            "to_state": target.value,
            "process_operator": transition.process_operator,
            "required_gates": sorted(required),
            "satisfied_gates": sorted(satisfied),
            "algebra_registry_ref": PROCESS_ALGEBRA_REGISTRY,
            "algebra_usage": usage,
            "algebra_validation": validation,
            "authorization_result": "NOT_MINTED_BY_PROCESS_ENGINE",
            "semantic_compliance_proved": False,
            "boundary": "Transition validity and algebra conformance do not grant authority, admit a semantic delta, or promote Garden canon.",
        }


class SectionUnitReviewProcess(GardenProcess):
    route = ProcessRoute.SECTION_UNIT_REVIEW
    transitions = SECTION_TRANSITIONS
    policies = (BINDING_POLICY, PACKET_POLICY, SECTION_POLICY)


class NonSemanticRepairProcess(GardenProcess):
    route = ProcessRoute.NON_SEMANTIC_REPAIR
    transitions = LIGHT_TRANSITIONS
    policies = (BINDING_POLICY, LIGHT_POLICY)


class PatchDeltaProcess(GardenProcess):
    route = ProcessRoute.PATCH_DELTA
    transitions = SEMANTIC_TRANSITIONS
    policies = (BINDING_POLICY, PACKET_POLICY, SEMANTIC_POLICY)


class MinorDeltaProcess(GardenProcess):
    route = ProcessRoute.MINOR_DELTA
    transitions = SEMANTIC_TRANSITIONS
    policies = (BINDING_POLICY, PACKET_POLICY, SEMANTIC_POLICY, MINOR_POLICY)


class MajorDelegableProcess(GardenProcess):
    route = ProcessRoute.MAJOR_DELEGABLE
    transitions = SEMANTIC_TRANSITIONS
    policies = (BINDING_POLICY, PACKET_POLICY, SEMANTIC_POLICY, MINOR_POLICY, MAJOR_POLICY)


class MajorProtectedProcess(GardenProcess):
    route = ProcessRoute.MAJOR_PROTECTED
    transitions = SEMANTIC_TRANSITIONS
    policies = (BINDING_POLICY, PACKET_POLICY, SEMANTIC_POLICY, MINOR_POLICY, MAJOR_POLICY, PROTECTED_POLICY)


PROCESS_IMPLEMENTATIONS: Mapping[ProcessRoute, type[GardenProcess]] = {
    ProcessRoute.SECTION_UNIT_REVIEW: SectionUnitReviewProcess,
    ProcessRoute.NON_SEMANTIC_REPAIR: NonSemanticRepairProcess,
    ProcessRoute.PATCH_DELTA: PatchDeltaProcess,
    ProcessRoute.MINOR_DELTA: MinorDeltaProcess,
    ProcessRoute.MAJOR_DELEGABLE: MajorDelegableProcess,
    ProcessRoute.MAJOR_PROTECTED: MajorProtectedProcess,
}


class ProcessFactory:
    @staticmethod
    def restore(route_receipt: Mapping[str, Any], transition_receipts: Sequence[Mapping[str, Any]], *, binding: CycleBinding, work_id: str, algebra_profile: Mapping[str, Any], expected_process_version: str = CURRENT_GOVERNING_PROCESS_VERSION) -> GardenProcess:
        """Replay a complete receipt prefix against an externally observed binding.

        Recompute route, transitions, gate coverage and algebra validation. This
        checks record conformance, not truth/authenticity of external gate evidence.
        No partially replayed process is returned if any record fails validation.
        """
        if not isinstance(route_receipt, Mapping):
            raise SemanticError("process restoration requires a route receipt")
        process = ProcessFactory.create(route_receipt.get("route"), binding=binding, work_id=work_id, expected_process_version=expected_process_version)
        if dict(route_receipt) != process.route_receipt():
            raise SemanticError("route receipt differs from observed binding or current route definition")
        if not isinstance(transition_receipts, (list, tuple)):
            raise SemanticError("transition receipts must be an ordered complete prefix")
        for index, receipt in enumerate(transition_receipts):
            try:
                if not isinstance(receipt, Mapping):
                    raise TypeError("receipt must be a mapping")
                target = ProcessState(receipt["to_state"])
                refs = receipt["algebra_usage"]["source_obligation_refs"]
                gates = receipt["satisfied_gates"]
                if not isinstance(refs, list) or not isinstance(gates, list):
                    raise TypeError("gates and source references must be lists")
                if any(not isinstance(item, str) for item in refs + gates):
                    raise TypeError("gates and source references must be strings")
                regenerated = process.advance(target, satisfied_gates=gates, algebra_profile=algebra_profile, source_obligation_refs=refs)
                if dict(receipt) != regenerated:
                    raise SemanticError("receipt binding, order, gate coverage or algebra result mismatch")
            except (KeyError, TypeError, ValueError, SemanticError) as exc:
                raise SemanticError(f"invalid process transition receipt at index {index}: {exc}") from exc
        return process

    @staticmethod
    def create(route: ProcessRoute | str, *, binding: CycleBinding, work_id: str, expected_process_version: str = CURRENT_GOVERNING_PROCESS_VERSION) -> GardenProcess:
        try:
            typed_route = route if isinstance(route, ProcessRoute) else ProcessRoute(route)
        except ValueError as exc:
            raise SemanticError(f"unsupported process route: {route!r}") from exc
        return PROCESS_IMPLEMENTATIONS[typed_route](binding=binding, work_id=work_id, expected_process_version=expected_process_version)
