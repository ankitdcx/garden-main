import importlib.util,json,subprocess,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2];spec=importlib.util.spec_from_file_location('permission_checker',ROOT/'scripts/check_permission_recovery.py');checker=importlib.util.module_from_spec(spec);spec.loader.exec_module(checker)
class CheckerTests(unittest.TestCase):
    def test_complete_positive_requires_marker_and_counts(self):
        out='Model checking completed. No error has been found.\n12 states generated, 7 distinct states found\nThe depth of the complete state graph search is 4.'
        self.assertEqual(checker.classify(out,0)['outcome'],'COMPLETED_WITHIN_BOUNDS');self.assertEqual(checker.classify(out.replace('12 states generated',''),0)['outcome'],'INCOMPLETE')
    def test_negative_requires_named_invariant(self):
        counts='\n12 states generated, 7 distinct states found\nThe depth of the complete state graph search is 4.'
        good=checker.classify('Invariant NoStaleFenceAccepted is violated.'+counts,12,negative=True);bad=checker.classify('Invariant TypeOK is violated.'+counts,12,negative=True)
        self.assertEqual(good['violated_invariant'],'NoStaleFenceAccepted');self.assertEqual(bad['reason'],'UNEXPECTED_OR_WRONG_INVARIANT_COUNTEREXAMPLE')
        self.assertEqual(checker.classify('Invariant NoStaleFenceAccepted is violated.'+counts,0,negative=True)['outcome'],'INCOMPLETE')
        mixed=checker.classify('Invariant NoStaleFenceAccepted is violated.\nInvariant TypeOK is violated.'+counts,12,negative=True)
        self.assertNotEqual(mixed.get('violated_invariant'),'NoStaleFenceAccepted')
    def test_timeout_is_incomplete(self):
        with patch.object(checker.subprocess,'run',side_effect=subprocess.TimeoutExpired(['java'],1)):r=checker.run_tlc(Path('/tmp/x'),checker.CONFIG,1)
        self.assertEqual((r['outcome'],r['reason']),('INCOMPLETE','TIMEOUT'))
    def test_cli_refuses_wrong_jar_hash_as_incomplete(self):
        with tempfile.TemporaryDirectory() as td:
            jar=Path(td)/'tool.jar';jar.write_bytes(b'not-tlc');out=Path(td)/'receipt.json'
            p=subprocess.run(['python',str(ROOT/'scripts/check_permission_recovery.py'),'--tlc-jar',str(jar),'--output',str(out)],text=True,capture_output=True)
            receipt=json.loads(out.read_text())
        self.assertEqual(p.returncode,2);self.assertEqual(receipt['positive']['reason'],'TOOL_SHA256_MISMATCH');self.assertEqual(receipt['adjudication']['result'],'INCOMPLETE')
if __name__=='__main__':unittest.main()
