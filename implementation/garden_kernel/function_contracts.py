from __future__ import annotations

import ast
from dataclasses import asdict, dataclass
from fnmatch import fnmatchcase
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable, Mapping

from .core import SemanticError


REGISTRY_SCHEMA = "GardenFunctionContractRegistry/v1"
REPORT_SCHEMA = "GardenFunctionContractCoverageReport/v1"


@dataclass(frozen=True)
class FunctionContractBinding:
    contract_id: str
    path: str
    function: str
    affects: tuple[str, ...]
    input_semantics: str
    output_semantics: str
    error_semantics: str
    unknown_semantics: str
    effect_semantics: str
    proof_obligations: tuple[str, ...]
    test_refs: tuple[str, ...]

    @property
    def identity(self) -> str:
        return f"{self.path}::{self.function}"


@dataclass(frozen=True)
class FunctionContractRegistry:
    registry_id: str
    design_epoch: str
    canonical_source_root_sha256: str
    scope_globs: tuple[str, ...]
    contracts: tuple[FunctionContractBinding, ...]
    semantic_compliance_proved: bool = False


@dataclass(frozen=True)
class FunctionSurfaceRecord:
    identity: str
    path: str
    function: str
    signature: str
    source_sha256: str
    coverage_state: str
    contract_id: str | None
    test_refs: tuple[str, ...]


