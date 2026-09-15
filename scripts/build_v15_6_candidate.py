#!/usr/bin/env python3
"""Build a reviewable v15.6 candidate; never promote or rewrite current canon."""
from __future__ import annotations
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'implementation'))
from garden_kernel.section_units import build_inventory
from check_successor_drift import normalized_diff

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def main():
    current = ROOT / 'canonical/current'
    archive = ROOT / 'canonical/archive/v15.5'
    target = ROOT / 'canonical/candidates/v15.6'
    evidence = ROOT / 'reviews/v15.6'
    delta = ROOT / 'design_deltas/v15.6'
    old_manifest = json.loads((current / 'SOURCE_MANIFEST.json').read_text())
    assert old_manifest['release'] == 'Garden v15.5'
    engineering = (delta / 'ENGINEERING-HARDENING-SPECIFICATION.txt').read_text()
    pending = (delta / 'PENDING-CONSOLIDATED-SPECIFICATION.txt').read_text()
    pending_sections = {role: '' for role in ('User', 'System', 'Technical', 'Annexure', 'Theories')}
    headings = list(re.finditer(r'^(USER|SYSTEM|TECHNICAL|ANNEXURE|THEORIES) — ', pending, re.M))
    assert headings, 'Missing owner-grouped pending specification'
    pending_preamble = pending[:headings[0].start()]
    for i, heading in enumerate(headings):
        end = headings[i+1].start() if i+1 < len(headings) else len(pending)
        pending_sections[heading.group(1).title()] += pending[heading.start():end]
    reconciliation = json.loads((delta / 'PENDING-RECONCILIATION-2026-09-15.json').read_text())
    new_delta = json.loads((delta / 'DELTASET-2026-09-15-ENGINEERING-HARDENING.json').read_text())
    target.mkdir(parents=True, exist_ok=True)
    archive.mkdir(parents=True, exist_ok=True)
    evidence.mkdir(parents=True, exist_ok=True)
    for source in current.iterdir():
        if source.is_file():
            archived = archive / source.name
            if archived.exists():
                assert archived.read_bytes() == source.read_bytes(), 'Archive collision'
            else:
                shutil.copyfile(source, archived)

    human = '''[H-V15-6] Candidate human guide
Owner: existing HumanCore, authority, safety, knowledge and evolution owners.
This candidate strengthens existing controls rather than adding top-level engines.
The engineering package covers safety mediation, read/write separation, reserved
resources, consequential contracts, delegated autonomy, private knowledge,
version resolution, compensation, provenance, diverse verification, adapters,
dependency failures, reusable schemas, cumulative containment and maturity.
The additional 38 work items cover permission/revocation/recovery modeling,
release verification, a physical fallback example and supporting trust analysis.
Temporal and seL4 adoption remain deferred. Specification is not implementation.
Older pending work includes GSL gaps, KR assimilation, historical recovery,
GAIA naming, constitutional events and process hardening. Exact dispositions
and missing-definition items appear in [A-V15-6]; complete clauses in [T-V15-6].
Eligibility never grants authority. Agreement never establishes truth by itself.
Physical effects of uncertain completion must be reconciled before retrying.
Current deployment or promotion permission is not created by this document.
'''
    system = '''[S-V15-6] Candidate system integration
Owner: existing Transition Fabric, AAP, ActionGate and capability owners.
Observe and type the request; bind the current authority, policy and DesignEpoch;
compare with DO_NOTHING; reserve shared cumulative effect/resource capacity;
check preconditions and fresh authorization; fence stale workers; mediate the
physical path; execute across a declared commitment point; record actual or
uncertain effect; check postconditions; reconcile, contain or compensate when
required. Repeated delivery cannot manufacture a fresh effect identity.
Independent verification assesses common failure modes and a bounded response
deadline. A safe-stop path retains its own authority and envelope. During
partitions, exclusive allocation and fresh revocation checks cannot be replaced
with optimistic merging. A model-checking completion is bounded by the model,
properties and assumptions recorded in its receipt.
Release verification binds TUF checks AND in-toto policy checks AND the same
artifact identity. No incomplete stage can authorize promotion.
ProcessVersion and DesignEpoch bindings stay immutable through a cycle.
Full owner-qualified candidate clauses: [T-V15-6]. Dispositions: [A-V15-6].
'''
    theories = '''[TH-V15-6] Engineering-pattern qualification
Owner: existing engineering-design, theory, proof and provenance owners.
These are established engineering patterns applied as bounded candidate profiles.
They are not evidence of comparison against 100 ranked designs or patent clearance.
CQRS and event sourcing are separate decisions. Minimal version selection is not
a universal solution for revoked proofs, exclusions or incompatible schemas.
Compensation is not guaranteed rollback; simulation is not physical validation;
different model families do not establish failure independence by themselves.
The permission model must disclose state bounds, fairness and commitment semantics.
The physical example must derive switching timing from explicit dynamics and
uncertainty, distinguish safe from recoverable regions, and record loss of
assurance outside those regions. Neither specification is claimed executed here.
TUF/in-toto, STPA, TLA+, local-first and PROV-O reuse must retain exact provenance
and applicable license records. Temporal and seL4 remain decisions after evidence.
No new top-level theory engine or authority source is introduced. [T-V15-6]
contains the full engineering requirements; [A-V15-6] records pending work.
'''
    texts = {
        'User': human,
        'System': system,
        'Technical': '[T-V15-6] Consolidated candidate technical contracts\n'
            + 'Owner: existing owner-qualified contracts named below.\n\n'
            + engineering,
        'Annexure': '[A-V15-6] Candidate disposition and registration boundary\n'
            + 'This is a candidate ledger, not an admission or certification receipt.\n'
            + 'Existing SchemaIDs retain their owners. Patch-local names are not automatically canonical SchemaIDs.\n'
            + json.dumps(reconciliation, indent=2, ensure_ascii=False)
            + '\n\nENGINEERING DELTA MACHINE-READABLE SPECIFICATION\n'
            + json.dumps(new_delta, indent=2, ensure_ascii=False) + '\n',
        'Theories': theories,
    }
    for role in texts:
        texts[role] += '\n\n' + pending_preamble + pending_sections[role]
    rows, retention, diff_rows = {}, [], []
    for role, old in old_manifest['files'].items():
        raw = (current / old['name']).read_bytes()
        assert len(raw) == old['bytes'] and digest(raw) == old['sha256']
        name = f'Garden_{role}_v15.6_FULL_CANDIDATE_2026-09-15.txt'
        header = (f'GARDEN v15.6 — FULL FIVE-FILE WORKING CANDIDATE — {role.upper()} — 2026-09-15\n'
            'Status: WORKING_FIVE_FILE_CANDIDATE / NOT CANONICAL / NOT CERTIFIED\n'
            'Predecessor: Garden v15.5; GSL v45.1; top-level topology unchanged.\n'
            'The complete predecessor bytes below are retained as a versioned source layer.\n'
            'Embedded prior release banners describe their historical source layer only.\n'
            'The appended v15.6 clauses are proposed refinements under the named existing owners.\n'
            'Explicit supersessions/dispositions govern this candidate; unresolved conflicts block promotion.\n'
            'Model, runtime, empirical and deployment work remains pending unless an exact receipt says otherwise.\n'
            'BEGIN IMMUTABLE V15.5 SOURCE LAYER\n').encode()
        suffix = ('\nEND IMMUTABLE V15.5 SOURCE LAYER\n\nBEGIN V15.6 CANDIDATE EXTENSION\n'
            + texts[role] + '\nEND V15.6 CANDIDATE EXTENSION\n').encode()
        output = header + raw + suffix
        (target / name).write_bytes(output)
        rows[role] = dict(name=name, bytes=len(output), sha256=digest(output))
        retention.append(dict(role=role, archive='canonical/archive/v15.5/'+old['name'],
            candidate='canonical/candidates/v15.6/'+name, predecessor_sha256=old['sha256'],
            retained_offset=len(header), retained_bytes=len(raw), exact_bytes_retained=output[len(header):len(header)+len(raw)] == raw))
        diff = normalized_diff(archive / old['name'], target / name)
        diff_rows.append(dict(predecessor='canonical/archive/v15.5/'+old['name'],
            candidate='canonical/candidates/v15.6/'+name, expected_diff_sha256=digest(diff.encode()),
            delta_ids=['V15.6-WORKING-CANDIDATE-NOT-ADMITTED']))
    roots = sorted([dict(role=role, **row) for role,row in rows.items()], key=lambda x:x['role'])
    root_hash = digest(json.dumps(roots, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode())
    manifest = dict(schema='GardenCanonicalSourceManifest/v1', release='Garden v15.6', gsl='v45.1',
        date='2026-09-15', status='WORKING_FIVE_FILE_CANDIDATE_NOT_CANONICAL', files=rows,
        source_root_algorithm=old_manifest['source_root_algorithm'], source_root_sha256=root_hash,
        predecessor_source_root_sha256=old_manifest['source_root_sha256'])
    write_json(target / 'SOURCE_MANIFEST.json', manifest)
    write_json(evidence / 'RETENTION-RECEIPT.json', dict(status='PASS', scope='Byte retention only; no semantic admission', files=retention))
    write_json(evidence / 'EXPECTED-CANDIDATE-DIFF.json', dict(schema='GardenSuccessorDeltaManifest/v1',
        predecessor_release='Garden v15.5', candidate_release='Garden v15.6 working candidate',
        admission_status='NOT_ADMITTED', files=diff_rows))
    old_inventory = build_inventory(source_dir=current, manifest=old_manifest, process_version='1.4')
    inventory = build_inventory(source_dir=target, manifest=manifest, process_version='1.4')
    old_unresolved = set(r for u in old_inventory.units for r in u.unresolved_references)
    unresolved = sorted(set(r for u in inventory.units for r in u.unresolved_references))
    inventory_payload = inventory.to_dict()
    inventory_payload['coverage_scope'] = 'Contiguous section-boundary segmentation only; not semantic closure or qualified review'
    inventory_payload['section_boundary_coverage_complete'] = inventory.coverage_complete
    inventory_payload['semantic_reference_closure_complete'] = False
    write_json(evidence / 'SECTION-INVENTORY.json', inventory_payload)
    write_json(evidence / 'REFERENCE-CLOSURE-RECEIPT.json', dict(status='INCONCLUSIVE',
        source_root_sha256=root_hash, scanner='garden_kernel.section_units.build_inventory',
        scanner_sha256=digest((ROOT/'implementation/garden_kernel/section_units.py').read_bytes()),
        scope='Explicit H/S/T/TH/RA/A anchor occurrences only; not all GSL syntax, semantic identifiers or proof obligations',
        unresolved=unresolved, newly_unresolved=sorted(set(unresolved)-old_unresolved),
        inherited_unresolved=sorted(old_unresolved), inventory_counts=inventory.counts(),
        complete_semantic_reference_closure=False, qualified_review_units=0))
    print(json.dumps(dict(candidate_source_root_sha256=root_hash, files=len(rows),
        exact_retention=all(r['exact_bytes_retained'] for r in retention),
        unresolved=len(unresolved), newly_unresolved=len(set(unresolved)-old_unresolved))))

if __name__ == '__main__':
    main()
