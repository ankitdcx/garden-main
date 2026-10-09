#!/usr/bin/env python3
"""Read-only Garden design-corpus structural checker (stdlib only)."""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
problems = []
counts = {"json": 0, "markdown": 0, "local_links": 0, "source_files": 0, "indexed_paths": 0}

def issue(kind, location, detail):
    problems.append((kind, str(location), str(detail)))

def read_json(path):
    counts["json"] += 1
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeError, OSError, json.JSONDecodeError) as exc:
        issue("INVALID_JSON", path.relative_to(ROOT), exc)
        return None

def local_path(ref):
    return isinstance(ref, str) and ref.startswith(("canonical/", "design_deltas/"))

def verify_ref(ref, location):
    counts["indexed_paths"] += 1
    if not (ROOT / ref).exists():
        issue("MISSING_INDEX_PATH", location, ref)

# All JSON must parse, including historical candidate sets.
for p in sorted(ROOT.rglob("*.json")):
    read_json(p)

# Markdown file/directory links only; remote URLs and heading anchors excluded.
for p in sorted(ROOT.rglob("*.md")):
    counts["markdown"] += 1
    try:
        body = p.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        issue("UNREADABLE_MARKDOWN", p.relative_to(ROOT), exc)
        continue
    # Inline Markdown links and images; do not treat code examples as references.
    body = re.sub(r"(?ms)^```.*?^```", "", body)
    for match in re.finditer(r"!?(?:\[[^\]]*\])\(([^)]+)\)", body):
        raw = match.group(1).strip().strip("<>")
        if raw.startswith(("https://", "http://", "mailto:", "#", "data:")):
            continue
        target = unquote(raw.split("#", 1)[0].split("?", 1)[0])
        if not target:
            continue
        counts["local_links"] += 1
        if not (p.parent / target).exists():
            issue("BROKEN_MARKDOWN_LINK", p.relative_to(ROOT), raw)

# Index paths: only fields declared as file/directory locators, not historical prose.
idx = ROOT / "CORPUS_INDEX.json"
if idx.exists():
    obj = read_json(idx)
    if isinstance(obj, dict):
        def scan(value, key=""):
            if isinstance(value, dict):
                for k, v in value.items():
                    scan(v, k)
            elif isinstance(value, list):
                for v in value:
                    scan(v, key)
            elif local_path(value) and (
                key == "path" or key.endswith("_path") or key in {
                    "readme", "companion_candidate_note",
                    "invariant_driven_theory_discovery", "recursive_discovery_compression"
                }
            ):
                verify_ref(value, idx.relative_to(ROOT))
        scan(obj)
        ids = [v.get("id") for v in obj.get("additive_candidates", []) if isinstance(v, dict)]
        if len(ids) != len(set(ids)):
            issue("DUPLICATE_CANDIDATE_ID", idx.relative_to(ROOT), "duplicate additive candidate IDs")
        if obj.get("canonical", {}).get("id") != "Garden-v15.5":
            issue("CANONICAL_INDEX_DRIFT", idx.relative_to(ROOT), "canonical index not v15.5")

# Exact byte-length and SHA-256 verification for frozen five-file source manifests.
for manifest in sorted(ROOT.glob("canonical/**/SOURCE_MANIFEST.json")):
    obj = read_json(manifest)
    if not isinstance(obj, dict):
        continue
    entries = obj.get("files", {})
    if not isinstance(entries, dict) or set(entries) != {"User", "System", "Technical", "Annexure", "Theories"}:
        issue("SOURCE_MANIFEST_ROLES", manifest.relative_to(ROOT), "expected exactly five source roles")
        continue
    for role, entry in entries.items():
        if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
            issue("INVALID_MANIFEST_ENTRY", manifest.relative_to(ROOT), role)
            continue
        p = manifest.parent / entry["name"]
        if not p.is_file():
            issue("MISSING_SOURCE", manifest.relative_to(ROOT), entry["name"])
            continue
        data = p.read_bytes()
        counts["source_files"] += 1
        if len(data) != entry.get("bytes"):
            issue("SOURCE_BYTES_MISMATCH", p.relative_to(ROOT), f"{len(data)} != {entry.get('bytes')}")
        digest = hashlib.sha256(data).hexdigest()
        if digest != entry.get("sha256"):
            issue("SOURCE_HASH_MISMATCH", p.relative_to(ROOT), f"{digest} != {entry.get('sha256')}")

pointer = ROOT / "canonical/candidates/CURRENT_CANDIDATE.json"
if pointer.is_file():
    obj = read_json(pointer)
    if isinstance(obj, dict):
        if obj.get("canonical") is not False:
            issue("CANDIDATE_POINTER_STATUS", pointer.relative_to(ROOT), "must remain noncanonical")
        ref = obj.get("manifest")
        if local_path(ref):
            verify_ref(ref, pointer.relative_to(ROOT))

print("Garden structural integrity check (read-only)")
for key, value in counts.items():
    print(f"  {key}: {value}")
if problems:
    for kind, location, detail in problems:
        print(f"FAIL [{kind}] {location}: {detail}")
    print(f"FAIL: {len(problems)} structural issue(s)")
    sys.exit(1)
print("PASS: checked structural constraints only; no semantic or admission claim")
