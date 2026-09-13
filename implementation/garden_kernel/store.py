from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Iterable

from .core import Claim, EpistemicStatus, EvidenceRef, SemanticError, TypedValue


_ALLOWED_PROMOTIONS: dict[EpistemicStatus, set[EpistemicStatus]] = {
    EpistemicStatus.UNKNOWN: {EpistemicStatus.ASSERTED, EpistemicStatus.CONFLICTED, EpistemicStatus.RETRACTED},
    EpistemicStatus.ASSERTED: {EpistemicStatus.SUPPORTED, EpistemicStatus.CONFLICTED, EpistemicStatus.RETRACTED},
    EpistemicStatus.SUPPORTED: {EpistemicStatus.VALIDATED, EpistemicStatus.PROVEN, EpistemicStatus.CONFLICTED, EpistemicStatus.RETRACTED},
    EpistemicStatus.VALIDATED: {EpistemicStatus.CONFLICTED, EpistemicStatus.RETRACTED},
    EpistemicStatus.PROVEN: {EpistemicStatus.CONFLICTED, EpistemicStatus.RETRACTED},
    EpistemicStatus.CONFLICTED: {EpistemicStatus.SUPPORTED, EpistemicStatus.VALIDATED, EpistemicStatus.PROVEN, EpistemicStatus.RETRACTED},
    EpistemicStatus.RETRACTED: set(),
}


