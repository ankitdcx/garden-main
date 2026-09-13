from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from .core import Obligation

ANCHOR_RE = re.compile(r"\[(?:H|S|T|TH|RA|A)-[A-Z0-9][A-Z0-9._-]*\]")
DEF_RE = re.compile(r"^@D\|([^|]+)\|(.*)$")
SCHEMA_RE = re.compile(r"^@SC\|([^|]+)\|([^|]*)\|(.*)$")
NORMATIVE_RE = re.compile(r"\b(SHALL|MUST|REQUIRED|REQUIRES|CANNOT|NEVER|BLOCKS?|REJECTS?)\b", re.I)
OWNER_RE = re.compile(r"\bOwners?\s*:\s*(.+)$", re.I)


@dataclass(frozen=True)
class GapRecord:
    gap_id: str
    source_file: str
    line_number: int
    text: str
    reason: str
    source_anchor: str | None


@dataclass
class ClosureManifest:
    source_hashes: dict[str, str] = field(default_factory=dict)
    obligations: list[Obligation] = field(default_factory=list)
    gaps: list[GapRecord] = field(default_factory=list)
    anchors_seen: set[str] = field(default_factory=set)
    parsed_definition_ids: set[str] = field(default_factory=set)
    parsed_schema_names: set[str] = field(default_factory=set)
    total_nonempty_lines: int = 0
    classified_lines: int = 0
    unclassified_lines: int = 0
    coverage_complete: bool = False
    coverage_note: str = (
        "PARTIAL_EXTRACTOR: only recognized structured definitions/schemas and explicit normative text are classified; "
        "unclassified material remains frontier and full source coverage is not claimed."
    )

    def frontier(self) -> list[GapRecord]:
        return list(self.gaps)


class ObligationExtractor:
    """Conservative text extractor: recognized material is emitted; ambiguity stays frontier.

    This reference extractor intentionally never claims complete source coverage.
    A later WP-002 implementation may promote `coverage_complete` only after every
    material source class is explicitly classified and tested.
    """

    def extract_paths(self, paths: Iterable[Path]) -> ClosureManifest:
        manifest = ClosureManifest()
        for path in paths:
            raw = path.read_bytes()
            manifest.source_hashes[path.name] = hashlib.sha256(raw).hexdigest()
            self._extract_text(path.name, raw.decode("utf-8"), manifest)
        manifest.coverage_complete = False
        return manifest

    def _extract_text(self, filename: str, text: str, manifest: ClosureManifest) -> None:
        current_anchor: str | None = None
        current_owner: str | None = None
        for number, raw_line in enumerate(text.splitlines(), 1):
            line = raw_line.strip()
            if not line:
                continue
            manifest.total_nonempty_lines += 1
            classified = False

            full_anchors = ANCHOR_RE.findall(line)
            if full_anchors:
                current_anchor = full_anchors[0]
                manifest.anchors_seen.update(full_anchors)
            owner_match = OWNER_RE.search(line)
            if owner_match:
                current_owner = owner_match.group(1).strip()

            dm = DEF_RE.match(line)
            if dm:
                definition_id, definition_text = dm.groups()
                manifest.parsed_definition_ids.add(definition_id)
                manifest.obligations.append(Obligation(
                    obligation_id=f"DEF:{definition_id}", text=definition_text.strip(),
                    source_file=filename, source_anchor=current_anchor, owner=current_owner,
                    status="EXTRACTED_DEFINITION",
                ))
                classified = True

            if not classified:
                sm = SCHEMA_RE.match(line)
                if sm:
                    name, schema_id, fields = sm.groups()
                    manifest.parsed_schema_names.add(name)
                    manifest.obligations.append(Obligation(
                        obligation_id=f"SCHEMA:{schema_id or name}",
                        text=f"{name}: {fields}", source_file=filename,
                        source_anchor=current_anchor, owner=current_owner,
                        status="EXTRACTED_SCHEMA",
                    ))
                    classified = True

            if not classified and NORMATIVE_RE.search(line):
                oid = hashlib.sha256(f"{filename}:{number}:{line}".encode()).hexdigest()[:16]
                manifest.obligations.append(Obligation(
                    obligation_id=f"TEXT:{oid}", text=line, source_file=filename,
                    source_anchor=current_anchor, owner=current_owner,
                    status="EXTRACTED_NORMATIVE_TEXT",
                ))
                classified = True

            if not classified and line.startswith("@") and not line.startswith("@N|"):
                gid = hashlib.sha256(f"{filename}:{number}:{line}".encode()).hexdigest()[:16]
                manifest.gaps.append(GapRecord(
                    gap_id=f"GAP:{gid}", source_file=filename, line_number=number,
                    text=line, reason="UNSUPPORTED_STRUCTURED_RECORD", source_anchor=current_anchor,
                ))
                classified = True

            if classified:
                manifest.classified_lines += 1
            else:
                manifest.unclassified_lines += 1

    @staticmethod
    def stable_anchor_hash(source_file: str, anchor: str | None, text: str) -> str:
        return hashlib.sha256(f"{source_file}\0{anchor or ''}\0{text}".encode()).hexdigest()
