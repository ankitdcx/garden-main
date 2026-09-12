from __future__ import annotations
import json
from .model import (
    PROFILE, CoreObject, ClaimStatus, DependencyKind, ReceiptResult,
    TypedValue, Node, Claim, Dependency, Obligation, TestSpec, Receipt, Document
)

class GSLSeedError(ValueError):
    pass

TOP_KEYS = {"profile","nodes","claims","dependencies","obligations","tests","receipts"}

def _require_dict(x, where):
    if not isinstance(x, dict):
        raise GSLSeedError(f"{where} must be an object")
    return x

def _require_list(x, where):
    if not isinstance(x, list):
        raise GSLSeedError(f"{where} must be a list")
    return x

def _typed_value(x, where):
    d = _require_dict(x, where)
    allowed = {"type","value","unit"}
    unknown = set(d) - allowed
    if unknown:
        raise GSLSeedError(f"{where}: unsupported fields {sorted(unknown)}")
    if "type" not in d or "value" not in d:
        raise GSLSeedError(f"{where}: type and value are required")
    if not isinstance(d["type"], str) or not d["type"]:
        raise GSLSeedError(f"{where}.type must be a non-empty string")
    unit = d.get("unit")
    if unit is not None and (not isinstance(unit, str) or not unit):
        raise GSLSeedError(f"{where}.unit must be a non-empty string when present")
    return TypedValue(d["type"], d["value"], unit)

def parse_text(text: str) -> Document:
    try:
        raw = json.loads(text)
    except json.JSONDecodeError as e:
        raise GSLSeedError(f"malformed JSON: {e.msg}") from e
    return parse_obj(raw)

def parse_obj(raw) -> Document:
    d = _require_dict(raw, "document")
    unknown = set(d) - TOP_KEYS
    if unknown:
        raise GSLSeedError(f"document: unsupported top-level fields {sorted(unknown)}")
    if d.get("profile") != PROFILE:
        raise GSLSeedError(f"unsupported profile {d.get('profile')!r}; expected {PROFILE!r}")

    nodes = []
    for i, item in enumerate(_require_list(d.get("nodes", []), "nodes")):
        x = _require_dict(item, f"nodes[{i}]")
        if set(x) - {"id","kind","fields"}:
            raise GSLSeedError(f"nodes[{i}]: unsupported fields {sorted(set(x)-{'id','kind','fields'})}")
        try:
            kind = CoreObject(x["kind"])
        except (KeyError, ValueError) as e:
            raise GSLSeedError(f"nodes[{i}]: invalid core object kind") from e
        if not isinstance(x.get("id"), str) or not x["id"]:
            raise GSLSeedError(f"nodes[{i}].id must be a non-empty string")
        fields_raw = _require_dict(x.get("fields", {}), f"nodes[{i}].fields")
        fields = {k: _typed_value(v, f"nodes[{i}].fields.{k}") for k,v in fields_raw.items()}
        nodes.append(Node(x["id"], kind, fields))

    claims = []
    for i, item in enumerate(_require_list(d.get("claims", []), "claims")):
        x = _require_dict(item, f"claims[{i}]")
        required = {"id","proposition","status"}
        if not required.issubset(x):
            raise GSLSeedError(f"claims[{i}]: missing {sorted(required-set(x))}")
        if set(x) - {"id","proposition","status","context_ref","evidence_refs","scope"}:
            raise GSLSeedError(f"claims[{i}]: unsupported fields")
        try:
            status = ClaimStatus(x["status"])
        except ValueError as e:
            raise GSLSeedError(f"claims[{i}]: invalid claim status") from e
        if not isinstance(x["proposition"], str) or not x["proposition"]:
            raise GSLSeedError(f"claims[{i}].proposition must be non-empty")
        ev = x.get("evidence_refs", [])
        _require_list(ev, f"claims[{i}].evidence_refs")
        claims.append(Claim(x["id"], x["proposition"], status, x.get("context_ref"), tuple(ev), x.get("scope")))

    deps = []
    for i, item in enumerate(_require_list(d.get("dependencies", []), "dependencies")):
        x = _require_dict(item, f"dependencies[{i}]")
        try:
            kind = DependencyKind(x["kind"])
        except (KeyError, ValueError) as e:
            raise GSLSeedError(f"dependencies[{i}]: invalid dependency kind") from e
        deps.append(Dependency(x["source_ref"], x["target_ref"], kind, x.get("feedback_group")))

    obs = []
    for i, item in enumerate(_require_list(d.get("obligations", []), "obligations")):
        x = _require_dict(item, f"obligations[{i}]")
        obs.append(Obligation(x["id"], x["proposition"], x["owner"], x["status"], tuple(x.get("dependency_refs", []))))

    tests = []
    for i, item in enumerate(_require_list(d.get("tests", []), "tests")):
        x = _require_dict(item, f"tests[{i}]")
        tests.append(TestSpec(x["id"], x["obligation_ref"], x["description"], x["expected"]))

    receipts = []
    for i, item in enumerate(_require_list(d.get("receipts", []), "receipts")):
        x = _require_dict(item, f"receipts[{i}]")
        try:
            result = ReceiptResult(x["result"])
        except (KeyError, ValueError) as e:
            raise GSLSeedError(f"receipts[{i}]: invalid receipt result") from e
        receipts.append(Receipt(x["id"], x["subject_ref"], result, x["checker_ref"], tuple(x.get("evidence_refs", [])), x.get("scope")))

    doc = Document(PROFILE, tuple(nodes), tuple(claims), tuple(deps), tuple(obs), tuple(tests), tuple(receipts))
    validate_document(doc)
    return doc