class KnowledgeStore:
    def __init__(self, path: str | Path = ":memory:") -> None:
        self.conn = sqlite3.connect(str(path))
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys=ON")
        self._init_schema()

    def _init_schema(self) -> None:
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS claims(
          claim_id TEXT PRIMARY KEY, subject TEXT NOT NULL, predicate TEXT NOT NULL,
          object_json TEXT NOT NULL, epistemic_status TEXT NOT NULL,
          context_ref TEXT, provenance_json TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS evidence(
          evidence_id TEXT PRIMARY KEY, kind TEXT NOT NULL, source_ref TEXT NOT NULL,
          content_hash TEXT
        );
        CREATE TABLE IF NOT EXISTS claim_evidence(
          claim_id TEXT NOT NULL REFERENCES claims(claim_id),
          evidence_id TEXT NOT NULL REFERENCES evidence(evidence_id),
          admitted INTEGER NOT NULL DEFAULT 0,
          PRIMARY KEY(claim_id,evidence_id)
        );
        CREATE TABLE IF NOT EXISTS dependencies(
          source_ref TEXT NOT NULL, target_ref TEXT NOT NULL, kind TEXT NOT NULL,
          required INTEGER NOT NULL DEFAULT 1,
          PRIMARY KEY(source_ref,target_ref,kind)
        );
        CREATE TABLE IF NOT EXISTS transitions(
          transition_id INTEGER PRIMARY KEY AUTOINCREMENT,
          claim_id TEXT NOT NULL REFERENCES claims(claim_id),
          from_status TEXT NOT NULL, to_status TEXT NOT NULL,
          reason TEXT NOT NULL, evidence_json TEXT NOT NULL,
          created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS corrections(
          correction_id INTEGER PRIMARY KEY AUTOINCREMENT,
          claim_id TEXT NOT NULL REFERENCES claims(claim_id),
          supersedes_claim_id TEXT, counterexample_ref TEXT,
          note TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """)
        self.conn.commit()

    def put_claim(self, claim: Claim) -> None:
        obj = {"type_name": claim.object.type_name, "value": claim.object.value,
               "unit": claim.object.unit, "representation": claim.object.representation}
        self.conn.execute(
            "INSERT INTO claims VALUES(?,?,?,?,?,?,?)",
            (claim.claim_id, claim.subject, claim.predicate, json.dumps(obj, sort_keys=True),
             claim.epistemic_status.value, claim.context_ref, json.dumps(claim.provenance)),
        )
        for dep in claim.dependency_refs:
            self.add_dependency(claim.claim_id, dep, "semantic", True)
        self.conn.commit()

    def get_claim(self, claim_id: str) -> Claim | None:
        row = self.conn.execute("SELECT * FROM claims WHERE claim_id=?", (claim_id,)).fetchone()
        if row is None:
            return None
        obj = json.loads(row["object_json"])
        deps = [r[0] for r in self.conn.execute(
            "SELECT target_ref FROM dependencies WHERE source_ref=? ORDER BY target_ref", (claim_id,)
        )]
        evidence = [r[0] for r in self.conn.execute(
            "SELECT evidence_id FROM claim_evidence WHERE claim_id=? AND admitted=1 ORDER BY evidence_id", (claim_id,)
        )]
        return Claim(
            claim_id=row["claim_id"], subject=row["subject"], predicate=row["predicate"],
            object=TypedValue(**obj), epistemic_status=EpistemicStatus(row["epistemic_status"]),
            context_ref=row["context_ref"], evidence_refs=tuple(evidence),
            dependency_refs=tuple(deps), provenance=tuple(json.loads(row["provenance_json"])),
        )

    def put_evidence(self, evidence: EvidenceRef) -> None:
        self.conn.execute(
            "INSERT INTO evidence VALUES(?,?,?,?)",
            (evidence.evidence_id, evidence.kind, evidence.source_ref, evidence.content_hash),
        )
        self.conn.commit()

    def attach_evidence(self, claim_id: str, evidence_id: str, admitted: bool = False) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO claim_evidence(claim_id,evidence_id,admitted) VALUES(?,?,?)",
            (claim_id, evidence_id, int(admitted)),
        )
        self.conn.commit()

    def transition_status(self, claim_id: str, to_status: EpistemicStatus, *, reason: str,
                          evidence_ids: Iterable[str] = ()) -> None:
        row = self.conn.execute("SELECT epistemic_status FROM claims WHERE claim_id=?", (claim_id,)).fetchone()
        if row is None:
            raise KeyError(claim_id)
        old = EpistemicStatus(row[0])
        if to_status not in _ALLOWED_PROMOTIONS[old]:
            raise SemanticError(f"epistemic transition not admitted: {old.value}->{to_status.value}")
        eids = tuple(evidence_ids)
        if to_status in {EpistemicStatus.SUPPORTED, EpistemicStatus.VALIDATED, EpistemicStatus.PROVEN}:
            if not eids:
                raise SemanticError("status promotion requires explicitly admitted evidence/proof references")
            placeholders = ",".join("?" for _ in eids)
            rows = self.conn.execute(
                f"SELECT evidence_id FROM claim_evidence WHERE claim_id=? AND admitted=1 AND evidence_id IN ({placeholders})",
                (claim_id, *eids),
            ).fetchall()
            if len(rows) != len(set(eids)):
                raise SemanticError("promotion references evidence not explicitly admitted to the claim")
        self.conn.execute("UPDATE claims SET epistemic_status=? WHERE claim_id=?", (to_status.value, claim_id))
        self.conn.execute(
            "INSERT INTO transitions(claim_id,from_status,to_status,reason,evidence_json) VALUES(?,?,?,?,?)",
            (claim_id, old.value, to_status.value, reason, json.dumps(eids)),
        )
        self.conn.commit()

    def add_dependency(self, source_ref: str, target_ref: str, kind: str, required: bool = True) -> None:
        self.conn.execute(
            "INSERT OR IGNORE INTO dependencies VALUES(?,?,?,?)",
            (source_ref, target_ref, kind, int(required)),
        )
        self.conn.commit()

    def affected_by(self, target_ref: str) -> set[str]:
        seen: set[str] = set()
        frontier = [target_ref]
        while frontier:
            target = frontier.pop()
            for row in self.conn.execute("SELECT source_ref FROM dependencies WHERE target_ref=?", (target,)):
                source = row[0]
                if source not in seen:
                    seen.add(source)
                    frontier.append(source)
        return seen

    def record_correction(self, claim_id: str, note: str, *, supersedes_claim_id: str | None = None,
                          counterexample_ref: str | None = None) -> None:
        self.conn.execute(
            "INSERT INTO corrections(claim_id,supersedes_claim_id,counterexample_ref,note) VALUES(?,?,?,?)",
            (claim_id, supersedes_claim_id, counterexample_ref, note),
        )
        self.conn.commit()
