from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .core import SemanticError
from .evolution_config import PipelineConfigClass, PipelineConfigDelta


class GovernanceTier(str, Enum):
    ORDINARY = "ORDINARY"
    CONSTITUTIONAL = "CONSTITUTIONAL"


class ConstitutionalDomain(str, Enum):
    ACTION_GATE_RULES = "ACTION_GATE_RULES"
    AUTHORITY_ENVELOPE_RULES = "AUTHORITY_ENVELOPE_RULES"
    DESIGN_EPOCH_BINDING_RULES = "DESIGN_EPOCH_BINDING_RULES"


CONSTITUTIONAL_CONFIG_CLASSES: dict[PipelineConfigClass, ConstitutionalDomain] = {
    PipelineConfigClass.ACTION_GATE_POLICY: ConstitutionalDomain.ACTION_GATE_RULES,
    PipelineConfigClass.AUTHORITY_ENVELOPE_POLICY: ConstitutionalDomain.AUTHORITY_ENVELOPE_RULES,
    PipelineConfigClass.DESIGN_EPOCH_POLICY: ConstitutionalDomain.DESIGN_EPOCH_BINDING_RULES,
}


@dataclass(frozen=True)
class GovernanceClassification:
    tier: GovernanceTier
    domain: ConstitutionalDomain | None
    reason: str


def classify_config_delta(delta: PipelineConfigDelta) -> GovernanceClassification:
    domain = CONSTITUTIONAL_CONFIG_CLASSES.get(delta.config_class)
    if domain is None:
        return GovernanceClassification(
            tier=GovernanceTier.ORDINARY,
            domain=None,
            reason="PIPELINE_CONFIG_CHANGE_WITHIN_EXISTING_CONSTITUTIONAL_RULES",
        )
    return GovernanceClassification(
        tier=GovernanceTier.CONSTITUTIONAL,
        domain=domain,
        reason=f"MODIFIES_{domain.value}",
    )


def require_human_approval(
    classification: GovernanceClassification,
    *,
    human_signoff: bool,
) -> None:
    if classification.tier is GovernanceTier.CONSTITUTIONAL and not human_signoff:
        raise SemanticError(
            "constitutional evolution change requires explicit human signoff"
        )
