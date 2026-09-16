"""Conjunctive release verification using upstream TUF and in-toto libraries.

Caller owns pinned trust roots, policy and persistent TUF cache. A valid receipt
is release evidence only; promotion still needs the existing admission owner.
"""
from __future__ import annotations
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import tempfile


def _snapshot_in_toto_inputs(layout_path, link_dir):
    """Copy policy inputs once so verification and profile checks see identical bytes."""
    layout_path = Path(layout_path)
    link_dir = Path(link_dir)
    try:
        layout_bytes = layout_path.read_bytes()
        links = {}
        for path in sorted(link_dir.glob('*.link')):
            if not path.is_file():
                continue
            links[path.name] = path.read_bytes()
    except OSError as exc:
        raise FileNotFoundError(f'in-toto input snapshot failed: {exc}') from exc
    return layout_bytes, links


def verify_release(*, metadata_dir, metadata_url, fetcher, trusted_root,
                   trusted_root_sha256, artifact_name, artifact_bytes,
                   layout_path, layout_sha256, layout_keys, link_dir,
                   expected_materials, expected_command):
    from tuf.ngclient.updater import Updater
    from in_toto.models.metadata import Metadata
    from in_toto.verifylib import in_toto_verify
    checks = {}; identities = {}
    artifact_hash = hashlib.sha256(artifact_bytes).hexdigest()
    root_hash = hashlib.sha256(trusted_root).hexdigest()
    observed_layout_hash = None
    try:
        if root_hash != trusted_root_sha256:
            raise ValueError('trusted-root identity mismatch')
        # Cache is per trusted repository and MUST survive invocations for rollback checks.
        updater = Updater(str(metadata_dir), metadata_url, fetcher=fetcher, bootstrap=trusted_root)
        updater.refresh()
        active_root_bytes = (Path(metadata_dir) / 'root.json').read_bytes()
        from tuf.api.metadata import Metadata as TUFMetadata
        active_root = TUFMetadata.from_bytes(active_root_bytes).signed
        identities['active_trusted_root_sha256'] = hashlib.sha256(active_root_bytes).hexdigest()
        identities['active_trusted_root_version'] = active_root.version
        target = updater.get_targetinfo(artifact_name)
        if target is None:
            raise ValueError('artifact absent from verified targets')
        target.verify_length_and_hashes(artifact_bytes)
        identities['tuf_artifact_sha256'] = target.hashes.get('sha256')
        checks['tuf'] = {'status': 'VALID'}
    except Exception as exc:
        checks['tuf'] = {'status': 'INCOMPLETE' if isinstance(exc, TimeoutError) else 'INVALID', 'reason': type(exc).__name__+': '+str(exc)}
    try:
        layout_bytes, link_bytes = _snapshot_in_toto_inputs(layout_path, link_dir)
        observed_layout_hash = hashlib.sha256(layout_bytes).hexdigest()
        if observed_layout_hash != layout_sha256:
            raise ValueError('layout policy identity mismatch')
        with tempfile.TemporaryDirectory(prefix='garden-intoto-snapshot-') as snapshot_dir_name:
            snapshot_dir = Path(snapshot_dir_name)
            snapshot_layout = snapshot_dir / 'root.layout'
            snapshot_layout.write_bytes(layout_bytes)
            for name, raw in link_bytes.items():
                (snapshot_dir / name).write_bytes(raw)
            layout = Metadata.load(str(snapshot_layout))
            if layout.signed.inspect:
                raise ValueError('this profile prohibits executing layout inspection commands')
            summary = in_toto_verify(layout, layout_keys, link_dir_path=str(snapshot_dir), persist_inspection_links=False)
            # in-toto command comparison can be advisory: enforce this profile's exact command policy.
            build = next(s for s in layout.signed.steps if s.name == 'build')
            if build.expected_command != expected_command:
                raise ValueError('layout command policy mismatch')
            matching = []
            for keyid in build.pubkeys:
                name = f'build.{keyid[:8]}.link'
                if name in link_bytes:
                    link = Metadata.load(str(snapshot_dir / name)).signed
                    if link.command != expected_command or link.materials != expected_materials:
                        raise ValueError('build command or source material identity mismatch')
                    matching.append(link)
            if len(matching) < build.threshold:
                raise FileNotFoundError('missing qualified build link')
            identities['in_toto_artifact_sha256'] = summary.products[artifact_name]['sha256']
        checks['in_toto'] = {'status': 'VALID'}
    except Exception as exc:
        checks['in_toto'] = {'status': 'INCOMPLETE' if isinstance(exc, TimeoutError) else 'INVALID', 'reason': type(exc).__name__+': '+str(exc)}
    identities['observed_artifact_sha256'] = artifact_hash
    checks['artifact_identity'] = {'status': 'VALID' if identities.get('tuf_artifact_sha256') == identities.get('in_toto_artifact_sha256') == artifact_hash else 'INVALID'}
    return {'schema':'GardenReleaseVerificationReceipt/v1',
            'status':'VERIFIED' if all(x['status']=='VALID' for x in checks.values()) else 'BLOCKED',
            'checks':checks,'identities':identities,'bootstrap_trusted_root_sha256':root_hash,
            'active_trusted_root_sha256':identities.get('active_trusted_root_sha256'),
            'active_trusted_root_version':identities.get('active_trusted_root_version'),
            'layout_policy_sha256':observed_layout_hash,
            'layout_verification_keys_sha256':hashlib.sha256(json.dumps(layout_keys,sort_keys=True).encode()).hexdigest(),
            'source_policy_sha256':hashlib.sha256(json.dumps(expected_materials,sort_keys=True).encode()).hexdigest(),
            'tool_versions':{p:importlib.metadata.version(p) for p in ('tuf','in-toto','securesystemslib')},
            'python':platform.python_version(),'promotion_authorized':False}
