from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from .core import SemanticError

ANCHOR_TOKEN_RE = re.compile(r"\[(?:H|S|T|TH|RA|A)-[A-Z0-9][A-Z0-9._-]*\]")
SEMANTIC_ANCHOR_RE = re.compile(
    r"^\s*SemanticAnchor\s*:\s*(\[(?:H|S|T|TH|RA|A)-[A-Z0-9][A-Z0-9._-]*\])(?:\s+.*)?$",
    re.IGNORECASE,
)
DIRECT_ANCHOR_RE = re.compile(
    r"^(\[(?:H|S|T|TH|RA|A)-[A-Z0-9][A-Z0-9._-]*\])(?:\s+.*)?$"
)
OWNER_RE = re.compile(r"\bOwners?\s*:\s*(.+)$", re.IGNORECASE)
NORMATIVE_RE = re.compile(
    r"\b(SHALL|MUST|REQUIRED|REQUIRES|CANNOT|NEVER|BLOCKS?|REJECTS?|PROHIBITED|MANDATORY|MAY NOT|FAILS? CLOSED|FAIL-CLOSED)\b",
    re.IGNORECASE,
)
STRUCTURED_NORMATIVE_RE = re.compile(r"^\s*@(D|SC|FC|INV|REG|TEST|POLICY|RIGHT|AUTH|HSA)\|", re.IGNORECASE)
HIGH_IMPACT_RE = re.compile(
    r"\b(HSA|HUMAN SOVEREIGN|RIGHTS?|AUTHORITY|ACTIONGATE|ACTION GATE|POLICY|SAFETY|SECURITY|PRIVACY|PROOF|EVIDENCE|DESIGNEPOCH|FUNCTIONCONTRACT|FUNCTION CONTRACT|SCHEMA(?:ID)?|INVARIANT|SEMANTIC REGISTR|CONSTITUTION|FAILURE STATE|STATE SEMANTICS)\b",
    re.IGNORECASE,
)
HISTORY_RE = re.compile(
    r"\b(HISTORY|HISTORICAL|VERSION(?:ING)?|CHANGELOG|RELEASE NOTES?|PRIOR[- ]ART|ARCHIVE|ARCHIVAL|RETROSPECTIVE|LINEAGE)\b",
    re.IGNORECASE,
)


class SectionUnitAmbiguityError(SemanticError):
    pass


@dataclass(frozen=True)
class SectionUnit:
    unit_id: str
    source_role: str
    source_file: str
    source_file_sha256: str
    start_line: int
    end_line: int
    anchor: str | None
    anchor_occurrence: int
    heading: str
    owner_ids: tuple[str, ...]
    references: tuple[str, ...]
    resolved_reference_target_hashes: Mapping[str, str]
    unresolved_references: tuple[str, ...]
    normative_semantics: bool
    tier: str
    content_sha256: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": "SectionUnit/v1",
            "id": self.unit_id,
            "source_role": self.source_role,
            "source_file": self.source_file,
            "source_file_sha256": self.source_file_sha256,
            "anchors": {
                "primary": self.anchor,
                "occurrence": self.anchor_occurrence,
                "range": {"start_line": self.start_line, "end_line": self.end_line},
                "heading": self.heading,
            },
            "owner_ids": list(self.owner_ids),
            "references": list(self.references),
            "reference_target_hashes": dict(self.resolved_reference_target_hashes),
            "unresolved_references": list(self.unresolved_references),
            "normative_semantics": self.normative_semantics,
            "tier": self.tier,
            "content_sha256": self.content_sha256,
        }


