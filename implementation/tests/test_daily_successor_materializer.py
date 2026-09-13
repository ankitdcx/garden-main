from __future__ import annotations

import json
from pathlib import Path

from scripts.materialize_daily_successor import materialize, source_root


ROLES = ("User", "System", "Technical", "Annexure", "Theories")
DATE = "2026-09-13"


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def fixture_repo(tmp_path: Path) -> tuple[Path, Path, Path]:
    root = tmp_path
    current = root / "canonical/current"
    current.mkdir(parents=True)
    predecessor_rows = []
    for role in ROLES:
        name = f"Garden_{role}_v15.5_FULL_2026-09-12.txt"
        data = f"old {role}\n".encode()
        (current / name).write_bytes(data)
        import hashlib
        predecessor_rows.append({"role":role,"name":name,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()})
    predecessor_root = source_root(predecessor_rows)
    write_json(current / "SOURCE_MANIFEST.json", {
        "schema":"GardenCanonicalSourceManifest/v1",
        "release":"Garden v15.5",
        "gsl":"v45.1",
        "date":"2026-09-12",
        "files":{r["role"]:{k:r[k] for k in ("name","bytes","sha256")} for r in predecessor_rows},
        "source_root_sha256":predecessor_root,
    })

    staging = root / "staging"
    staging.mkdir()
    for role in ROLES:
        (staging / f"Garden_{role}_v15.6_FULL_{DATE}.txt").write_text(f"new {role}\n", encoding="utf-8")
    review_path = root / "review.json"
    write_json(review_path, {
        "schema":"GardenDailyAdmittedDeltaManifest/v1",
        "date":DATE,
        "candidate_release":"Garden v15.6",
        "predecessor_source_root_sha256":predecessor_root,
        "deltas":[{
            "delta_id":"D-1",
            "independent_reviewer_families":["chatgpt","gemini","deepseek"],
            "cross_examination_families":["chatgpt","gemini","deepseek"],
            "gsl_admission":"PASS",
            "semantic_delta_admitted":True,
        }],
    })
    return root, staging, review_path


def test_dry_run_requires_three_reviewers_and_does_not_write(tmp_path: Path):
    root, staging, review = fixture_repo(tmp_path)
    payload = json.loads(review.read_text())
    payload["deltas"][0]["independent_reviewer_families"] = ["chatgpt", "gemini"]
    write_json(review, payload)
    receipt = materialize(root, staging, review, apply=False)
    assert receipt["result"] == "REJECT"
    assert any(x.startswith("INSUFFICIENT_INDEPENDENT_REVIEW") for x in receipt["failures"])
    assert not (root / "canonical/candidates/current").exists()


def test_materializes_complete_candidate_without_touching_canonical_current(tmp_path: Path):
    root, staging, review = fixture_repo(tmp_path)
    old_manifest = (root / "canonical/current/SOURCE_MANIFEST.json").read_bytes()
    receipt = materialize(root, staging, review, apply=True)
    assert receipt["result"] == "MATERIALIZED_CANDIDATE"
    assert receipt["canonical_promotion_authorized"] is False
    assert (root / "canonical/current/SOURCE_MANIFEST.json").read_bytes() == old_manifest
    candidate = root / "canonical/candidates/current"
    assert (candidate / "SOURCE_MANIFEST.json").is_file()
    assert len(list(candidate.glob("Garden_*_FULL_*.txt"))) == 5
    history = json.loads((root / "canonical/history/VERSION_HISTORY.json").read_text())
    assert history["entries"][-1]["release"] == "Garden v15.6"
    assert history["entries"][-1]["status"] == "SUCCESSOR_CANDIDATE_NOT_CANONICAL"


def test_second_candidate_archives_first_candidate(tmp_path: Path):
    root, staging, review = fixture_repo(tmp_path)
    first = materialize(root, staging, review, apply=True)
    assert first["result"] == "MATERIALIZED_CANDIDATE"

    # New day/new candidate version remains based on the immutable canonical predecessor;
    # lineage to the previous candidate is preserved through the explicit archive/history record.
    payload = json.loads(review.read_text())
    payload["date"] = "2026-09-14"
    payload["candidate_release"] = "Garden v15.7"
    write_json(review, payload)
    staging2 = root / "staging2"
    staging2.mkdir()
    for role in ROLES:
        (staging2 / f"Garden_{role}_v15.7_FULL_2026-09-14.txt").write_text(f"next {role}\n", encoding="utf-8")
    second = materialize(root, staging2, review, apply=True)
    assert second["result"] == "MATERIALIZED_CANDIDATE"
    assert second["archived_previous_candidate"]
    archive = root / second["archived_previous_candidate"]
    assert (archive / "SOURCE_MANIFEST.json").is_file()
    history = json.loads((root / "canonical/history/VERSION_HISTORY.json").read_text())
    assert [x["release"] for x in history["entries"]] == ["Garden v15.6", "Garden v15.7"]
