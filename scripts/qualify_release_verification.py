#!/usr/bin/env python3
"""Execute bounded upstream TUF/in-toto release-verification qualification."""
from __future__ import annotations
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'implementation'), str(ROOT / 'implementation/tests')]
from garden_kernel.release_verification import verify_release
from supply_chain_fixture import fixture

OUT = ROOT / 'reviews/v15.7/qualification/release'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def public(values):
    return {key: value for key, value in values.items() if not key.startswith('_test_')}


def dependency_record(name):
    dist = importlib.metadata.distribution(name)
    metadata = dist.metadata
    license_files = []
    for entry in dist.files or []:
        normalized = str(entry).lower()
        if 'dist-info/licenses/' in normalized or normalized.endswith(('license', 'license.txt', 'copying', 'notice')):
            path = dist.locate_file(entry)
            if path.is_file():
                license_files.append({'path': str(entry), 'sha256': sha(path)})
    return {
        'name': name,
        'version': dist.version,
        'license_expression': metadata.get('License-Expression'),
        'license_metadata': metadata.get('License'),
        'home_page': metadata.get('Home-page'),
        'project_urls': metadata.get_all('Project-URL') or [],
        'license_and_notice_files': license_files,
        'provenance': 'Installed distribution metadata in the executing assurance virtual environment.'
    }


def run_case(case):
    with tempfile.TemporaryDirectory(prefix=f'garden-release-{case}-') as directory:
        values = fixture(directory, case=case)
        receipt = verify_release(**public(values))
        return receipt


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    expected = {
        'valid': 'VERIFIED',
        'expired': 'BLOCKED',
        'insufficient_signatures': 'BLOCKED',
        'unauthorized_builder': 'BLOCKED',
        'missing_step': 'BLOCKED',
        'substituted_content': 'BLOCKED',
        'cross_stage_mismatch': 'BLOCKED'
    }
    cases = {}
    for case, expected_status in expected.items():
        receipt = run_case(case)
        cases[case] = {'expected_status': expected_status, 'observed': receipt,
                       'result': 'PASS' if receipt['status'] == expected_status else 'FAIL'}

    with tempfile.TemporaryDirectory(prefix='garden-release-rotation-') as directory:
        values = fixture(directory, version=2, rotate_root=True)
        receipt = verify_release(**public(values))
        cached_root = Path(values['metadata_dir'], 'root.json').read_bytes()
        old_ids = [s.public_key.keyid for s in values['_test_trust_state']['keys']['targets']]
        rotation_ok = receipt['status'] == 'VERIFIED' and b'"version":2' in cached_root and all(x.encode() not in cached_root for x in old_ids)
        cases['signed_rotation_online_key_revocation'] = {
            'expected_status': 'VERIFIED_WITH_ROOT_V2_AND_OLD_TARGET_KEYS_REVOKED',
            'observed': receipt,
            'cached_root_sha256': hashlib.sha256(cached_root).hexdigest(),
            'old_target_keyids_absent': all(x.encode() not in cached_root for x in old_ids),
            'result': 'PASS' if rotation_ok else 'FAIL'
        }

    with tempfile.TemporaryDirectory(prefix='garden-release-rollback-') as directory:
        newer = fixture(directory, version=2)
        first = verify_release(**public(newer))
        older = fixture(directory, version=1, trust_state=newer['_test_trust_state'])
        second = verify_release(**public(older))
        rollback_ok = first['status'] == 'VERIFIED' and second['status'] == 'BLOCKED' and second['checks']['tuf']['status'] == 'INVALID'
        cases['persistent_cache_version_rollback'] = {
            'expected_status': 'NEWER_VERIFIED_THEN_OLDER_BLOCKED',
            'newer': first,
            'rollback_attempt': second,
            'result': 'PASS' if rollback_ok else 'FAIL'
        }

    requirement_names = [line.split('==', 1)[0].strip() for line in
                         (ROOT / 'requirements/assurance.txt').read_text().splitlines()
                         if line.strip() and not line.lstrip().startswith('#')]
    reuse = {
        'schema': 'GardenAssuranceDependencyReuseManifest/v1',
        'requirements_path': 'requirements/assurance.txt',
        'requirements_sha256': sha(ROOT / 'requirements/assurance.txt'),
        'dependencies': [dependency_record(name) for name in requirement_names],
        'claim_boundary': 'Version/license/notice provenance only; no patent clearance, ownership, or production qualification claim.'
    }
    (OUT / 'REUSE-MANIFEST.json').write_text(json.dumps(reuse, indent=2, sort_keys=True) + '\n')
    sources = ['implementation/garden_kernel/release_verification.py',
               'implementation/tests/supply_chain_fixture.py',
               'implementation/tests/test_release_verification.py',
               'scripts/qualify_release_verification.py', 'requirements/assurance.txt',
               'reviews/v15.7/qualification/release/FUNCTION-CONTRACTS.json',
               'reviews/v15.7/qualification/release/FUNCTION-CONTRACT-COVERAGE.json']
    receipt = {
        'schema': 'GardenReleaseVerificationQualificationReceipt/v1',
        'status': 'PASS' if all(row['result'] == 'PASS' for row in cases.values()) else 'FAIL',
        'scope': 'Bounded fixture qualification using real upstream TUF and in-toto libraries.',
        'source_files': [{'path': path, 'sha256': sha(ROOT / path)} for path in sources],
        'tool_versions': {name: importlib.metadata.version(name) for name in ('tuf','in-toto','securesystemslib')},
        'python': platform.python_version(),
        'cases': cases,
        'reuse_manifest_sha256': sha(OUT / 'REUSE-MANIFEST.json'),
        'production_qualification': False,
        'canonical_promotion_authorized': False,
        'limitations': [
            'Deterministic local fixtures do not establish production repository, HSM, network, clock, operator, build-worker, or deployment security.',
            'Private fixture keys exist only in process memory to construct signed test histories.',
            'The rotation case revokes old online role keys through a root transition authorized by both old and new root thresholds. It does not establish recovery from total root-key compromise; that requires an independently authenticated trust anchor or explicit out-of-band recovery, and no automatic trust reset is implemented.',
            'The receipt is test evidence, not canonical admission or production qualification.'
        ]
    }
    (OUT / 'release-verification-receipt.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status': receipt['status'], 'cases': len(cases),
                      'receipt': str((OUT / 'release-verification-receipt.json').relative_to(ROOT))}))
    return 0 if receipt['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
