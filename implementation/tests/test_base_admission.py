"""Trust-boundary and replay tests using real Git trees."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone

from garden_kernel.base_admission import ADMISSION_PATH, base_pinned_attestation, change_bindings
from garden_kernel.core import SemanticError

NOW = datetime(2026, 9, 15, tzinfo=timezone.utc)


class BaseAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        (self.root/'target').write_text('before')
        self.base = self.commit()
        (self.root/'target').write_text('after')
        self.head = self.commit()
        self.request = {'action': {'action_id': 'A', 'verb': 'PROPOSE'}}
        self.record = {
            'schema': 'GardenBasePinnedHumanAdmission/v1', 'receipt_id': 'H1',
            'decision': 'HUMAN_ADMITTED', 'repository': 'owner/repo', 'pull_request': 72,
            'design_epoch': 'v15.5', 'canonical_source_root_sha256': 'root',
            'kind': 'HUMAN_SIGNOFF', 'canonical_promotion': False,
            'expires_at': '2026-09-22T00:00:00Z',
            'change_path_encoding': 'SHA256_UTF8',
            'changes': {hashlib.sha256(p.encode()).hexdigest(): v for p,v in change_bindings(self.root, self.base, self.head).items()},
            'attestor_ref': 'agent:codex:human-instruction-recorder',
            'observed_human_instruction': 'Explicit scoped human instruction recorded by agent; not a human signature.',
            'action_request_sha256': {'A': self.request_hash()},
        }

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL, text=True).strip()

    def commit(self):
        self.git('add', '-A'); self.git('commit', '-qm', 'test')
        return self.git('rev-parse', 'HEAD')

    def request_hash(self):
        return hashlib.sha256(json.dumps(self.request, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

    def admit(self):
        self.git('checkout', '-q', self.base)
        raw=subprocess.check_output(['git','ls-tree','-r','-z',self.base],cwd=self.root,text=True)
        bound=sorted(x for x in raw.split('\0') if x and x.split('\t',1)[1]!=ADMISSION_PATH)
        self.record['base_tree_without_admission']=hashlib.sha256('\0'.join(bound).encode()).hexdigest()
        p=self.root/ADMISSION_PATH;p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.record));self.base=self.commit()
        (self.root/'target').write_text('after');self.head=self.commit()

    def verify(self, **kwargs):
        return base_pinned_attestation(root=self.root, base_ref=self.base, head_ref=self.head,
            repository=kwargs.get('repository', 'owner/repo'), request=self.request,
            design_epoch='v15.5', source_root_sha256='root', now=NOW)

    def test_base_pinned_approval_is_narrow_human_signoff(self):
        self.admit();receipts,attestors=self.verify()
        self.assertEqual(len(receipts),1)
        self.assertEqual(receipts[0]['kind'],'HUMAN_SIGNOFF')
        self.assertEqual([k.value for k in next(iter(attestors.values()))],['HUMAN_SIGNOFF'])

    def test_candidate_cannot_introduce_its_own_approval(self):
        p=self.root/ADMISSION_PATH;p.parent.mkdir(parents=True);p.write_text(json.dumps(self.record))
        self.head=self.commit();self.assertEqual(self.verify(),((),{}))

    def test_candidate_cannot_replace_base_approval(self):
        self.admit();p=self.root/ADMISSION_PATH
        forged=dict(self.record);forged['decision']='HUMAN_ADMITTED';p.write_text(json.dumps(forged)+' ')
        self.head=self.commit()
        with self.assertRaisesRegex(SemanticError,'exact change set'): self.verify()

    def test_extra_change_deletion_or_mode_change_cannot_replay(self):
        self.admit(); approved_head=self.head
        for change in ('extra','delete','mode'):
            with self.subTest(change=change):
                self.git('checkout','-q',approved_head)
                if change=='extra': (self.root/'extra').write_text('unauthorized')
                elif change=='delete': (self.root/'target').unlink()
                else: (self.root/'target').chmod(0o755)
                self.head=self.commit()
                with self.assertRaisesRegex(SemanticError,'exact change set'): self.verify()

    def test_wrong_repository_rejected(self):
        self.admit()
        with self.assertRaisesRegex(SemanticError,'repository'):self.verify(repository='attacker/repo')

    def test_expiry_and_stale_source_rejected(self):
        for field,value in [('expires_at','2026-09-14T00:00:00Z'),('design_epoch','v15.4')]:
            with self.subTest(field=field):
                old=self.record[field];self.record[field]=value;self.admit()
                with self.assertRaises(SemanticError):self.verify()
                self.record[field]=old

    def test_different_action_or_verb_rejected(self):
        self.admit();self.request['action']['action_id']='B'
        with self.assertRaisesRegex(SemanticError,'action mismatch'):self.verify()
        self.request['action']['verb']='MATERIALIZE'
        with self.assertRaisesRegex(SemanticError,'only covers'):self.verify()

    def test_malformed_request_keeps_typed_failure(self):
        self.admit();self.request={'action': []}
        with self.assertRaisesRegex(SemanticError,'action object'):self.verify()

    def test_wrong_pull_request_rejected(self):
        self.record['pull_request']=73;self.admit()
        with self.assertRaisesRegex(SemanticError,'pull request'):self.verify()

    def test_missing_or_changed_baseline_binding_is_rejected(self):
        self.admit()
        p=self.root/ADMISSION_PATH
        self.git('checkout','-q',self.base)
        o=json.loads(p.read_text());o.pop('base_tree_without_admission');p.write_text(json.dumps(o));self.base=self.commit()
        (self.root/'target').write_text('after');self.head=self.commit()
        with self.assertRaisesRegex(SemanticError,'baseline tree binding'):self.verify()
