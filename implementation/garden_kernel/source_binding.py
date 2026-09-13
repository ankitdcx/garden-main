from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from typing import Iterable

from .core import Obligation


@dataclass(frozen=True)
class SourceBinding:
    binding_key: str
    obligation_id: str
    source_file: str
    source_anchor: str | None
    semantic_hash: str
    owner: str | None
    status: str


def _normalized_text(text: str) -> str:
    return " ".join(text.split())


def binding_key(obligation: Obligation) -> str:
    """Return an identity stable across ordinary line-number movement.

    Canonical definition/schema IDs remain the preferred identity. Extracted free
    normative text falls back to source file + semantic anchor + normalized text,
    deliberately avoiding physical line number as identity.
    """
    if obligation.obligation_id.startswith(("DEF:", "SCHEMA:")):
        return obligation.obligation_id
    raw = "\0".join(
        [
            obligation.source_file,
            obligation.source_anchor or "",
            _normalized_text(obligation.text),
        ]
    ).encode("utf-8")
    return "TEXTSEM:" + hashlib.sha256(raw).hexdigest()


def semantic_hash(obligation: Obligation) -> str:
    payload = {
        "text": _normalized_text(obligation.text),
        "source_anchor": obligation.source_anchor,
        "owner": obligation.owner,
        "dependency_refs": sorted(obligation.dependency_refs),
        "status": obligation.status,
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def build_source_bindings(obligations: Iterable[Obligation]) -> list[SourceBinding]:
    bindings: list[SourceBinding] = []
    for obligation in obligations:
        bindings.append(
            SourceBinding(
                binding_key=binding_key(obligation),
                obligation_id=obligation.obligation_id,
                source_file=obligation.source_file,
                source_anchor=obligation.source_anchor,
                semantic_hash=semantic_hash(obligation),
                owner=obligation.owner,
                status=obligation.status,
            )
        )
    return bindings


def diff_source_bindings(previous: Iterable[SourceBinding], current: Iterable[SourceBinding]) -> dict:
    """Return explicit stale/add/remove candidates between two extraction snapshots."""
    before = {item.binding_key: item for item in previous}
    after = {item.binding_key: item for item in current}

    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(
        key
        for key in set(before) & set(after)
        if before[key].semantic_hash != after[key].semantic_hash
    )
    unchanged = len(set(before) & set(after)) - len(changed)

    return {
        "schema": "GardenSourceBindingDiff/v0.1",
        "added": [asdict(after[key]) for key in added],
        "removed": [asdict(before[key]) for key in removed],
        "changed": [
            {"before": asdict(before[key]), "after": asdict(after[key])}
            for key in changed
        ],
        "unchanged_count": unchanged,
        "stale_binding_keys": sorted(set(removed) | set(changed)),
        "note": (
            "A stale binding key identifies an obligation requiring impact/revalidation review; "
            "it does not by itself prove downstream artifacts are invalid."
        ),
    }
