import unittest
from garden_swarm_seed.core import GardenSwarm
class T(unittest.TestCase):
 def setUp(self):
  self.g=GardenSwarm(':memory:'); self.g.add_genesis_root('SRC','SOURCE','1','garden-source','src')
  self.g.register_agent('A','p','fa','ca','oa',roles=('BUILD',),capabilities=('CODE',),network_scope=(),correlation_key='A')
  self.g.register_agent('B','p2','fb','cb','ob',roles=('RED',),capabilities=('REVIEW',),network_scope=(),correlation_key='B')
  self.g.register_agent('C','p3','fc','cc','oc',roles=('IMPL',),capabilities=('REVIEW',),network_scope=(),correlation_key='C')
 def tearDown(self):self.g.close()
 def cand(self,gclass='DESIGN',req=('SEMANTIC',)):
  self.g.add_gap('G','x',gclass,4,'root','E1');self.g.create_work_package('W','G',10,'CODE',req);self.g.claim_work('W','A');return self.g.submit('W','A','artifact',1,1)[0]
 def sem(self,owner=None,pin='PINNED'):
  self.g.register_verifier('V','1','SEMANTIC','checker','op','semantic corpus',owner_agent_id=owner,pin_status=pin)
 def test_root_hash(self):self.assertEqual(len(self.g.root_hash('SRC')),64)
 def test_agent_cannot_register_r0(self):
  with self.assertRaises(PermissionError):self.g.register_agent('X','p','f','c','o',ring='R0')
 def test_no_ambient_network(self):
  self.g.add_gap('G','x','DESIGN',2,'r','E');self.g.create_work_package('W','G',1,'CODE',(),network_scope=('WEB',))
  with self.assertRaises(PermissionError):self.g.claim_work('W','A')
 def test_unpinned_verifier_rejected(self):
  s=self.cand();self.sem(pin='UNPINNED')
  with self.assertRaises(PermissionError):self.g.add_verifier_receipt(s,'V','PASS','x')
 def test_self_verify_rejected(self):
  s=self.cand();self.sem(owner='A')
  with self.assertRaises(PermissionError):self.g.add_verifier_receipt(s,'V','PASS','x')
 def test_compile_not_semantic(self):
  s=self.cand(req=('SEMANTIC',));self.g.register_verifier('VC','1','COMPILE','compiler','op','compile only');self.g.add_verifier_receipt(s,'VC','PASS','built');self.g.add_review(s,'B','RED','SUPPORT','ok');ok,msg=self.g.try_close(s);self.assertFalse(ok);self.assertIn('SEMANTIC',msg)
 def test_formal_not_empirical_discovery(self):
  s=self.cand('DISCOVERY',('FORMAL',));self.g.register_verifier('VF','1','FORMAL','proof','op','formal');self.g.add_verifier_receipt(s,'VF','PASS','proof');self.g.add_review(s,'B','RED','SUPPORT','ok');ok,msg=self.g.try_close(s);self.assertFalse(ok);self.assertIn('empirical/security',msg)
 def test_empirical_discovery(self):
  s=self.cand('DISCOVERY',('EMPIRICAL',));self.g.register_verifier('VE','1','EMPIRICAL','measurement-protocol','lab','measurement');self.g.add_verifier_receipt(s,'VE','PASS','measured');self.g.add_review(s,'B','RED','SUPPORT','ok');ok,_=self.g.try_close(s);self.assertTrue(ok)
 def test_blocked_report_no_penalty(self):
  self.g.add_gap('G','x','DISCOVERY',3,'r','E');before=self.g.agent_credit('A');self.g.report_frontier('G','A','BLOCKED','missing sensor',2);self.assertGreaterEqual(self.g.agent_credit('A'),before)
 def test_counterexample_credit(self):
  self.g.add_gap('G','x','DESIGN',3,'r','E');before=self.g.agent_credit('B');self.g.report_frontier('G','B','COUNTEREXAMPLE','bug',3);self.assertGreater(self.g.agent_credit('B'),before)
 def test_correlation(self):
  s=self.cand();self.g.register_agent('B2','p2','fb','cb','ob',roles=('R',),capabilities=('REVIEW',),correlation_key='B');self.g.add_review(s,'B','R1','SUPPORT','x');self.g.add_review(s,'B2','R2','SUPPORT','y');self.assertEqual(self.g.independent_review_clusters(s),1)
 def test_budget(self):
  self.g.add_gap('G','x','DESIGN',2,'r','E');self.g.create_work_package('W','G',1,'CODE');self.g.claim_work('W','A')
  with self.assertRaises(ValueError):self.g.submit('W','A','x',1,2)
 def test_success(self):
  s=self.cand();self.sem();self.g.add_verifier_receipt(s,'V','PASS','ok');self.g.add_review(s,'B','RED','SUPPORT','ok');self.g.add_review(s,'C','IMPL','SUPPORT','ok');ok,_=self.g.try_close(s,min_independent_review_clusters=2,required_review_roles=('RED','IMPL'));self.assertTrue(ok);self.assertGreater(self.g.agent_credit('A'),0)
 def test_blocker(self):
  s=self.cand();self.sem();self.g.add_verifier_receipt(s,'V','PASS','ok');self.g.add_review(s,'B','RED','BLOCKER','bad');ok,_=self.g.try_close(s);self.assertFalse(ok)
 def test_unknown(self):
  s=self.cand();self.sem();self.g.add_verifier_receipt(s,'V','UNKNOWN','?');self.g.add_review(s,'B','RED','SUPPORT','ok');ok,_=self.g.try_close(s);self.assertFalse(ok)
 def test_10k(self):
  r=self.g.simulation_10k();self.assertEqual(r['agents'],10000);self.assertEqual(r['unique_correlation_clusters'],503)
if __name__=='__main__':unittest.main()