def validate_document(doc: Document) -> None:
    ids = {}
    for collection in (doc.nodes, doc.claims, doc.obligations, doc.tests, doc.receipts):
        for item in collection:
            if item.id in ids:
                raise GSLSeedError(f"duplicate id {item.id}")
            ids[item.id] = item

    context_ids = {n.id for n in doc.nodes if n.kind is CoreObject.CONTEXT}
    for c in doc.claims:
        if c.context_ref is not None and c.context_ref not in context_ids:
            raise GSLSeedError(f"claim {c.id}: missing CONTEXT {c.context_ref}")
        for ev in c.evidence_refs:
            if ev not in ids:
                raise GSLSeedError(f"claim {c.id}: missing evidence ref {ev}")

    for dep in doc.dependencies:
        if dep.source_ref not in ids or dep.target_ref not in ids:
            raise GSLSeedError(f"dependency {dep.source_ref}->{dep.target_ref}: unresolved reference")
        if dep.kind is DependencyKind.BUILD and dep.feedback_group is not None:
            raise GSLSeedError("BUILD dependencies cannot declare a feedback group")
        if dep.source_ref == dep.target_ref and not (dep.kind is DependencyKind.RUNTIME and dep.feedback_group):
            raise GSLSeedError("self-dependency only allowed for explicit RUNTIME feedback")

    _validate_build_dag(doc.dependencies)
    _validate_feedback_cycles(doc.dependencies)

    obligation_ids = {o.id for o in doc.obligations}
    for t in doc.tests:
        if t.obligation_ref not in obligation_ids:
            raise GSLSeedError(f"test {t.id}: missing obligation {t.obligation_ref}")

    for r in doc.receipts:
        if r.subject_ref not in ids:
            raise GSLSeedError(f"receipt {r.id}: missing subject {r.subject_ref}")

def _validate_build_dag(deps):
    graph = {}
    for d in deps:
        if d.kind is DependencyKind.BUILD:
            graph.setdefault(d.source_ref, set()).add(d.target_ref)
            graph.setdefault(d.target_ref, set())
    visiting, done = set(), set()
    def dfs(n):
        if n in visiting:
            raise GSLSeedError("BUILD dependency cycle")
        if n in done:
            return
        visiting.add(n)
        for m in graph.get(n, ()):
            dfs(m)
        visiting.remove(n); done.add(n)
    for n in graph:
        dfs(n)

def _validate_feedback_cycles(deps):
    # LOGICAL cycles are rejected. SEMANTIC/RUNTIME cycles are allowed only
    # when every internal cycle edge declares the same non-empty feedback_group.
    nonbuild = [d for d in deps if d.kind is not DependencyKind.BUILD]

    logical = [d for d in nonbuild if d.kind is DependencyKind.LOGICAL]
    if logical:
        graph = {}
        for d in logical:
            graph.setdefault(d.source_ref, set()).add(d.target_ref)
            graph.setdefault(d.target_ref, set())
        visiting, done = set(), set()
        def dfs(n):
            if n in visiting:
                raise GSLSeedError("LOGICAL dependency cycle")
            if n in done:
                return
            visiting.add(n)
            for m in graph.get(n, ()):
                dfs(m)
            visiting.remove(n); done.add(n)
        for n in graph:
            dfs(n)

    feedback_edges = [d for d in nonbuild if d.kind in {DependencyKind.SEMANTIC, DependencyKind.RUNTIME}]
    graph = {}
    for d in feedback_edges:
        graph.setdefault(d.source_ref, set()).add(d.target_ref)
        graph.setdefault(d.target_ref, set())

    index = 0
    stack = []
    on_stack = set()
    indices = {}
    low = {}
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        low[v] = index
        index += 1
        stack.append(v); on_stack.add(v)
        for w in graph.get(v, ()):
            if w not in indices:
                strongconnect(w); low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = set()
            while True:
                w = stack.pop(); on_stack.remove(w); comp.add(w)
                if w == v:
                    break
            sccs.append(comp)

    for v in graph:
        if v not in indices:
            strongconnect(v)

    for comp in sccs:
        internal = [d for d in feedback_edges if d.source_ref in comp and d.target_ref in comp]
        is_cycle = len(comp) > 1 or any(d.source_ref == d.target_ref for d in internal)
        if not is_cycle:
            continue
        groups = {d.feedback_group for d in internal}
        if None in groups or "" in groups or len(groups) != 1:
            raise GSLSeedError("SEMANTIC/RUNTIME dependency cycle requires one shared non-empty feedback_group")