@dataclass(frozen=True)
class FunctionContractCoverageReport:
    schema: str
    registry_id: str
    design_epoch: str
    canonical_source_root_sha256: str
    scoped_function_count: int
    declared_contract_count: int
    frontier_function_count: int
    declaration_coverage_ratio: float
    semantic_compliance_proved: bool
    functions: tuple[FunctionSurfaceRecord, ...]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def _require_text(value: Any, label: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise SemanticError(f"FunctionContract requires non-empty {label}")
    return text


def _require_text_tuple(values: Iterable[Any], label: str) -> tuple[str, ...]:
    out = tuple(str(value).strip() for value in values if str(value).strip())
    if not out:
        raise SemanticError(f"FunctionContract requires non-empty {label}")
    return out


def load_function_contract_registry(path: str | Path) -> FunctionContractRegistry:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("schema") != REGISTRY_SCHEMA:
        raise SemanticError("unsupported FunctionContract registry schema")
    if bool(payload.get("semantic_compliance_proved", False)):
        raise SemanticError("FunctionContract declarations cannot by themselves prove semantic compliance")

    contracts: list[FunctionContractBinding] = []
    seen_ids: set[str] = set()
    seen_functions: set[str] = set()
    for raw in payload.get("contracts") or []:
        binding = FunctionContractBinding(
            contract_id=_require_text(raw.get("contract_id"), "contract_id"),
            path=_require_text(raw.get("path"), "path"),
            function=_require_text(raw.get("function"), "function"),
            affects=_require_text_tuple(raw.get("affects") or (), "affects"),
            input_semantics=_require_text(raw.get("input_semantics"), "input_semantics"),
            output_semantics=_require_text(raw.get("output_semantics"), "output_semantics"),
            error_semantics=_require_text(raw.get("error_semantics"), "error_semantics"),
            unknown_semantics=_require_text(raw.get("unknown_semantics"), "unknown_semantics"),
            effect_semantics=_require_text(raw.get("effect_semantics"), "effect_semantics"),
            proof_obligations=_require_text_tuple(raw.get("proof_obligations") or (), "proof_obligations"),
            test_refs=_require_text_tuple(raw.get("test_refs") or (), "test_refs"),
        )
        if binding.contract_id in seen_ids:
            raise SemanticError(f"duplicate FunctionContract id: {binding.contract_id}")
        if binding.identity in seen_functions:
            raise SemanticError(f"duplicate FunctionContract function binding: {binding.identity}")
        seen_ids.add(binding.contract_id)
        seen_functions.add(binding.identity)
        contracts.append(binding)

    scope_globs = _require_text_tuple(payload.get("scope_globs") or (), "scope_globs")
    root = _require_text(payload.get("canonical_source_root_sha256"), "canonical_source_root_sha256")
    if len(root) != 64:
        raise SemanticError("FunctionContract registry canonical source root must be SHA-256")
    if not contracts:
        raise SemanticError("FunctionContract registry requires at least one declared contract")
    return FunctionContractRegistry(
        registry_id=_require_text(payload.get("registry_id"), "registry_id"),
        design_epoch=_require_text(payload.get("design_epoch"), "design_epoch"),
        canonical_source_root_sha256=root,
        scope_globs=scope_globs,
        contracts=tuple(contracts),
        semantic_compliance_proved=False,
    )


def validate_registry_against_manifest(
    registry: FunctionContractRegistry,
    manifest: Mapping[str, Any],
) -> None:
    if manifest.get("schema") != "GardenCanonicalSourceManifest/v1":
        raise SemanticError("unsupported canonical source manifest")
    release = str(manifest.get("release") or "")
    expected_epoch = release.removeprefix("Garden ")
    if registry.design_epoch != expected_epoch:
        raise SemanticError("FunctionContract registry is stale for current DesignEpoch")
    if registry.canonical_source_root_sha256 != str(manifest.get("source_root_sha256") or ""):
        raise SemanticError("FunctionContract registry is stale for current canonical source root")


def _annotation_text(node: ast.AST | None) -> str:
    if node is None:
        return "<untyped>"
    return ast.unparse(node)


def _signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    parts: list[str] = []
    positional = [*node.args.posonlyargs, *node.args.args]
    defaults_offset = len(positional) - len(node.args.defaults)
    for index, arg in enumerate(positional):
        part = f"{arg.arg}: {_annotation_text(arg.annotation)}"
        if index >= defaults_offset:
            part += "=<default>"
        parts.append(part)
    if node.args.vararg:
        parts.append(f"*{node.args.vararg.arg}: {_annotation_text(node.args.vararg.annotation)}")
    elif node.args.kwonlyargs:
        parts.append("*")
    for arg, default in zip(node.args.kwonlyargs, node.args.kw_defaults):
        part = f"{arg.arg}: {_annotation_text(arg.annotation)}"
        if default is not None:
            part += "=<default>"
        parts.append(part)
    if node.args.kwarg:
        parts.append(f"**{node.args.kwarg.arg}: {_annotation_text(node.args.kwarg.annotation)}")
    return f"({', '.join(parts)}) -> {_annotation_text(node.returns)}"


def _source_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _scoped_files(root: Path, registry: FunctionContractRegistry) -> tuple[Path, ...]:
    out: list[Path] = []
    for path in sorted(root.rglob("*.py")):
        rel = path.relative_to(root).as_posix()
        if any(fnmatchcase(rel, pattern) for pattern in registry.scope_globs):
            out.append(path)
    return tuple(out)


def enumerate_scoped_public_functions(
    root: str | Path,
    registry: FunctionContractRegistry,
) -> tuple[FunctionSurfaceRecord, ...]:
    base = Path(root).resolve()
    contracts = {contract.identity: contract for contract in registry.contracts}
    records: list[FunctionSurfaceRecord] = []
    discovered: set[str] = set()
    for path in _scoped_files(base, registry):
        rel = path.relative_to(base).as_posix()
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=rel)
        digest = _source_digest(path)
        functions: list[tuple[str, ast.FunctionDef | ast.AsyncFunctionDef]] = []
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"):
                functions.append((node.name, node))
            elif isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                for member in node.body:
                    if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)) and not member.name.startswith("_"):
                        functions.append((f"{node.name}.{member.name}", member))
        for function_name, node in functions:
            identity = f"{rel}::{function_name}"
            contract = contracts.get(identity)
            records.append(
                FunctionSurfaceRecord(
                    identity=identity,
                    path=rel,
                    function=function_name,
                    signature=_signature(node),
                    source_sha256=digest,
                    coverage_state="DECLARED_REFERENCE" if contract else "FRONTIER",
                    contract_id=contract.contract_id if contract else None,
                    test_refs=contract.test_refs if contract else (),
                )
            )
            discovered.add(identity)

    missing = sorted(set(contracts) - discovered)
    if missing:
        raise SemanticError(
            "FunctionContract registry references missing/non-public functions: " + ", ".join(missing)
        )
    return tuple(sorted(records, key=lambda record: record.identity))


def validate_contract_test_refs(
    root: str | Path,
    registry: FunctionContractRegistry,
) -> None:
    base = Path(root).resolve()
    for contract in registry.contracts:
        for ref in contract.test_refs:
            path = base / ref
            if not path.is_file():
                raise SemanticError(
                    f"FunctionContract {contract.contract_id} references missing test: {ref}"
                )


def audit_function_contract_coverage(
    root: str | Path,
    registry: FunctionContractRegistry,
) -> FunctionContractCoverageReport:
    validate_contract_test_refs(root, registry)
    records = enumerate_scoped_public_functions(root, registry)
    declared = sum(1 for record in records if record.coverage_state == "DECLARED_REFERENCE")
    frontier = sum(1 for record in records if record.coverage_state == "FRONTIER")
    total = len(records)
    return FunctionContractCoverageReport(
        schema=REPORT_SCHEMA,
        registry_id=registry.registry_id,
        design_epoch=registry.design_epoch,
        canonical_source_root_sha256=registry.canonical_source_root_sha256,
        scoped_function_count=total,
        declared_contract_count=declared,
        frontier_function_count=frontier,
        declaration_coverage_ratio=0.0 if total == 0 else round(declared / total, 6),
        semantic_compliance_proved=False,
        functions=records,
    )
