import hashlib, json, tempfile, unittest
from pathlib import Path
from scripts import check_git_preflight_event as preflight
from scripts import render_git_operating_context as render
from scripts import secret_scan
ROOT=Path(__file__).resolve().parents[2]
class GitProcessV2Tests(unittest.TestCase):
 def test_source_revision_and_generated_views_match(self):
  data,sha=render.canonical_source(ROOT/'GIT_OPERATING_CONTEXT_SOURCE.json'); self.assertEqual(data['schema'],'GardenGitOperatingContextSource/v2'); self.assertGreaterEqual(data['document_revision'],2); machine,human=render.render(ROOT/'GIT_OPERATING_CONTEXT_SOURCE.json'); self.assertEqual((ROOT/'GIT_OPERATING_CONTEXT.json').read_text(),machine); self.assertEqual((ROOT/'GIT_OPERATING_CONTEXT.md').read_text(),human); self.assertIn(sha,machine)
 def test_bad_merge_recovery_never_rewrites_main(self):
  source=json.loads((ROOT/'GIT_OPERATING_CONTEXT_SOURCE.json').read_text()); self.assertTrue(source['recovery']['bad_merge']['never_reset_or_force_push_main'])
 def test_preflight_required_for_chatgpt_branch(self):
  source=json.loads((ROOT/'GIT_OPERATING_CONTEXT_SOURCE.json').read_text()); event={'repository':{'full_name':'ankitdcx/garden-main'},'pull_request':{'head':{'ref':'chatgpt/x'},'base':{'sha':'1'*40},'body':''}}; result=preflight.validate_event(event,source); self.assertEqual(result['status'],'BLOCKED')
 def test_secret_scanner_detects_constructed_token_without_printing_it(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'x.txt'; token='sk-'+('A'*30); p.write_text('api_key = "'+token+'"\n'); receipt=secret_scan.scan_paths(['x.txt'],root=Path(td),allowlist=[]); self.assertEqual(receipt['status'],'BLOCKED'); self.assertNotIn(token,json.dumps(receipt))
if __name__=='__main__': unittest.main()
