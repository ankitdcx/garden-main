#!/usr/bin/env python3
"""PR gate for garden-main multi-agent integration provenance.

Binds the PR's AgentWorkIntent/v1 to the protected base commit and the base
canonical/current source manifest, checks declared paths against the actual diff,
and compares concurrent PR intents. It never merges, promotes canon, or grants
authority.
"""
from __future__ import annotations

import base64
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Mapping
from urllib import parse, request

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from implementation.garden_kernel.integration_provenance import (  # noqa: E402
    AgentWorkIntent,
    assess_intents,
    normalize_path,
    validate_current_binding,
)

INTENT_MARKER = "<!-- GARDEN_AGENT_WORK_INTENT -->"
RECEIPT_MARKER = "<!-- GARDEN_INTEGRATION_RECEIPT -->"
MANIFEST_PATH = "canonical/current/SOURCE_MANIFEST.json"


def extract_json_block(body: str | None, marker: str) -> Mapping[str, Any] | None:
    if not body or marker not in body:
        return None
    tail = body.split(marker, 1)[1]
    match = re.search(r"```(?:json)?\s*\n(.*?)\n```", tail, flags=re.DOTALL | re.IGNORECASE)
    if not match:
        raise ValueError(f"{marker} must be followed by a fenced JSON object")
    data = json.loads(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"{marker} block must contain a JSON object")
    return data


def _covers(declared: str, actual: str) -> bool:
    d, a = normalize_path(declared), normalize_path(actual)
    return d == a or a.startswith(d + "/")


def undeclared_paths(intent: AgentWorkIntent, changed_paths: list[str]) -> list[str]:
    return sorted(path for path in changed_paths if not any(_covers(d, path) for d in intent.target_paths))


def direct_path_overlap(a: list[str], b: list[str]) -> bool:
    aa = [normalize_path(x) for x in a]
    bb = [normalize_path(x) for x in b]
    return any(x == y or x.startswith(y + "/") or y.startswith(x + "/") for x in aa for y in bb)


def expected_binding(manifest: Mapping[str, Any], base_sha: str) -> dict[str, str]:
    source_root = str(manifest.get("source_root_sha256", "")).lower()
    release = str(manifest.get("release", "")).strip()
    if not re.fullmatch(r"[0-9a-f]{64}", source_root):
        raise ValueError("base canonical source manifest has invalid source_root_sha256")
    if not release.startswith("Garden v"):
        raise ValueError("base canonical source manifest has unexpected release")
    return {
        "base_sha": base_sha.lower(),
        "source_root_sha256": source_root,
        "design_epoch_ref": f"Garden-{release.split()[-1]}@{source_root}",
    }


