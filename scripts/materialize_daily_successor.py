#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import date
from pathlib import Path
from typing import Any

ROLES = ("User", "System", "Technical", "Annexure", "Theories")
MIN_REVIEW_FAMILIES = 3


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_root(rows: list[dict[str, Any]]) -> str:
    material = sorted(
        ({"role": r["role"], "name": r["name"], "bytes": r["bytes"], "sha256": r["sha256"]} for r in rows),
        key=lambda r: (r["role"], r["name"]),
    )
    return sha256_bytes(canonical_json(material))


def safe_version_token(release: str) -> str:
    m = re.fullmatch(r"Garden\s+(v\d+\.\d+(?:\.\d+)?)", release.strip())
    if not m:
        raise ValueError(f"unsupported candidate release: {release}")
    return m.group(1)


def validate_review_manifest(payload: dict[str, Any], predecessor_root: str, today: str) -> tuple[str, list[str]]:
    failures: list[str] = []
    if payload.get("schema") != "GardenDailyAdmittedDeltaManifest/v1":
        failures.append("REVIEW_MANIFEST_SCHEMA_INVALID")
    if payload.get("predecessor_source_root_sha256") != predecessor_root:
        failures.append("PREDECESSOR_SOURCE_ROOT_MISMATCH")
    if payload.get("date") != today:
        failures.append("DAILY_MANIFEST_DATE_MISMATCH")
    release = str(payload.get("candidate_release", ""))
    try:
        safe_version_token(release)
    except ValueError:
        failures.append("CANDIDATE_RELEASE_INVALID")
    deltas = payload.get("deltas") or []
    if not deltas:
        return release, failures + ["NO_SEMANTIC_RELEASE"]
    ids: set[str] = set()
    for row in deltas:
        delta_id = str(row.get("delta_id", ""))
        if not delta_id or delta_id in ids:
            failures.append(f"DELTA_ID_INVALID_OR_DUPLICATE:{delta_id}")
        ids.add(delta_id)
        blind = set(str(x) for x in row.get("independent_reviewer_families") or [])
        final = set(str(x) for x in row.get("cross_examination_families") or [])
        if len(blind) < MIN_REVIEW_FAMILIES:
            failures.append(f"INSUFFICIENT_INDEPENDENT_REVIEW:{delta_id}")
        if len(final) < MIN_REVIEW_FAMILIES:
            failures.append(f"INSUFFICIENT_PEER_CROSS_EXAMINATION:{delta_id}")
        if not final.issubset(blind):
            failures.append(f"CROSS_EXAMINATION_FAMILY_NOT_BLIND_REVIEWER:{delta_id}")
        if row.get("gsl_admission") != "PASS":
            failures.append(f"GSL_ADMISSION_NOT_PASS:{delta_id}")
        if row.get("semantic_delta_admitted") is not True:
            failures.append(f"DELTA_NOT_EXPLICITLY_ADMITTED:{delta_id}")
    return release, failures


def candidate_rows(staging: Path, release: str, release_date: str) -> tuple[list[dict[str, Any]], list[str]]:
    token = safe_version_token(release)
    rows: list[dict[str, Any]] = []
    failures: list[str] = []
    expected_names = set()
    for role in ROLES:
        name = f"Garden_{role}_{token}_FULL_{release_date}.txt"
        expected_names.add(name)
        path = staging / name
        if not path.is_file():
            failures.append(f"MISSING_CANDIDATE_FILE:{name}")
            continue
        data = path.read_bytes()
        if not data.strip():
            failures.append(f"EMPTY_CANDIDATE_FILE:{name}")
            continue
        rows.append({"role": role, "name": name, "bytes": len(data), "sha256": sha256_bytes(data)})
    extras = sorted(p.name for p in staging.glob("Garden_*_FULL_*.txt") if p.name not in expected_names)
    failures.extend(f"UNEXPECTED_CANDIDATE_FILE:{name}" for name in extras)
    return rows, failures


def archive_current_candidate(root: Path) -> str | None:
    current = root / "canonical" / "candidates" / "current"
    manifest_path = current / "SOURCE_MANIFEST.json"
    if not manifest_path.is_file():
        return None
    manifest = load_json(manifest_path)
    release = str(manifest.get("release", "UNKNOWN")).replace(" ", "-")
    candidate_date = str(manifest.get("date", "UNKNOWN"))
    root_short = str(manifest.get("source_root_sha256", "UNKNOWN"))[:12]
    archive_id = f"{release}_{candidate_date}_{root_short}"
    archive = root / "canonical" / "archive" / "candidates" / archive_id
    if archive.exists():
        raise RuntimeError(f"archive destination already exists: {archive.relative_to(root)}")
    archive.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(current), str(archive))
    return archive.relative_to(root).as_posix()


