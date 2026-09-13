from implementation.garden_kernel.integration_provenance import (
    AgentWorkIntent,
    assess_intents,
    compare_intents,
    validate_current_binding,
)

BASE = "1" * 40
ROOT = "2" * 64
EPOCH = f"Garden-v15.5@{ROOT}"


def intent(intent_id="a", **overrides):
    data = {
        "schema": "AgentWorkIntent/v1",
        "intent_id": intent_id,
        "agent_id": "agent:a",
        "work_package_id": "WP-X",
        "base_sha": BASE,
        "source_root_sha256": ROOT,
        "design_epoch_ref": EPOCH,
        "target_paths": ["implementation/a.py"],
        "target_symbols": ["Thing"],
        "semantic_domains": ["authority-resolution"],
        "affected_invariants": ["INV-1"],
        "affected_contracts": ["FC-1"],
        "intended_effect": "bounded change",
        "parallel_mode": "INDEPENDENT_COMPARISON",
    }
    data.update(overrides)
    return AgentWorkIntent.from_mapping(data)


def test_different_files_same_semantic_domain_collide():
    a = intent("a", target_paths=["implementation/a.py"], target_symbols=[])
    b = intent("b", target_paths=["implementation/b.py"], target_symbols=[], affected_invariants=[], affected_contracts=[])
    result = compare_intents(a, b)
    assert result["classification"] == "POTENTIAL_COLLISION"
    assert "SEMANTIC_DOMAIN_OVERLAP" in result["reasons"]


def test_parent_directory_overlap_collides():
    a = intent("a", target_paths=["implementation"])
    b = intent("b", target_paths=["implementation/garden_kernel/core.py"], semantic_domains=["other"], target_symbols=[], affected_invariants=[], affected_contracts=[])
    assert "PATH_OVERLAP" in compare_intents(a, b)["reasons"]


def test_shared_contract_collides_without_path_overlap():
    a = intent("a", target_paths=["a.py"], semantic_domains=["one"], target_symbols=[], affected_invariants=[])
    b = intent("b", target_paths=["b.py"], semantic_domains=["two"], target_symbols=[], affected_invariants=[])
    assert "CONTRACT_OVERLAP" in compare_intents(a, b)["reasons"]


def test_no_overlap_passes_without_receipt():
    a = intent("a", target_paths=["a.py"], semantic_domains=["one"], target_symbols=[], affected_invariants=[], affected_contracts=[])
    b = intent("b", target_paths=["b.py"], semantic_domains=["two"], target_symbols=[], affected_invariants=[], affected_contracts=[])
    assert assess_intents(a, [b])["disposition"] == "PASS"


def test_collision_requires_receipt():
    a = intent("a")
    b = intent("b")
    assert assess_intents(a, [b])["disposition"] == "REQUIRES_INTEGRATION_RECEIPT"


def test_compatible_receipt_requires_post_integration_tests():
    a = intent("a")
    b = intent("b")
    receipt = {
        "schema": "IntegrationReceipt/v1",
        "current_intent_id": "a",
        "work_package_id": "WP-X",
        "base_sha": BASE,
        "source_root_sha256": ROOT,
        "design_epoch_ref": EPOCH,
        "concurrent_intent_ids": ["b"],
        "semantic_compare": "COMPATIBLE",
        "composition_evidence": ["manual semantic diff"],
    }
    assert assess_intents(a, [b], receipt)["disposition"] == "BLOCKED"


def test_complete_receipt_passes():
    a = intent("a")
    b = intent("b")
    receipt = {
        "schema": "IntegrationReceipt/v1",
        "current_intent_id": "a",
        "work_package_id": "WP-X",
        "base_sha": BASE,
        "source_root_sha256": ROOT,
        "design_epoch_ref": EPOCH,
        "concurrent_intent_ids": ["b"],
        "semantic_compare": "COMPATIBLE",
        "composition_evidence": ["semantic delta composition checked"],
        "tests_after_integration": ["pytest -q"],
    }
    assert assess_intents(a, [b], receipt)["disposition"] == "PASS"


def test_receipt_omitting_colliding_intent_blocks():
    a = intent("a")
    b = intent("b")
    receipt = {
        "schema": "IntegrationReceipt/v1",
        "current_intent_id": "a",
        "work_package_id": "WP-X",
        "base_sha": BASE,
        "source_root_sha256": ROOT,
        "design_epoch_ref": EPOCH,
        "concurrent_intent_ids": [],
        "semantic_compare": "COMPATIBLE",
        "composition_evidence": ["x"],
        "tests_after_integration": ["y"],
    }
    assert assess_intents(a, [b], receipt)["disposition"] == "BLOCKED"


def test_binding_rejects_stale_source_root():
    a = intent("a")
    errors = validate_current_binding(a, base_sha=BASE, source_root_sha256="3" * 64, design_epoch_ref=EPOCH)
    assert "STALE_OR_MISMATCHED_SOURCE_ROOT" in errors


def test_binding_rejects_stale_base_sha():
    a = intent("a")
    errors = validate_current_binding(a, base_sha="4" * 40, source_root_sha256=ROOT, design_epoch_ref=EPOCH)
    assert "STALE_OR_MISMATCHED_BASE_SHA" in errors
