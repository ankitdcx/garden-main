from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from fnmatch import fnmatchcase
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from .core import SemanticError


class RepoArtifactClass(str, Enum):
    CANONICAL_SOURCE = "CANONICAL_SOURCE"
    IMPLEMENTATION = "IMPLEMENTATION"
    TEST = "TEST"
    WORKFLOW = "WORKFLOW"
    CONFIGURATION = "CONFIGURATION"
    WORK_PACKAGE = "WORK_PACKAGE"
    REVIEW = "REVIEW"
    RECEIPT = "RECEIPT"
    TOOLING = "TOOLING"
    BOOTSTRAP = "BOOTSTRAP"
    DOCUMENTATION = "DOCUMENTATION"
    DATA = "DATA"
    FRONTIER = "FRONTIER"


class GardenModule(str, Enum):
    SOURCE_IDENTITY = "SOURCE_IDENTITY"
    GSL_TYPING = "GSL_TYPING"
    DESIGN_EPOCH = "DESIGN_EPOCH"
    SOURCE_OBLIGATION = "SOURCE_OBLIGATION"
    DEPENDENCY = "DEPENDENCY"
    FUNCTION_CONTRACT = "FUNCTION_CONTRACT"
    COMPARE = "COMPARE"
    REASON = "REASON"
    PROOF = "PROOF"
    AAP = "AAP"
    AUTHORITY = "AUTHORITY"
    ACTION_GATE = "ACTION_GATE"
    PROCESS_ALGEBRA = "PROCESS_ALGEBRA"
    POLICY_ALGEBRA = "POLICY_ALGEBRA"
    DECISION_ALGEBRA = "DECISION_ALGEBRA"
    CONFORMANCE_ALGEBRA = "CONFORMANCE_ALGEBRA"
    EVIDENCE_ALGEBRA = "EVIDENCE_ALGEBRA"
    BRIDGE_ALGEBRA = "BRIDGE_ALGEBRA"
    AUDIT = "AUDIT"
    COMPLIANCE = "COMPLIANCE"
    HUMAN_SOVEREIGNTY = "HUMAN_SOVEREIGNTY"
    SECURITY = "SECURITY"
    PRIVACY = "PRIVACY"
    SAFETY = "SAFETY"
    PIPELINE_CONFIG_DELTA = "PIPELINE_CONFIG_DELTA"
    THEORY_PROFILE = "THEORY_PROFILE"


@dataclass(frozen=True)
class RepoProfileRule:
    rule_id: str
    pattern: str
    artifact_class: RepoArtifactClass
    required_change_modules: tuple[GardenModule, ...]
    conditional_change_modules: tuple[GardenModule, ...]
    coverage_state: str
    note: str = ""

    def __post_init__(self) -> None:
        if not self.rule_id.strip() or not self.pattern.strip():
            raise SemanticError("repo profile rule requires rule_id and pattern")
        if self.coverage_state not in {"DECLARED", "FRONTIER"}:
            raise SemanticError("coverage_state must be DECLARED or FRONTIER")


@dataclass(frozen=True)
class RepoConformanceProfile:
    profile_id: str
    design_epoch: str
    canonical_source_root_sha256: str
    rules: tuple[RepoProfileRule, ...]
    semantic_compliance_proved: bool = False

    def __post_init__(self) -> None:
        if not self.profile_id.strip() or not self.design_epoch.strip():
            raise SemanticError("repo conformance profile requires id and DesignEpoch")
        if len(self.canonical_source_root_sha256) != 64:
            raise SemanticError("canonical_source_root_sha256 must be a SHA-256 hex digest")
        if not self.rules:
            raise SemanticError("repo conformance profile requires at least one rule")
        ids = [r.rule_id for r in self.rules]
        if len(ids) != len(set(ids)):
            raise SemanticError("repo profile rule ids must be unique")
        if self.semantic_compliance_proved:
            raise SemanticError(
                "artifact classification profile cannot by itself prove semantic GSL compliance"
            )


@dataclass(frozen=True)
class RepoArtifactRecord:
    path: str
    sha256: str
    bytes: int
    artifact_class: RepoArtifactClass
    rule_id: str
    coverage_state: str
    required_change_modules: tuple[GardenModule, ...]
    conditional_change_modules: tuple[GardenModule, ...]
    shadowed_rule_ids: tuple[str, ...]


