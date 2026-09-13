from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping

from .core import SemanticError


class EvolutionArtifactKind(str, Enum):
    FINDING = "FINDING"
    TEST = "TEST"
    DELTA = "DELTA"


class BindingStatus(str, Enum):
    CURRENT = "CURRENT"
    STALE = "STALE"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class EvolutionArtifactBinding:
    artifact_id: str
    kind: EvolutionArtifactKind
    design_epoch: str
    dependencies: Mapping[str, str]
    required_dependencies: frozenset[str] | None
    derived_from_refs: tuple[str, ...] = ()
    source_obligation_refs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.artifact_id.strip():
            raise SemanticError("artifact_id is required")
        if not self.design_epoch.strip():
            raise SemanticError("design_epoch is required")
        if self.kind is EvolutionArtifactKind.DELTA and not self.source_obligation_refs:
            raise SemanticError("DELTA requires at least one source obligation reference")


@dataclass(frozen=True)
class BindingValidation:
    status: BindingStatus
    reasons: tuple[str, ...]


def validate_evolution_binding(
    binding: EvolutionArtifactBinding,
    *,
    current_design_epoch: str,
    current_dependencies: Mapping[str, str],
) -> BindingValidation:
    stale: list[str] = []
    if binding.design_epoch != current_design_epoch:
        stale.append(f"DESIGN_EPOCH_CHANGED:{binding.design_epoch}->{current_design_epoch}")
    if binding.required_dependencies is None:
        reason = "DEPENDENCY_CLOSURE_NOT_DECLARED"
        return BindingValidation(
            BindingStatus.STALE if stale else BindingStatus.UNKNOWN,
            tuple(stale + [reason]),
        )
    omitted = sorted(binding.required_dependencies - set(binding.dependencies))
    if omitted:
        reasons = [f"DEPENDENCY_CLOSURE_INCOMPLETE:{name}" for name in omitted]
        return BindingValidation(
            BindingStatus.STALE if stale else BindingStatus.UNKNOWN,
            tuple(stale + reasons),
        )
    missing = sorted(set(binding.dependencies) - set(current_dependencies))
    if missing:
        reasons = [f"DEPENDENCY_STATE_UNKNOWN:{name}" for name in missing]
        return BindingValidation(
            BindingStatus.STALE if stale else BindingStatus.UNKNOWN,
            tuple(stale + reasons),
        )
    for name, bound_value in binding.dependencies.items():
        current_value = current_dependencies[name]
        if bound_value != current_value:
            stale.append(f"DEPENDENCY_CHANGED:{name}:{bound_value}->{current_value}")
    if stale:
        return BindingValidation(BindingStatus.STALE, tuple(stale))
    return BindingValidation(BindingStatus.CURRENT, ("BINDING_CURRENT",))


def require_current_for_accumulation(
    bindings: tuple[EvolutionArtifactBinding, ...],
    *,
    current_design_epoch: str,
    current_dependencies: Mapping[str, str],
) -> None:
    if not bindings:
        raise SemanticError("accumulation requires at least one epoch-bound artifact")
    failures: list[str] = []
    for binding in bindings:
        result = validate_evolution_binding(
            binding,
            current_design_epoch=current_design_epoch,
            current_dependencies=current_dependencies,
        )
        if result.status is not BindingStatus.CURRENT:
            failures.append(
                f"{binding.artifact_id}:{result.status.value}:{'|'.join(result.reasons)}"
            )
    if failures:
        raise SemanticError(
            "non-current evolution artifacts cannot accumulate; re-derive first: "
            + "; ".join(failures)
        )
