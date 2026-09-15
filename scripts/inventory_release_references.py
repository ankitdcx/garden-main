#!/usr/bin/env python3
"""Inventory v15.5 references without rewriting historical evidence bindings."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HISTORY = ('reviews/', 'design_deltas/', 'canonical/archive/', 'bootstrap/')

def main():
    rows = []
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    for name in paths:
        if not name or name.startswith('canonical/candidates/'):
            continue
        try:
            lines = (ROOT / name).read_text().splitlines()
        except (UnicodeError, OSError):
            continue
        for n,line in enumerate(lines,1):
            if not any(token in line for token in ('15.5', '63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598')):
                continue
            if name.startswith(HISTORY):
                category = 'PRESERVE_HISTORICAL_BINDING'
            elif name.startswith('canonical/current/'):
                category = 'ATOMIC_CURRENT_POINTER_SWAP_AFTER_PROMOTION_ONLY'
            elif '/tests/' in name:
                category = 'CLASSIFY_FIXTURE_VS_CURRENT_INTEGRATION_BEFORE_CHANGE'
            elif name.startswith('governance/') or name.endswith('.json'):
                category = 'REVALIDATE_VERSION_BOUND_RECORD_DO_NOT_STRING_REPLACE'
            else:
                category = 'ACTIVE_REFERENCE_REVIEW_AT_PROMOTION'
            rows.append(dict(path=name,line=n,category=category,excerpt=line[:240]))
    out = dict(schema='GardenReleaseReferenceMigrationInventory/v1',
        scope='All tracked UTF-8 files at the local review snapshot; no Git history rewrite',
        status='PREPARED_NOT_APPLIED_PROMOTION_BLOCKED', references=rows,
        rules=['Preserve old hashes, receipts, provenance, fixtures and immutable CycleBindings.',
               'Only after admission replace active current source paths and regenerate dependent current records.',
               'Public garden-swarm requires its own snapshot and authorized public projection; no private source transfer.'])
    path = ROOT / 'reviews/v15.6/REFERENCE-MIGRATION-INVENTORY.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(f'{len(rows)} references inventoried; none blindly rewritten')

if __name__ == '__main__':
    main()
