"""Consume human admissions from the trusted base, never the proposed tree.

A Git-pinned admission is a recorded human instruction, not a human signature.
Repository branch protection and the operator admitting that base are the trust
boundary. An untrusted checkout alone cannot establish that boundary.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import re
from pathlib import Path
import subprocess
from typing import Any

from .core import SemanticError
from .evolution_trust import AttestationKind, make_attestation_receipt

ADMISSION_PATH = 'governance/human_admissions/PR-72.json'
SCHEMA = 'GardenBasePinnedHumanAdmission/v1'


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(['git', *args], cwd=root, capture_output=True, text=True)
    if result.returncode:
        raise SemanticError('cannot read admission Git evidence')
    return result.stdout


def change_bindings(root: Path, base: str, head: str) -> dict[str, dict[str, str | None]]:
    """Include deletions and disable rename folding; bind content and file mode."""
    raw = _git(root, 'diff', '--raw', '--no-abbrev', '--no-renames', '-z', base, head)
    parts = raw.split('\0')
    rows = {}
    for i in range(0, len(parts) - 1, 2):
        if not parts[i]:
            continue
        before_mode, after_mode, before, after, _status = parts[i].split()
        rows[parts[i + 1]] = {
            'before': None if set(before) == {'0'} else before,
            'after': None if set(after) == {'0'} else after,
            'before_mode': before_mode.lstrip(':'),
            'after_mode': after_mode,
        }
    return rows


def base_pinned_attestation(*, root: Path, base_ref: str, head_ref: str,
                            repository: str, request: dict[str, Any],
                            pull_request: int = 72,
                            design_epoch: str, source_root_sha256: str,
                            now: datetime | None = None):
    if not isinstance(pull_request, int) or isinstance(pull_request, bool) or pull_request <= 0:
        raise SemanticError('invalid pull request number')
    admission_path = f'governance/human_admissions/PR-{pull_request}.json'
    base = _git(root, 'rev-parse', '--verify', base_ref + '^{commit}').strip()
    head = _git(root, 'rev-parse', '--verify', head_ref + '^{commit}').strip()
    # Absence preserves the existing fail-closed behavior. Read ONLY base bytes.
    exists = subprocess.run(['git', 'cat-file', '-e', base + ':' + admission_path],
                            cwd=root, capture_output=True)
    if exists.returncode:
        return (), {}
    raw = _git(root, 'show', base + ':' + admission_path)
    try:
        record = json.loads(raw)
    except (ValueError, TypeError) as exc:
        raise SemanticError('malformed base human admission') from exc
    if not isinstance(record, dict):
        raise SemanticError('malformed base human admission object')
    if record.get('schema') != SCHEMA or record.get('decision') != 'HUMAN_ADMITTED':
        raise SemanticError('base admission is not admitted')
    if record.get('pull_request') != pull_request:
        raise SemanticError('base admission pull request mismatch')
    if not repository or record.get('repository') != repository:
        raise SemanticError('base admission repository mismatch')
    if record.get('design_epoch') != design_epoch or record.get('canonical_source_root_sha256') != source_root_sha256:
        raise SemanticError('base admission source identity mismatch')
    if record.get('kind') != 'HUMAN_SIGNOFF' or record.get('canonical_promotion') is not False:
        raise SemanticError('unsupported base admission scope')
    try:
        expires = datetime.fromisoformat(record['expires_at'].replace('Z', '+00:00'))
        if expires.tzinfo is None or (now or datetime.now(timezone.utc)) >= expires:
            raise SemanticError('base admission expired')
    except (KeyError, ValueError, TypeError) as exc:
        raise SemanticError('invalid admission expiry') from exc
    baseline = record.get('base_tree_without_admission')
    if not isinstance(baseline, str) or re.fullmatch(r'[0-9a-f]{64}', baseline) is None:
        raise SemanticError('missing baseline tree binding')
    tree = _git(root, 'ls-tree', '-r', '-z', base)
    bound = sorted(x for x in tree.split('\0') if x and x.split('\t', 1)[1] != admission_path)
    if hashlib.sha256('\0'.join(bound).encode()).hexdigest() != baseline:
        raise SemanticError('base admission baseline tree mismatch')
    if change_bindings(root, base, head) != record.get('changes'):
        raise SemanticError('base admission does not cover exact change set')
    if not isinstance(request, dict) or not isinstance(request.get('action'), dict):
        raise SemanticError('invalid admission action object')
    if not isinstance(record.get('action_request_sha256'), dict) or not isinstance(record.get('receipt_id'), str) or not record['receipt_id'].strip():
        raise SemanticError('invalid admission receipt or action bindings')
    action = request['action']
    if action.get('verb') not in {'PROPOSE', 'TRIAGE'}:
        raise SemanticError('base admission only covers candidate triage and proposals')
    request_hash = hashlib.sha256(json.dumps(request, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
    if record.get('action_request_sha256', {}).get(action.get('action_id')) != request_hash:
        raise SemanticError('base admission action mismatch')
    issuer = record.get('attestor_ref')
    if issuer != 'agent:codex:human-instruction-recorder' or not record.get('observed_human_instruction'):
        raise SemanticError('missing scoped human instruction provenance')
    blob = _git(root, 'rev-parse', base + ':' + admission_path).strip()
    receipt = make_attestation_receipt(
        receipt_id=record['receipt_id'] + ':' + action['action_id'],
        kind=AttestationKind.HUMAN_SIGNOFF, action_id=action['action_id'],
        design_epoch=design_epoch, source_root_sha256=source_root_sha256,
        issuer_ref=issuer,
        evidence_refs=[f'git:{repository}@{base}:{admission_path}#blob={blob}', f'git-change:{base}..{head}'],
    )
    return (receipt,), {issuer: frozenset({AttestationKind.HUMAN_SIGNOFF})}
