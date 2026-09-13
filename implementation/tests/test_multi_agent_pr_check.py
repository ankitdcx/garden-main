from scripts.check_multi_agent_pr import (
    INTENT_MARKER,
    evaluate_pr,
    expected_binding,
    extract_json_block,
)

BASE = "1" * 40
ROOT = "2" * 64
EPOCH = f"Garden-v15.5@{ROOT}"


def body(*, paths=None, domains=None, source_root=ROOT, base=BASE, epoch=EPOCH):
    payload = {
        "schema": "AgentWorkIntent/v1",
        "intent_id": "current",
        "agent_id": "agent:test",
        "work_package_id": "WP-TEST",
        "base_sha": base,
        "source_root_sha256": source_root,
        "design_epoch_ref": epoch,
        "target_paths": paths or ["implementation/new.py"],
        "target_symbols": [],
        "semantic_domains": domains or ["test-domain"],
        "affected_invariants": [],
        "affected_contracts": [],
        "intended_effect": "test",
        "parallel_mode": "INDEPENDENT_COMPARISON",
    }
    import json
    return INTENT_MARKER + "\n```json\n" + json.dumps(payload) + "\n```\n"


def binding():
    return {"base_sha": BASE, "source_root_sha256": ROOT, "design_epoch_ref": EPOCH}


def test_expected_binding_uses_manifest_root():
    result = expected_binding({"release": "Garden v15.5", "source_root_sha256": ROOT}, BASE)
    assert result == binding()


def test_extract_requires_marker():
    assert extract_json_block("no marker", INTENT_MARKER) is None


def test_missing_intent_blocks():
    result = evaluate_pr(
        current_pr_number=1,
        current_body="",
        current_changed_paths=["implementation/new.py"],
        concurrent_prs=[],
        base_binding=binding(),
    )
    assert result["disposition"] == "BLOCKED"
    assert "MISSING_AGENT_WORK_INTENT" in result["failures"]


def test_undeclared_actual_change_blocks():
    result = evaluate_pr(
        current_pr_number=1,
        current_body=body(paths=["implementation/new.py"]),
        current_changed_paths=["implementation/new.py", "scripts/extra.py"],
        concurrent_prs=[],
        base_binding=binding(),
    )
    assert result["disposition"] == "BLOCKED"
    assert any(x.startswith("UNDECLARED_CHANGED_PATHS:") for x in result["failures"])


def test_stale_binding_blocks():
    result = evaluate_pr(
        current_pr_number=1,
        current_body=body(source_root="3" * 64),
        current_changed_paths=["implementation/new.py"],
        concurrent_prs=[],
        base_binding=binding(),
    )
    assert "STALE_OR_MISMATCHED_SOURCE_ROOT" in result["failures"]


def test_legacy_direct_overlap_blocks():
    result = evaluate_pr(
        current_pr_number=1,
        current_body=body(paths=["scripts"]),
        current_changed_paths=["scripts/check.py"],
        concurrent_prs=[{"number": 2, "body": None, "changed_paths": ["scripts/other.py"]}],
        base_binding=binding(),
    )
    assert result["disposition"] == "BLOCKED"
    assert any(x.startswith("UNKNOWN_CONCURRENT_INTENT_DIRECT_PATH_OVERLAP:") for x in result["failures"])


def test_legacy_different_path_warns_without_claiming_independence():
    result = evaluate_pr(
        current_pr_number=1,
        current_body=body(),
        current_changed_paths=["implementation/new.py"],
        concurrent_prs=[{"number": 2, "body": None, "changed_paths": ["docs/readme.md"]}],
        base_binding=binding(),
    )
    assert result["disposition"] == "PASS"
    assert result["warnings"] == ["PR#2:NO_DECLARED_INTENT_SEMANTIC_OVERLAP_UNKNOWN"]