def evaluate_pr(
    *,
    current_pr_number: int,
    current_body: str | None,
    current_changed_paths: list[str],
    concurrent_prs: list[dict[str, Any]],
    base_binding: Mapping[str, str],
) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []
    intent_data = extract_json_block(current_body, INTENT_MARKER)
    if intent_data is None:
        return {
            "schema": "GardenMainPRIntegrationCheck/v1",
            "pr": current_pr_number,
            "disposition": "BLOCKED",
            "failures": ["MISSING_AGENT_WORK_INTENT"],
            "warnings": [],
            "authority_effect": "NONE_PROPOSAL_ONLY",
        }
    current = AgentWorkIntent.from_mapping(intent_data)
    failures.extend(validate_current_binding(current, **dict(base_binding)))

    undeclared = undeclared_paths(current, current_changed_paths)
    if undeclared:
        failures.append("UNDECLARED_CHANGED_PATHS:" + ",".join(undeclared))

    other_intents: list[AgentWorkIntent] = []
    unknown_direct: list[int] = []
    for pr in concurrent_prs:
        if int(pr["number"]) == current_pr_number:
            continue
        other_data = extract_json_block(pr.get("body"), INTENT_MARKER)
        if other_data is None:
            if direct_path_overlap(current_changed_paths, list(pr.get("changed_paths") or [])):
                unknown_direct.append(int(pr["number"]))
            else:
                warnings.append(f"PR#{pr['number']}:NO_DECLARED_INTENT_SEMANTIC_OVERLAP_UNKNOWN")
            continue
        try:
            other_intents.append(AgentWorkIntent.from_mapping(other_data))
        except ValueError as exc:
            warnings.append(f"PR#{pr['number']}:INVALID_OR_LEGACY_INTENT:{exc}")

    if unknown_direct:
        failures.append("UNKNOWN_CONCURRENT_INTENT_DIRECT_PATH_OVERLAP:" + ",".join(map(str, sorted(unknown_direct))))

    receipt = extract_json_block(current_body, RECEIPT_MARKER)
    guard = assess_intents(current, other_intents, receipt)
    if guard["disposition"] != "PASS":
        failures.append("INTEGRATION_GUARD:" + guard["disposition"])

    return {
        "schema": "GardenMainPRIntegrationCheck/v1",
        "pr": current_pr_number,
        "current_intent_id": current.intent_id,
        "current_intent_hash": current.evidence_hash(),
        "work_package_id": current.work_package_id,
        "base_binding": dict(base_binding),
        "changed_paths": sorted(current_changed_paths),
        "guard": guard,
        "disposition": "BLOCKED" if failures else "PASS",
        "failures": failures,
        "warnings": warnings,
        "authority_effect": "NONE_PROPOSAL_ONLY",
        "canonical_effect": "NONE",
        "uncertainty": "Legacy/concurrent PRs without a valid AgentWorkIntent/v1 can only be checked for direct path overlap. Cross-file semantic absence is not inferred.",
    }


def _api_json(url: str, token: str) -> Any:
    req = request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "garden-main-integration-provenance",
    })
    with request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def _pr_files(api_url: str, token: str, number: int) -> list[str]:
    files: list[str] = []
    page = 1
    while True:
        data = _api_json(f"{api_url}/pulls/{number}/files?per_page=100&page={page}", token)
        files.extend(item["filename"] for item in data)
        if len(data) < 100:
            return files
        page += 1


def _base_manifest(api_url: str, token: str, base_sha: str) -> Mapping[str, Any]:
    encoded_path = parse.quote(MANIFEST_PATH, safe="/")
    data = _api_json(f"{api_url}/contents/{encoded_path}?ref={base_sha}", token)
    if data.get("encoding") != "base64" or not data.get("content"):
        raise ValueError("unable to resolve base canonical source manifest")
    manifest = json.loads(base64.b64decode(data["content"]).decode("utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("base canonical source manifest must be a JSON object")
    return manifest


def main() -> int:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    repository = os.environ.get("GITHUB_REPOSITORY")
    token = os.environ.get("GITHUB_TOKEN")
    api_root = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    if not event_path or not repository or not token:
        raise SystemExit("GITHUB_EVENT_PATH, GITHUB_REPOSITORY and GITHUB_TOKEN are required")
    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    current_pr = event.get("pull_request")
    if not current_pr:
        raise SystemExit("pull_request event required")
    number = int(current_pr["number"])
    base_sha = str(current_pr["base"]["sha"]).lower()
    api_url = f"{api_root}/repos/{repository}"
    binding = expected_binding(_base_manifest(api_url, token, base_sha), base_sha)
    current_files = _pr_files(api_url, token, number)
    pulls = _api_json(f"{api_url}/pulls?state=open&per_page=100", token)
    concurrent: list[dict[str, Any]] = []
    for pr in pulls:
        pr_number = int(pr["number"])
        if pr_number == number:
            continue
        concurrent.append({
            "number": pr_number,
            "body": pr.get("body"),
            "changed_paths": _pr_files(api_url, token, pr_number),
        })
    result = evaluate_pr(
        current_pr_number=number,
        current_body=current_pr.get("body"),
        current_changed_paths=current_files,
        concurrent_prs=concurrent,
        base_binding=binding,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["disposition"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
