from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from typing import Any, Mapping

from .core import SemanticError
from .evolution_epoch import EvolutionArtifactBinding, EvolutionArtifactKind


class PipelineConfigClass(str, Enum):
    ROTATION_SCHEDULE = "ROTATION_SCHEDULE"
    INTEGRATOR_PROMPT = "INTEGRATOR_PROMPT"
    REVIEWER_ROLE = "REVIEWER_ROLE"
    ROUTING_POLICY = "ROUTING_POLICY"
    ACTION_GATE_POLICY = "ACTION_GATE_POLICY"
    AUTHORITY_ENVELOPE_POLICY = "AUTHORITY_ENVELOPE_POLICY"
    DESIGN_EPOCH_POLICY = "DESIGN_EPOCH_POLICY"


def _stable_payload(values: Mapping[str, Any]) -> str:
    try:
        return json.dumps(values, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    except (TypeError, ValueError) as exc:
        raise SemanticError("pipeline config must be deterministically JSON-serializable") from exc


def config_hash(values: Mapping[str, Any]) -> str:
    return hashlib.sha256(_stable_payload(values).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class PipelineConfigSnapshot:
    config_id: str
    config_class: PipelineConfigClass
    design_epoch: str
    values: Mapping[str, Any]
    source_obligation_refs: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.config_id.strip() or not self.design_epoch.strip():
            raise SemanticError("config snapshot requires config_id and design_epoch")
        if not self.source_obligation_refs:
            raise SemanticError("config snapshot requires source obligation references")
        config_hash(self.values)

    @property
    def digest(self) -> str:
        return config_hash(self.values)


@dataclass(frozen=True)
class PipelineConfigDelta:
    delta_id: str
    config_id: str
    config_class: PipelineConfigClass
    design_epoch: str
    before_hash: str
    after_hash: str
    changed_fields: tuple[str, ...]
    source_obligation_refs: tuple[str, ...]
    provenance_refs: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.delta_id.strip() or not self.config_id.strip() or not self.design_epoch.strip():
            raise SemanticError("config delta requires delta_id, config_id, and design_epoch")
        if not self.changed_fields:
            raise SemanticError("config delta requires at least one changed field")
        if len(set(self.changed_fields)) != len(self.changed_fields):
            raise SemanticError("config delta changed_fields must be unique")
        if not self.source_obligation_refs:
            raise SemanticError("config delta requires source obligation references")
        if not self.provenance_refs:
            raise SemanticError("config delta requires provenance")
        if self.before_hash == self.after_hash:
            raise SemanticError("no-op pipeline config delta is forbidden")

    def as_epoch_binding(self) -> EvolutionArtifactBinding:
        return EvolutionArtifactBinding(
            artifact_id=self.delta_id,
            kind=EvolutionArtifactKind.DELTA,
            design_epoch=self.design_epoch,
            dependencies={"pipeline_config_before": self.before_hash},
            required_dependencies=frozenset({"pipeline_config_before"}),
            derived_from_refs=self.provenance_refs,
        )


def derive_config_delta(
    *,
    delta_id: str,
    before: PipelineConfigSnapshot,
    after: PipelineConfigSnapshot,
    provenance_refs: tuple[str, ...],
) -> PipelineConfigDelta:
    if before.config_id != after.config_id:
        raise SemanticError("config delta cannot change config identity")
    if before.config_class is not after.config_class:
        raise SemanticError("config delta cannot change config class")
    if before.design_epoch != after.design_epoch:
        raise SemanticError("cross-epoch config changes require re-derivation, not mutation")
    if before.source_obligation_refs != after.source_obligation_refs:
        raise SemanticError("source obligation rebinding must be explicit, not hidden in a config delta")

    before_keys = set(before.values)
    after_keys = set(after.values)
    changed = sorted(
        key for key in before_keys | after_keys
        if before.values.get(key) != after.values.get(key)
        or (key in before.values) != (key in after.values)
    )
    if not changed:
        raise SemanticError("no-op pipeline config delta is forbidden")

    return PipelineConfigDelta(
        delta_id=delta_id,
        config_id=before.config_id,
        config_class=before.config_class,
        design_epoch=before.design_epoch,
        before_hash=before.digest,
        after_hash=after.digest,
        changed_fields=tuple(changed),
        source_obligation_refs=before.source_obligation_refs,
        provenance_refs=provenance_refs,
    )
