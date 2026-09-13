from __future__ import annotations

import hashlib
import json
from pathlib import Path

from scripts.materialize_daily_successor import materialize, source_root


ROLES = ("User", "System", "Technical", "Annexure", "Theories")
DATE = "2026-09-13"


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def fixture_repo(tmp_path: Path) -> tuple[Path, Path, Path, str]:
    root = tmp_path
    current = root / "canonical/current"
    current.mkdir(parents=True)
    predecessor_rows = []
    for role in ROLES:
        name = f"Garden_{role}_v15.5_FULL_2026-09-12.txt"
        data = f"old {role}\n".encode()
        (current / name).write_bytes(data)
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
        "canonical_baseline_source_root_sha256":predecessor_root,
        "predecessor_release":"Garden v15.5",
        "predecessor_source_root_sha256":predecessor_root,
        "deltas":[{
            "delta_id":"D-1",
            "independent_reviewer_families":["chatgpt","gemini","deepseek"],
            "cross_examination_families":["chatgpt","gemini","deepseek"],
            "gsl_admission":"PASS",
            "semantic_delta_admitted":True,
        }],
    })
    return root, staging, review_path, predecessor_root


def test_dry_run_requires_three_reviewers_and_does_not_write(tmp_path: Path):
    root, staging, review, _ = fixture_repo(tmp_path)
    payload = json.loads(review.read_text())
    payload["deltas"][0]["independent_reviewer_families"] = ["chatgpt", "gemini"]
    write_json(review, payload)
    receipt = materialize(root, staging, review, apply=False)
    assert receipt["result"] == "REJECT"
    assert any(x.startswith("INSUFFICIENT_INDEPENDENT_REVIEW") for x in receipt["failures"])
    assert not (root / "canonical/candidates/current").exists()


def test_materializes_complete_candidate_without_touching_canonical_current(tmp_path: Path):
    root, staging, review, canonical_root = fixture_repo(tmp_path)
    old_manifest = (root / "canonical/current/SOURCE_MANIFEST.json").read_bytes()
    receipt = materialize(root, staging, review, apply=True)
    assert receipt["result"] == "MATERIALIZED_CANDIDATE"
    assert receipt["canonical_promotion_authorized"] is False
    assert receipt["predecessor_kind"] == "CANONICAL"
    assert receipt["predecessor_source_root_sha256"] == canonical_root
    assert (root / "canonical/current/SOURCE_MANIFEST.json").read_bytes() == old_manifest
    candidate = root / "canonical/candidates/current"
    manifest = json.loads((candidate / "SOURCE_MANIFEST.json").read_text())
    assert manifest["schema"] == "GardenCandidateSourceManifest/v2"
    assert manifest["canonical_baseline_source_root_sha256"] == canonical_root
    assert manifest["predecessor_source_root_sha256"] == canonical_root
    assert len(list(candidate.glob("Garden_*_FULL_*.txt"))) == 5
    history = json.loads((root / "canonical/history/VERSION_HISTORY.json").read_text())
    assert history["entries"][-1]["release"] == "Garden v15.6"
    assert history["entries"][-1]["status"] == "SUCCESSOR_CANDIDATE_NOT_CANONICAL"


def test_second_candidate_requires_and_binds_first_candidate_as_predecessor(tmp_path: Path):
    root, staging, review, canonical_root = fixture_repo(tmp_path)
    first = materialize(root, staging, review, apply=True)
    assert first["result"] == "MATERIALIZED_CANDIDATE"
    first_root = first["candidate_source_root_sha256"]

    payload = json.loads(review.read_text())
    payload["date"] = "2026-09-14"
    payload["candidate_release"] = "Garden v15.7"
    payload["predecessor_release"] = "Garden v15.6"
    payload["predecessor_source_root_sha256"] = first_root
    payload["canonical_baseline_source_root_sha256"] = canonical_root
    write_json(review, payload)
    staging2 = root / "staging2"
    staging2.mkdir()
    for role in ROLES:
        (staging2 / f"Garden_{role}_v15.7_FULL_2026-09-14.txt").write_text(f"next {role}\n", encoding="utf-8")

    second = materialize(root, staging2, review, apply=True)
    assert second["result"] == "MATERIALIZED_CANDIDATE"
    assert second["predecessor_release"] == "Garden v15.6"
    assert second["predecessor_source_root_sha256"] == first_root
    assert second["predecessor_kind"] == "SUCCESSOR_CANDIDATE"
    assert second["canonical_baseline_source_root_sha256"] == canonical_root
    assert second["archived_previous_candidate"]
    archive = root / second["archived_previous_candidate"]
    archived_manifest = json.loads((archive / "SOURCE_MANIFEST.json").read_text())
    assert archived_manifest["source_root_sha256"] == first_root

    current_manifest = json.loads((root / "canonical/candidates/current/SOURCE_MANIFEST.json").read_text())
    assert current_manifest["predecessor_release"] == "Garden v15.6"
    assert current_manifest["predecessor_source_root_sha256"] == first_root
    assert current_manifest["canonical_baseline_source_root_sha256"] == canonical_root

    history = json.loads((root / "canonical/history/VERSION_HISTORY.json").read_text())
    assert [x["release"] for x in history["entries"]] == ["Garden v15.6", "Garden v15.7"]
    assert history["entries"][-1]["predecessor_source_root_sha256"] == first_root


def test_second_candidate_rejects_if_it_rebases_on_canonical_instead_of_previous_candidate(tmp_path: Path):
    root, staging, review, canonical_root = fixture_repo(tmp_path)
    first = materialize(root, staging, review, apply=True)
    assert first["result"] == "MATERIALIZED_CANDIDATE"

    payload = json.loads(review.read_text())
    payload["date"] = "2026-09-14"
    payload["candidate_release"] = "Garden v15.7"
    payload["predecessor_release"] = "Garden v15.5"
    payload["predecessor_source_root_sha256"] = canonical_root
    write_json(review, payload)
    staging2 = root / "staging2"
    staging2.mkdir()
    for role in ROLES:
        (staging2 / f"Garden_{role}_v15.7_FULL_2026-09-14.txt").write_text(f"next {role}\n", encoding="utf-8")

    receipt = materialize(root, staging2, review, apply=False)
    assert receipt["result"] == "REJECT"
    assert "PREDECESSOR_SOURCE_ROOT_MISMATCH" in receipt["failures"]
    assert "PREDECESSOR_RELEASE_MISMATCH" in receipt["failures"]