def materialize(root: Path, staging: Path, review_manifest_path: Path, *, apply: bool) -> dict[str, Any]:
    canonical_manifest = load_json(root / "canonical" / "current" / "SOURCE_MANIFEST.json")
    predecessor_root = str(canonical_manifest["source_root_sha256"])
    review = load_json(review_manifest_path)
    release_date = str(review.get("date") or date.today().isoformat())
    release, failures = validate_review_manifest(review, predecessor_root, release_date)
    if "NO_SEMANTIC_RELEASE" in failures:
        return {
            "schema":"GardenDailyMaterializationReceipt/v1",
            "result":"NO_SEMANTIC_RELEASE",
            "date":release_date,
            "predecessor_source_root_sha256":predecessor_root,
            "failures":[x for x in failures if x != "NO_SEMANTIC_RELEASE"],
            "wrote_files":False,
        }
    rows, file_failures = candidate_rows(staging, release, release_date)
    failures.extend(file_failures)
    if failures:
        return {"schema":"GardenDailyMaterializationReceipt/v1","result":"REJECT","date":release_date,"candidate_release":release,"predecessor_source_root_sha256":predecessor_root,"failures":failures,"wrote_files":False}

    candidate_root = source_root(rows)
    manifest = {
        "schema":"GardenCandidateSourceManifest/v1",
        "release":release,
        "gsl":canonical_manifest.get("gsl"),
        "date":release_date,
        "predecessor_release":canonical_manifest.get("release"),
        "predecessor_source_root_sha256":predecessor_root,
        "files":{r["role"]:{"name":r["name"],"bytes":r["bytes"],"sha256":r["sha256"]} for r in rows},
        "source_root_algorithm":"sha256(canonical-json(sorted role/name/bytes/sha256 rows))",
        "source_root_sha256":candidate_root,
        "status":"SUCCESSOR_CANDIDATE_NOT_CANONICAL",
        "canonical_promotion_authorized":False,
        "review_manifest_sha256":sha256_bytes(review_manifest_path.read_bytes()),
    }
    receipt = {
        "schema":"GardenDailyMaterializationReceipt/v1",
        "result":"READY_TO_MATERIALIZE" if not apply else "MATERIALIZED_CANDIDATE",
        "date":release_date,
        "candidate_release":release,
        "predecessor_source_root_sha256":predecessor_root,
        "candidate_source_root_sha256":candidate_root,
        "admitted_delta_ids":[str(x["delta_id"]) for x in review["deltas"]],
        "review_family_floor":MIN_REVIEW_FAMILIES,
        "canonical_promotion_authorized":False,
        "wrote_files":apply,
        "failures":[],
    }
    if not apply:
        return receipt

    archived = archive_current_candidate(root)
    current = root / "canonical" / "candidates" / "current"
    current.mkdir(parents=True, exist_ok=False)
    for r in rows:
        shutil.copy2(staging / r["name"], current / r["name"])
    (current / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (current / "ADMITTED_DELTAS.json").write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    history_dir = root / "canonical" / "history"
    history_dir.mkdir(parents=True, exist_ok=True)
    history_path = history_dir / "VERSION_HISTORY.json"
    if history_path.is_file():
        history = load_json(history_path)
    else:
        history = {"schema":"GardenVersionHistory/v1","entries":[]}
    if any(x.get("date") == release_date and x.get("release") == release for x in history.get("entries") or []):
        raise RuntimeError("daily version history already contains this release/date")
    history.setdefault("entries", []).append({
        "release":release,
        "date":release_date,
        "status":"SUCCESSOR_CANDIDATE_NOT_CANONICAL",
        "source_root_sha256":candidate_root,
        "predecessor_source_root_sha256":predecessor_root,
        "archived_previous_candidate":archived,
        "canonical_promotion_authorized":False,
    })
    history_path.write_text(json.dumps(history, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    receipt["archived_previous_candidate"] = archived
    receipt["candidate_path"] = current.relative_to(root).as_posix()
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--staging-dir", required=True)
    parser.add_argument("--review-manifest", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--output", default="/tmp/garden-daily-materialization-receipt.json")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    staging = (root / args.staging_dir).resolve() if not Path(args.staging_dir).is_absolute() else Path(args.staging_dir).resolve()
    review = (root / args.review_manifest).resolve() if not Path(args.review_manifest).is_absolute() else Path(args.review_manifest).resolve()
    receipt = materialize(root, staging, review, apply=args.apply)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(receipt, sort_keys=True))
    return 0 if receipt["result"] in {"READY_TO_MATERIALIZE","MATERIALIZED_CANDIDATE","NO_SEMANTIC_RELEASE"} and not receipt.get("failures") else 1


if __name__ == "__main__":
    raise SystemExit(main())