@dataclass(frozen=True)
class CanonicalSectionInventory:
    release: str
    design_epoch: str
    source_root_sha256: str
    process_version: str
    source_hashes: Mapping[str, str]
    units: tuple[SectionUnit, ...]
    coverage_complete: bool
    boundary_algorithm: str

    def counts(self) -> dict[str, int]:
        out = {"TOTAL": len(self.units), "TIER_A": 0, "TIER_B": 0, "TIER_C": 0}
        for unit in self.units:
            out[unit.tier] += 1
        return out

    def inventory_sha256(self) -> str:
        raw = json.dumps([u.to_dict() for u in self.units], sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def count_receipt(self, *, qualified: int = 0, stale: int = 0, unreviewed: int | None = None) -> dict[str, Any]:
        counts = self.counts()
        if unreviewed is None:
            unreviewed = counts["TOTAL"] - qualified - stale
        if min(qualified, stale, unreviewed) < 0 or qualified + stale + unreviewed != counts["TOTAL"]:
            raise SemanticError("coverage states must exactly partition the SectionUnit denominator")
        return {
            "schema": "CanonicalSectionCountReceipt/v1",
            **counts,
            "QUALIFIED": qualified,
            "STALE": stale,
            "UNREVIEWED": unreviewed,
            "source_root": self.source_root_sha256,
            "DesignEpoch": self.design_epoch,
            "ProcessVersion": self.process_version,
            "inventory_sha256": self.inventory_sha256(),
            "coverage_complete": self.coverage_complete,
            "sweep_completion_valid": False,
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": "CanonicalSectionInventory/v1",
            "release": self.release,
            "design_epoch": self.design_epoch,
            "source_root_sha256": self.source_root_sha256,
            "process_version": self.process_version,
            "source_hashes": dict(self.source_hashes),
            "coverage_complete": self.coverage_complete,
            "boundary_algorithm": self.boundary_algorithm,
            "counts": self.counts(),
            "inventory_sha256": self.inventory_sha256(),
            "units": [u.to_dict() for u in self.units],
        }


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _declared_anchor(raw_line: str) -> str | None:
    semantic = SEMANTIC_ANCHOR_RE.match(raw_line)
    if semantic:
        return semantic.group(1).upper()
    if raw_line != raw_line.lstrip():
        return None
    direct = DIRECT_ANCHOR_RE.match(raw_line)
    if not direct:
        return None
    remainder = raw_line[len(direct.group(1)) :].lstrip()
    if remainder.startswith(("->", "→", "=", "|")):
        return None
    return direct.group(1).upper()


def _owner_ids(anchor: str | None, source_role: str, lines: list[str]) -> tuple[str, ...]:
    owners: list[str] = []
    for raw in lines:
        match = OWNER_RE.search(raw)
        if not match:
            continue
        value = match.group(1).strip()
        anchor_ids = [x.upper() for x in ANCHOR_TOKEN_RE.findall(value)]
        if anchor_ids:
            owners.extend(anchor_ids)
        else:
            for item in re.split(r"\s*[;,]\s*", value):
                item = item.strip()
                if item:
                    owners.append(item)
    if not owners:
        owners.append(anchor or f"FILE:{source_role}")
    return tuple(dict.fromkeys(owners))


def _tier_for(anchor: str | None, heading: str, text: str) -> tuple[bool, str]:
    normative = bool(NORMATIVE_RE.search(text) or STRUCTURED_NORMATIVE_RE.search(text) or HIGH_IMPACT_RE.search(text))
    if normative:
        return True, "TIER_A"
    history_basis = " ".join(x for x in (anchor or "", heading, text[:600]) if x)
    if HISTORY_RE.search(history_basis):
        return False, "TIER_C"
    return False, "TIER_B"


def _segment_file(*, source_role: str, source_file: str, raw: bytes) -> tuple[list[dict[str, Any]], str]:
    text = raw.decode("utf-8")
    lines = text.splitlines()
    file_hash = _sha256_bytes(raw)
    declarations: list[tuple[int, str, str]] = []
    for idx, raw_line in enumerate(lines, 1):
        anchor = _declared_anchor(raw_line)
        if anchor:
            declarations.append((idx, anchor, raw_line.strip()))

    starts: list[tuple[int, str | None, str]] = []
    if not declarations or declarations[0][0] > 1:
        starts.append((1, None, "FILE_FRONTMATTER"))
    starts.extend(declarations)

    segments: list[dict[str, Any]] = []
    anchor_occurrence: dict[str, int] = {}
    for pos, (start_line, anchor, heading) in enumerate(starts):
        end_line = starts[pos + 1][0] - 1 if pos + 1 < len(starts) else len(lines)
        if end_line < start_line:
            raise SectionUnitAmbiguityError(f"invalid SectionUnit range in {source_file}: {start_line}>{end_line}")
        segment_lines = lines[start_line - 1 : end_line]
        if not segment_lines:
            raise SectionUnitAmbiguityError(f"empty SectionUnit range in {source_file}:{start_line}-{end_line}")
        content = "\n".join(segment_lines)
        occurrence = 0
        if anchor:
            occurrence = anchor_occurrence.get(anchor, 0) + 1
            anchor_occurrence[anchor] = occurrence
        owner_ids = _owner_ids(anchor, source_role, segment_lines)
        refs = tuple(dict.fromkeys(x.upper() for x in ANCHOR_TOKEN_RE.findall(content)))
        normative, tier = _tier_for(anchor, heading, content)
        local = (anchor or "FRONTMATTER").strip("[]").replace("/", "_")
        unit_id = f"{source_role}:{local}:{occurrence or 1}"
        segments.append({
            "unit_id": unit_id,
            "source_role": source_role,
            "source_file": source_file,
            "source_file_sha256": file_hash,
            "start_line": start_line,
            "end_line": end_line,
            "anchor": anchor,
            "anchor_occurrence": occurrence,
            "heading": heading,
            "owner_ids": owner_ids,
            "references": refs,
            "normative_semantics": normative,
            "tier": tier,
            "content_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        })

    expected_start = 1
    for seg in segments:
        if seg["start_line"] != expected_start:
            raise SectionUnitAmbiguityError(f"SectionUnit coverage gap in {source_file}: expected line {expected_start}, got {seg['start_line']}")
        expected_start = seg["end_line"] + 1
    if expected_start != len(lines) + 1:
        raise SectionUnitAmbiguityError(f"SectionUnit coverage does not terminate at EOF for {source_file}")
    return segments, file_hash


def build_inventory(*, source_dir: Path, manifest: Mapping[str, Any], process_version: str) -> CanonicalSectionInventory:
    if manifest.get("schema") != "GardenCanonicalSourceManifest/v1":
        raise SemanticError("canonical source manifest schema is not recognized")
    release = str(manifest.get("release") or "").strip()
    source_root = str(manifest.get("source_root_sha256") or "").strip()
    if not release or not source_root:
        raise SemanticError("canonical source manifest requires release and source_root_sha256")
    if not process_version.strip():
        raise SemanticError("ProcessVersion is required")
    source_rows = manifest.get("files")
    if not isinstance(source_rows, Mapping) or len(source_rows) != 5:
        raise SemanticError("canonical SectionUnit inventory requires exactly five source roles")

    provisional: list[dict[str, Any]] = []
    source_hashes: dict[str, str] = {}
    for role, entry_raw in source_rows.items():
        if not isinstance(entry_raw, Mapping):
            raise SemanticError(f"manifest file row {role} is invalid")
        entry = dict(entry_raw)
        name = str(entry.get("name") or "").strip()
        expected_hash = str(entry.get("sha256") or "").strip()
        expected_bytes = int(entry.get("bytes") or -1)
        path = source_dir / name
        if not path.is_file():
            raise SemanticError(f"canonical source file missing: {name}")
        raw = path.read_bytes()
        if len(raw) != expected_bytes:
            raise SemanticError(f"canonical source byte count mismatch: {name}")
        actual_hash = _sha256_bytes(raw)
        if actual_hash != expected_hash:
            raise SemanticError(f"canonical source hash mismatch: {name}")
        segments, segmented_hash = _segment_file(source_role=str(role), source_file=name, raw=raw)
        if segmented_hash != actual_hash:
            raise SemanticError(f"SectionUnit segmenter hash drift: {name}")
        provisional.extend(segments)
        source_hashes[name] = actual_hash

    by_anchor: dict[str, list[str]] = {}
    for seg in provisional:
        if seg["anchor"]:
            by_anchor.setdefault(seg["anchor"], []).append(seg["content_sha256"])
    target_hashes = {
        anchor: hashlib.sha256(json.dumps(hashes, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()
        for anchor, hashes in by_anchor.items()
    }

    units: list[SectionUnit] = []
    ids: set[str] = set()
    for seg in provisional:
        if seg["unit_id"] in ids:
            raise SectionUnitAmbiguityError(f"duplicate SectionUnit id: {seg['unit_id']}")
        ids.add(seg["unit_id"])
        refs = tuple(seg["references"])
        resolved = {ref: target_hashes[ref] for ref in refs if ref in target_hashes}
        unresolved = tuple(ref for ref in refs if ref not in target_hashes)
        units.append(SectionUnit(
            unit_id=seg["unit_id"],
            source_role=seg["source_role"],
            source_file=seg["source_file"],
            source_file_sha256=seg["source_file_sha256"],
            start_line=seg["start_line"],
            end_line=seg["end_line"],
            anchor=seg["anchor"],
            anchor_occurrence=seg["anchor_occurrence"],
            heading=seg["heading"],
            owner_ids=tuple(seg["owner_ids"]),
            references=refs,
            resolved_reference_target_hashes=resolved,
            unresolved_references=unresolved,
            normative_semantics=bool(seg["normative_semantics"]),
            tier=seg["tier"],
            content_sha256=seg["content_sha256"],
        ))

    design_epoch = f"{release.replace('Garden ', 'Garden-')}@{source_root}"
    return CanonicalSectionInventory(
        release=release,
        design_epoch=design_epoch,
        source_root_sha256=source_root,
        process_version=process_version,
        source_hashes=source_hashes,
        units=tuple(units),
        coverage_complete=True,
        boundary_algorithm=(
            "SectionUnit/v1-anchor-occurrence-v1: file frontmatter plus every explicit SemanticAnchor or unindented non-mapping canonical anchor declaration; ranges are contiguous through EOF; repeated anchors are occurrence-qualified; reference target hashes aggregate all declarations of the referenced anchor."
        ),
    )
