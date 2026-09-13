from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum

from .core import SemanticError


class CausalLevel(IntEnum):
    C0_CORRELATION = 0
    C1_TEMPORAL = 1
    C2_MECHANISTIC = 2
    C3_INTERVENTION = 3
    C4_COUNTERFACTUAL = 4


@dataclass(frozen=True)
class CausalRelationLevelBinding:
    source_ref: str
    target_ref: str
    level: CausalLevel
    model_refs: tuple[str, ...] = ()
    assumption_refs: tuple[str, ...] = ()
    evidence_refs: tuple[str, ...] = ()
    identification_refs: tuple[str, ...] = ()
    uncertainty_refs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.source_ref.strip() or not self.target_ref.strip():
            raise SemanticError("causal relation requires source and target")
        if self.level >= CausalLevel.C2_MECHANISTIC and not self.model_refs:
            raise SemanticError("C2+ causes relation requires a declared causal/mechanistic model")
        if self.level >= CausalLevel.C2_MECHANISTIC and not self.assumption_refs:
            raise SemanticError("C2+ causes relation requires explicit assumptions")
        if self.level >= CausalLevel.C3_INTERVENTION and not self.identification_refs:
            raise SemanticError("C3+ causes relation requires intervention/identification support")
        if self.level >= CausalLevel.C4_COUNTERFACTUAL and not self.evidence_refs:
            raise SemanticError("C4 causes relation requires evidence/support refs")


def require_causal_level(
    binding: CausalRelationLevelBinding,
    *,
    minimum_level: CausalLevel,
) -> None:
    if binding.level < minimum_level:
        raise SemanticError(
            f"CAUSAL_LEVEL_UNDERFLOW:{binding.level.name}->{minimum_level.name}"
        )


def compose_causal_path(
    edges: tuple[CausalRelationLevelBinding, ...],
) -> CausalLevel:
    """Return only the maximum level justified by every edge in the path.

    Path composition cannot amplify causal status. A composed path is bounded by
    its weakest edge and still requires an ordinary causal-Claim validation step.
    """
    if not edges:
        raise SemanticError("causal path requires at least one edge")
    for left, right in zip(edges, edges[1:]):
        if left.target_ref != right.source_ref:
            raise SemanticError("causal path edges are not connected")
    return min(edge.level for edge in edges)
