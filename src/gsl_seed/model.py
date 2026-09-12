from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

PROFILE = "GSL-SEED-JSON-0.1"

class CoreObject(str, Enum):
    TIME = "TIME"
    SPACE = "SPACE"
    THING = "THING"
    EVENT = "EVENT"
    ACTION = "ACTION"
    AGENCY = "AGENCY"
    RULE = "RULE"
    VALUE = "VALUE"
    CONTEXT = "CONTEXT"
    CLAIM = "CLAIM"

class ClaimStatus(str, Enum):
    REPORTED = "REPORTED"
    HYPOTHESIS = "HYPOTHESIS"
    PREDICTION = "PREDICTION"
    FORMAL_CONCLUSION = "FORMAL_CONCLUSION"
    EMPIRICAL_RESULT = "EMPIRICAL_RESULT"
    SUPPORTED_WITH_SCOPE = "SUPPORTED_WITH_SCOPE"
    REFUTED = "REFUTED"
    INCONCLUSIVE = "INCONCLUSIVE"
    UNKNOWN = "UNKNOWN"
    QUALIFIED_KNOWLEDGE = "QUALIFIED_KNOWLEDGE"

class DependencyKind(str, Enum):
    BUILD = "BUILD"
    LOGICAL = "LOGICAL"
    SEMANTIC = "SEMANTIC"
    RUNTIME = "RUNTIME"

class ReceiptResult(str, Enum):
    PASS_SCOPED = "PASS_SCOPED"
    FAIL = "FAIL"
    INCONCLUSIVE = "INCONCLUSIVE"
    STALE = "STALE"

@dataclass(frozen=True)
class TypedValue:
    type_name: str
    value: Any
    unit: str | None = None

@dataclass(frozen=True)
class Node:
    id: str
    kind: CoreObject
    fields: dict[str, TypedValue] = field(default_factory=dict)

@dataclass(frozen=True)
class Claim:
    id: str
    proposition: str
    status: ClaimStatus
    context_ref: str | None
    evidence_refs: tuple[str, ...] = ()
    scope: str | None = None

@dataclass(frozen=True)
class Dependency:
    source_ref: str
    target_ref: str
    kind: DependencyKind
    feedback_group: str | None = None

@dataclass(frozen=True)
class Obligation:
    id: str
    proposition: str
    owner: str
    status: str
    dependency_refs: tuple[str, ...] = ()

@dataclass(frozen=True)
class TestSpec:
    id: str
    obligation_ref: str
    description: str
    expected: str

@dataclass(frozen=True)
class Receipt:
    id: str
    subject_ref: str
    result: ReceiptResult
    checker_ref: str
    evidence_refs: tuple[str, ...] = ()
    scope: str | None = None

@dataclass(frozen=True)
class Document:
    profile: str
    nodes: tuple[Node, ...]
    claims: tuple[Claim, ...]
    dependencies: tuple[Dependency, ...]
    obligations: tuple[Obligation, ...]
    tests: tuple[TestSpec, ...]
    receipts: tuple[Receipt, ...]
