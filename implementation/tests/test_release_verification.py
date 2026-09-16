import tempfile
import unittest
from pathlib import Path
import importlib.util

from garden_kernel.release_verification import verify_release

ASSURANCE_DEPS_AVAILABLE = all(importlib.util.find_spec(name) is not None
                               for name in ('tuf', 'in_toto', 'securesystemslib'))
if ASSURANCE_DEPS_AVAILABLE:
    from supply_chain_fixture import fixture


def public_args(values):
    return {key: value for key, value in values.items() if not key.startswith('_test_')}


@unittest.skipUnless(ASSURANCE_DEPS_AVAILABLE,
                     'install requirements/assurance.txt to run release-verification qualification')
class ReleaseVerificationTests(unittest.TestCase):
    def run_case(self, case='valid', **kwargs):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        values = fixture(directory.name, case=case, **kwargs)
        return verify_release(**public_args(values)), values

    def test_valid_conjunctive_release(self):
        receipt, _ = self.run_case()
        self.assertEqual(receipt['status'], 'VERIFIED')
        self.assertFalse(receipt['promotion_authorized'])

    def test_expired_metadata(self):
        receipt, _ = self.run_case('expired')
        self.assertEqual(receipt['status'], 'BLOCKED')
        self.assertEqual(receipt['checks']['tuf']['status'], 'INVALID')

    def test_insufficient_signatures(self):
        receipt, _ = self.run_case('insufficient_signatures')
        self.assertEqual(receipt['status'], 'BLOCKED')
        self.assertEqual(receipt['checks']['tuf']['status'], 'INVALID')

    def test_unauthorized_builder(self):
        receipt, _ = self.run_case('unauthorized_builder')
        self.assertEqual(receipt['status'], 'BLOCKED')
        self.assertEqual(receipt['checks']['in_toto']['status'], 'INVALID')

    def test_missing_step(self):
        receipt, _ = self.run_case('missing_step')
        self.assertEqual(receipt['status'], 'BLOCKED')
        self.assertEqual(receipt['checks']['in_toto']['status'], 'INVALID')

    def test_substituted_content(self):
        receipt, _ = self.run_case('substituted_content')
        self.assertEqual(receipt['status'], 'BLOCKED')
        self.assertEqual(receipt['checks']['tuf']['status'], 'INVALID')

    def test_cross_stage_hash_mismatch(self):
        receipt, _ = self.run_case('cross_stage_mismatch')
        self.assertEqual(receipt['status'], 'BLOCKED')
        self.assertEqual(receipt['checks']['artifact_identity']['status'], 'INVALID')

    def test_missing_layout_is_typed_failure(self):
        receipt, values = self.run_case()
        Path(values['layout_path']).unlink()
        receipt = verify_release(**public_args(values))
        self.assertEqual(receipt['status'], 'BLOCKED')
        self.assertEqual(receipt['checks']['in_toto']['status'], 'INVALID')
        self.assertIn('FileNotFoundError', receipt['checks']['in_toto']['reason'])

    def test_missing_link_is_typed_failure(self):
        receipt, values = self.run_case()
        next(Path(values['link_dir']).glob('*.link')).unlink()
        receipt = verify_release(**public_args(values))
        self.assertEqual(receipt['status'], 'BLOCKED')
        self.assertEqual(receipt['checks']['in_toto']['status'], 'INVALID')

    def test_signed_root_rotation_revokes_old_online_role_keys(self):
        receipt, values = self.run_case(version=2, rotate_root=True)
        self.assertEqual(receipt['status'], 'VERIFIED', receipt)
        cached_root = Path(values['metadata_dir'], 'root.json').read_bytes()
        self.assertIn(b'"version":2', cached_root)
        self.assertEqual(receipt['active_trusted_root_version'], 2)
        self.assertEqual(receipt['active_trusted_root_sha256'],
                         values['_test_trust_state']['rotated_root_sha256'])
        old_target_ids = {s.public_key.keyid for s in values['_test_trust_state']['keys']['targets']}
        for keyid in old_target_ids:
            self.assertNotIn(keyid.encode(), cached_root)

    def test_persistent_cache_rejects_metadata_version_rollback(self):
        with tempfile.TemporaryDirectory() as directory:
            newer = fixture(directory, version=2)
            first = verify_release(**public_args(newer))
            self.assertEqual(first['status'], 'VERIFIED', first)
            older = fixture(directory, version=1, trust_state=newer['_test_trust_state'])
            second = verify_release(**public_args(older))
            self.assertEqual(second['status'], 'BLOCKED')
            self.assertEqual(second['checks']['tuf']['status'], 'INVALID')
            self.assertRegex(second['checks']['tuf']['reason'].lower(), 'rollback|version')


if __name__ == '__main__':
    unittest.main()