@dataclass(frozen=True)
class RepoConformanceReport:
    schema: str
    profile_id: str
    design_epoch: str
    canonical_source_root_sha256: str
    artifact_count: int
    explicit_artifact_count: int
    frontier_artifact_count: int
    semantic_compliance_proved: bool
    artifacts: tuple[RepoArtifactRecord, ...]

    def as_dict(self) -> dict[str, Any]:
        def encode(value: Any) -> Any:
            if isinstance(value, Enum):
                return value.value
            if isinstance(value, tuple):
                return [encode(x) for x in value]
            if hasattr(value, "__dataclass_fields__"):
                return {k: encode(v) for k, v in asdict(value).items()}
            return value

        return encode(self)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _module_tuple(values: list[str] | tuple[str, ...]) -> tuple[GardenModule, ...]:
    try:
        return tuple(GardenModule(value) for value in values)
    except ValueError as exc:
        raise SemanticError(f"unknown Garden module in repo profile: {exc}") from exc


def load_repo_profile(path: str | Path) -> RepoConformanceProfile:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("schema") != "GardenRepoConformanceProfile/v1":
        raise SemanticError("unsupported repo conformance profile schema")
    rules = []
    for raw in payload.get("rules") or []:
        rules.append(
            RepoProfileRule(
                rule_id=str(raw["rule_id"]),
                pattern=str(raw["pattern"]),
                artifact_class=RepoArtifactClass(raw["artifact_class"]),
                required_change_modules=_module_tuple(raw.get("required_change_modules") or []),
                conditional_change_modules=_module_tuple(raw.get("conditional_change_modules") or []),
                coverage_state=str(raw.get("coverage_state", "DECLARED")),
                note=str(raw.get("note", "")),
            )
        )
    return RepoConformanceProfile(
        profile_id=str(payload["profile_id"]),
        design_epoch=str(payload["design_epoch"]),
        canonical_source_root_sha256=str(payload["canonical_source_root_sha256"]),
        rules=tuple(rules),
        semantic_compliance_proved=bool(payload.get("semantic_compliance_proved", False)),
    )


def classify_repo_path(relpath: str, profile: RepoConformanceProfile) -> tuple[RepoProfileRule, tuple[str, ...]]:
    normalized = relpath.replace("\\", "/")
    matches = [rule for rule in profile.rules if fnmatchcase(normalized, rule.pattern)]
    if not matches:
        raise SemanticError(f"repo artifact has no GSL profile rule: {normalized}")
    selected = matches[0]
    return selected, tuple(rule.rule_id for rule in matches[1:])


def iter_repo_files(root: str | Path) -> list[Path]:
    base = Path(root).resolve()
    files: list[Path] = []
    for path in base.rglob("*"):
        if not path.is_file():
            continue
        relparts = path.relative_to(base).parts
        if not relparts:
            continue
        if relparts[0] == ".git" or "__pycache__" in relparts:
            continue
        if path.suffix in {".pyc", ".pyo"}:
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.relative_to(base).as_posix())


def audit_repo(root: str | Path, profile: RepoConformanceProfile) -> RepoConformanceReport:
    base = Path(root).resolve()
    records: list[RepoArtifactRecord] = []
    for path in iter_repo_files(base):
        rel = path.relative_to(base).as_posix()
        rule, shadowed = classify_repo_path(rel, profile)
        records.append(
            RepoArtifactRecord(
                path=rel,
                sha256=_sha256(path),
                bytes=path.stat().st_size,
                artifact_class=rule.artifact_class,
                rule_id=rule.rule_id,
                coverage_state=rule.coverage_state,
                required_change_modules=rule.required_change_modules,
                conditional_change_modules=rule.conditional_change_modules,
                shadowed_rule_ids=shadowed,
            )
        )
    frontier = sum(1 for r in records if r.coverage_state == "FRONTIER")
    return RepoConformanceReport(
        schema="GardenRepoConformanceReport/v1",
        profile_id=profile.profile_id,
        design_epoch=profile.design_epoch,
        canonical_source_root_sha256=profile.canonical_source_root_sha256,
        artifact_count=len(records),
        explicit_artifact_count=len(records) - frontier,
        frontier_artifact_count=frontier,
        semantic_compliance_proved=False,
        artifacts=tuple(records),
    )


def validate_profile_against_manifest(
    profile: RepoConformanceProfile,
    manifest: Mapping[str, Any],
) -> None:
    if manifest.get("schema") != "GardenCanonicalSourceManifest/v1":
        raise SemanticError("unsupported canonical source manifest")
    root = str(manifest.get("source_root_sha256") or "")
    release = str(manifest.get("release") or "")
    expected_epoch = f"{release}:{root}"
    if profile.canonical_source_root_sha256 != root:
        raise SemanticError("repo GSL profile is bound to a stale canonical source root")
    if profile.design_epoch != expected_epoch:
        raise SemanticError("repo GSL profile DesignEpoch does not match current canonical identity")
