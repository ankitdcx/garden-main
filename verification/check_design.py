"""Verify the Garden design repository with the Python standard library."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ROLES = {"User", "System", "Technical", "Annexure", "Theories"}
RELEASE_ROOT = "63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_bytes())


def verify_roles(directory, rows, expected_root):
    rows = sorted(rows, key=lambda row: row["role"])
    require(len(rows) == 5 and {r["role"] for r in rows} == ROLES, f"role set in {directory}")
    require({p.name for p in directory.glob("Garden_*.txt")} == {r["name"] for r in rows},
            f"source file set differs in {directory}")
    for row in rows:
        path = directory / row["name"]
        data = path.read_bytes()
        require(len(data) == row["bytes"] and digest(data) == row["sha256"], f"source identity: {path}")
    encoded = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    require(digest(encoded) == expected_root, f"source root in {directory}")


def verify_receipt(actual, expected):
    require(actual.get("status") == "PASS", "closure scanner did not return PASS")
    require(actual == expected, "closure receipt differs from the reference receipt")


def verify_release(directory):
    manifest = read_json(directory / "SOURCE_MANIFEST.json")
    require(manifest["source_root_sha256"] == RELEASE_ROOT, "unexpected v15.5 release identity")
    verify_roles(directory, [dict(role=k, **v) for k, v in manifest["files"].items()], RELEASE_ROOT)
    archive = ROOT / "verification/v15.5"
    output = subprocess.check_output(
        [sys.executable, str(archive / "garden_reference_closure_v15_5.py"), str(directory)]
    )
    verify_receipt(json.loads(output), read_json(archive / "Garden_v15.5_ReferenceClosureReceipt_2026-09-12.json"))


def verify_candidates():
    for version in ("v15.6", "v15.7"):
        directory = ROOT / "canonical/candidates" / version
        manifest = read_json(directory / "EDITION_MANIFEST.json")
        verify_roles(directory, manifest["roles"], manifest["current_source_root"])

    rep = ROOT / "design_deltas/v15.11/rep"
    manifest = read_json(rep / "CANDIDATE_MANIFEST.json")
    doc = manifest["candidate_document"]
    content = (rep / doc["path"]).read_bytes()
    require(digest(content) == doc["sha256"], "REP candidate source identity")
    for key, pattern in (("invariants", r"^### (REPESC-\d+) "), ("tests", r"^\| (TEST-REPESC-\d+) ")):
        ids = re.findall(pattern, content.decode(), re.MULTILINE)
        require(ids and len(ids) == len(set(ids)) and ids == manifest[key], f"REP {key} disagree with source")
    table = read_json(ROOT / "design_deltas/v15.10/GCSC_RELATION_SIGNATURE_CANDIDATE.json")
    objects = set(table["objects"])
    require(len(objects) == 10 and len(table["signatures"]) == 24, "relation signature inventory")
    for name, signature in table["signatures"].items():
        for side in ("source", "target"):
            require(set(signature[side]) <= objects, f"{name} has undeclared {side} objects")
    require({"scope", "validity", "authority_ref"} <= set(table["signatures"]["delegates"]["required_qualifiers"]),
            "missing delegation qualifier")


def verify_recovery():
    path = ROOT / "design_deltas/v15.9.1/COMPLETE_SUFFIX_CROSSWALK.md"
    data = path.read_bytes()
    sections = re.split(rb"(?m)^## (User|System|Technical|Theories|Annexure)\n", data)
    require(len(sections) == 11 and {s.decode() for s in sections[1::2]} == ROLES, "suffix sections")
    rows = re.findall(rb"(?m)^\| \[([A-Za-z]+)\]\(#[a-z]+\) \| [^|]+ \| \[(\d+), (\d+)\) \| (\d+) \|$", sections[0])
    require(len(rows) == 5, "suffix range inventory")
    offsets = {role: (int(start), int(end), int(size)) for role, start, end, size in rows}
    for role, section in zip(sections[1::2], sections[2::2]):
        hashes = re.findall(rb"Suffix SHA-256: `([0-9a-f]{64})`", section)
        blocks = re.findall(rb"(?ms)^```text\n(.*?)^```$", section)
        start, end, size = offsets[role]
        require(len(blocks) == 1 and len(blocks[0]) == end - start == size, "suffix byte span")
        require(len(hashes) == 1 and digest(blocks[0]).encode() == hashes[0],
                f"recovered suffix identity: {role.decode()}")


def verify_paths():
    # Scan tracked Markdown and the limited inline relative-file syntax used in these guides.
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    for name in tracked:
        path = ROOT / name
        if path.suffix == ".json":
            read_json(path)
        elif path.suffix == ".md":
            for link in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", path.read_text()):
                if link.startswith(("#", "mailto:")) or "://" in link:
                    continue
                target = path.parent / unquote(link.partition("#")[0])
                require(target.exists(), f"broken local link in {name}: {link}")


def main():
    verify_release(ROOT / "canonical/current")
    verify_candidates()
    verify_recovery()
    verify_paths()
    print("PASS: canonical replay, edition identities, candidate metadata, recovered suffixes and document paths")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        sys.exit(f"FAIL: {error}")
