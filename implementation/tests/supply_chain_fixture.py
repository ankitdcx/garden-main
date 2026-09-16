from datetime import datetime,timezone,timedelta
from pathlib import Path
import hashlib,json,sys
from tuf.api.metadata import Root,Targets,Snapshot,Timestamp,Metadata,TargetFile,MetaFile
from tuf.ngclient.fetcher import FetcherInterface
from tuf.api.exceptions import DownloadHTTPError
from securesystemslib.signer import CryptoSigner
from in_toto.models.layout import Layout,Step
from in_toto.models.metadata import Metablock
from in_toto.models.link import Link

class MemoryFetcher(FetcherInterface):
    def __init__(self,files):self.files=files
    def _fetch(self,url):
        name=url.rsplit('/',1)[-1]
        if name not in self.files:raise DownloadHTTPError('absent fixture',404)
        yield self.files[name]

def fixture(rootdir,case='valid',version=1,trust_state=None,rotate_root=False):
    rootdir=Path(rootdir);rootdir.mkdir(parents=True,exist_ok=True)
    expiration=datetime.now(timezone.utc)+timedelta(days=2)
    if trust_state is None:
        trust_state={'keys':{r:[CryptoSigner.generate_ed25519(),CryptoSigner.generate_ed25519()] for r in ('root','targets','snapshot','timestamp')}}
    keys=trust_state['keys']
    root=Metadata(Root(version=1,expires=expiration,consistent_snapshot=False))
    for role,signers in keys.items():
        root.signed.roles[role].threshold=2
        for signer in signers:root.signed.add_key(signer.public_key,role)
    for signer in keys['root']:root.sign(signer,append=True)
    bootstrap_root=root.to_bytes()
    remote_root=None
    active_keys=keys
    if rotate_root:
        active_keys={r:[CryptoSigner.generate_ed25519(),CryptoSigner.generate_ed25519()] for r in ('root','targets','snapshot','timestamp')}
        rotated=Metadata(Root(version=2,expires=expiration,consistent_snapshot=False))
        for role,signers in active_keys.items():
            rotated.signed.roles[role].threshold=2
            for signer in signers:rotated.signed.add_key(signer.public_key,role)
        # TUF root rotation requires the new root to satisfy both old and new root thresholds.
        for signer in keys['root']:rotated.sign(signer,append=True)
        for signer in active_keys['root']:rotated.sign(signer,append=True)
        remote_root=rotated.to_bytes()
        trust_state['rotated_keys']=active_keys
        trust_state['rotated_root_sha256']=hashlib.sha256(remote_root).hexdigest()
    artifact=b'Garden reference build\n';source=b'exact source revision\n'
    targets=Metadata(Targets(version=version,expires=expiration,targets={'artifact.bin':TargetFile.from_data('artifact.bin',artifact)}))
    if case=='expired':targets.signed.expires=datetime.now(timezone.utc)-timedelta(days=1)
    for signer in active_keys['targets'][:1 if case=='insufficient_signatures' else 2]:targets.sign(signer,append=True)
    targets_raw=targets.to_bytes()
    snapshot=Metadata(Snapshot(version=version,expires=expiration,meta={'targets.json':MetaFile.from_data(version,targets_raw,['sha256'])}))
    for signer in active_keys['snapshot']:snapshot.sign(signer,append=True)
    snapshot_raw=snapshot.to_bytes()
    timestamp=Metadata(Timestamp(version=version,expires=expiration,snapshot_meta=MetaFile.from_data(version,snapshot_raw,['sha256'])))
    for signer in active_keys['timestamp']:timestamp.sign(signer,append=True)
    files={'targets.json':targets_raw,'snapshot.json':snapshot_raw,'timestamp.json':timestamp.to_bytes()}
    if remote_root is not None:files['2.root.json']=remote_root
    owner=CryptoSigner.generate_ed25519();builder=CryptoSigner.generate_ed25519()
    builderkey={'keyid':builder.public_key.keyid,**builder.public_key.to_dict()}
    ownerkey={'keyid':owner.public_key.keyid,**owner.public_key.to_dict()}
    step=Step(name='build',pubkeys=[builder.public_key.keyid],threshold=1,
        expected_materials=[['ALLOW','source.txt'],['DISALLOW','*']],
        expected_products=[['CREATE','artifact.bin'],['DISALLOW','*']],expected_command=['garden-fixture-build','source.txt'])
    layout=Metablock(signed=Layout(steps=[step],keys={builder.public_key.keyid:builderkey},expires=expiration.strftime('%Y-%m-%dT%H:%M:%SZ')))
    layout.create_signature(owner);layoutpath=rootdir/'root.layout';layout.dump(str(layoutpath))
    materials={'source.txt':{'sha256':hashlib.sha256(source).hexdigest()}}
    product=artifact if case!='cross_stage_mismatch' else b'other separately signed build'
    link=Metablock(signed=Link(name='build',materials=materials,products={'artifact.bin':{'sha256':hashlib.sha256(product).hexdigest()}},command=step.expected_command))
    link.create_signature(CryptoSigner.generate_ed25519() if case=='unauthorized_builder' else builder)
    if case!='missing_step':link.dump(str(rootdir/f'build.{builder.public_key.keyid[:8]}.link'))
    result=dict(metadata_dir=rootdir/'cache',metadata_url='https://fixture.invalid/',fetcher=MemoryFetcher(files),trusted_root=bootstrap_root,trusted_root_sha256=hashlib.sha256(bootstrap_root).hexdigest(),artifact_name='artifact.bin',artifact_bytes=b'substituted' if case=='substituted_content' else artifact,layout_path=layoutpath,layout_sha256=hashlib.sha256(layoutpath.read_bytes()).hexdigest(),layout_keys={owner.public_key.keyid:ownerkey},link_dir=rootdir,expected_materials=materials,expected_command=step.expected_command)
    # Test-only, in-memory signing capability for constructing same trust-root versions.
    result['_test_trust_state']=trust_state
    return result
