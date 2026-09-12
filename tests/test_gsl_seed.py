import unittest
from gsl_seed import (
    PROFILE, CoreObject, ClaimStatus, DependencyKind, GSLSeedError,
    parse_obj, TransitionEvidence, transition_claim, EpistemicTransitionError
)

def base():
    return {
        "profile": PROFILE,
        "nodes": [
            {"id":"CTX1","kind":"CONTEXT","fields":{"domain":{"type":"String","value":"bootstrap"}}},
            {"id":"EV1","kind":"EVENT","fields":{"description":{"type":"String","value":"observed fixture"}}}
        ],
        "claims": [
            {"id":"C1","proposition":"Parser preserves claim status","status":"HYPOTHESIS","context_ref":"CTX1","evidence_refs":["EV1"],"scope":"seed"}
        ],
        "dependencies": [],
        "obligations": [
            {"id":"O1","proposition":"Preserve status","owner":"Engine.Compile","status":"PENDING","dependency_refs":[]}
        ],
        "tests": [
            {"id":"T1","obligation_ref":"O1","description":"round trip","expected":"status unchanged"}
        ],
        "receipts": []
    }

class SeedKernelTests(unittest.TestCase):
    def test_ten_core_objects_exact(self):
        self.assertEqual({x.value for x in CoreObject},{"TIME","SPACE","THING","EVENT","ACTION","AGENCY","RULE","VALUE","CONTEXT","CLAIM"})
    def test_parse_valid_document(self):
        doc=parse_obj(base()); self.assertEqual(doc.claims[0].status,ClaimStatus.HYPOTHESIS); self.assertEqual(doc.nodes[0].kind,CoreObject.CONTEXT)
    def test_unknown_profile_fails(self):
        x=base(); x["profile"]="GSL-FUTURE"
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_unknown_core_object_fails(self):
        x=base(); x["nodes"][0]["kind"]="META_OBJECT"
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_unknown_claim_status_fails(self):
        x=base(); x["claims"][0]["status"]="TRUE"
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_missing_context_fails(self):
        x=base(); x["claims"][0]["context_ref"]="MISSING"
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_missing_evidence_ref_fails(self):
        x=base(); x["claims"][0]["evidence_refs"]=["NOPE"]
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_duplicate_ids_fail(self):
        x=base(); x["nodes"][1]["id"]="CTX1"
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_build_dependency_cycle_fails(self):
        x=base(); x["obligations"].append({"id":"O2","proposition":"x","owner":"Engine.Compile","status":"PENDING","dependency_refs":[]}); x["dependencies"]=[{"source_ref":"O1","target_ref":"O2","kind":"BUILD"},{"source_ref":"O2","target_ref":"O1","kind":"BUILD"}]
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_runtime_feedback_explicit_allowed(self):
        x=base(); x["dependencies"]=[{"source_ref":"C1","target_ref":"C1","kind":"RUNTIME","feedback_group":"FG1"}]; doc=parse_obj(x); self.assertEqual(doc.dependencies[0].kind,DependencyKind.RUNTIME)
    def test_build_self_dependency_fails(self):
        x=base(); x["dependencies"]=[{"source_ref":"O1","target_ref":"O1","kind":"BUILD"}]
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_receipt_missing_subject_fails(self):
        x=base(); x["receipts"]=[{"id":"R1","subject_ref":"NOPE","result":"PASS_SCOPED","checker_ref":"checker"}]
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_epistemic_status_does_not_auto_promote_from_evidence(self):
        self.assertEqual(parse_obj(base()).claims[0].status,ClaimStatus.HYPOTHESIS)
    def test_transition_requires_evidence(self):
        claim=parse_obj(base()).claims[0]
        with self.assertRaises(EpistemicTransitionError): transition_claim(claim,ClaimStatus.SUPPORTED_WITH_SCOPE,TransitionEvidence("EMPIRICAL",()))
    def test_transition_is_explicit_and_scoped(self):
        claim=parse_obj(base()).claims[0]; out=transition_claim(claim,ClaimStatus.SUPPORTED_WITH_SCOPE,TransitionEvidence("EMPIRICAL",("EV1",),"seed-only")); self.assertEqual(out.status,ClaimStatus.SUPPORTED_WITH_SCOPE); self.assertEqual(out.scope,"seed-only")
    def test_direct_hypothesis_to_qualified_knowledge_rejected(self):
        claim=parse_obj(base()).claims[0]
        with self.assertRaises(EpistemicTransitionError): transition_claim(claim,ClaimStatus.QUALIFIED_KNOWLEDGE,TransitionEvidence("EMPIRICAL",("EV1",),"seed"))
    def test_runtime_two_node_cycle_requires_feedback_group(self):
        x=base(); x["obligations"].append({"id":"O2","proposition":"x","owner":"Engine.Reason","status":"PENDING","dependency_refs":[]}); x["dependencies"]=[{"source_ref":"O1","target_ref":"O2","kind":"RUNTIME"},{"source_ref":"O2","target_ref":"O1","kind":"RUNTIME"}]
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_runtime_two_node_cycle_with_shared_feedback_group_allowed(self):
        x=base(); x["obligations"].append({"id":"O2","proposition":"x","owner":"Engine.Reason","status":"PENDING","dependency_refs":[]}); x["dependencies"]=[{"source_ref":"O1","target_ref":"O2","kind":"RUNTIME","feedback_group":"FG1"},{"source_ref":"O2","target_ref":"O1","kind":"RUNTIME","feedback_group":"FG1"}]
        self.assertEqual(len(parse_obj(x).dependencies),2)
    def test_runtime_cycle_mismatched_feedback_groups_fails(self):
        x=base(); x["obligations"].append({"id":"O2","proposition":"x","owner":"Engine.Reason","status":"PENDING","dependency_refs":[]}); x["dependencies"]=[{"source_ref":"O1","target_ref":"O2","kind":"RUNTIME","feedback_group":"FG1"},{"source_ref":"O2","target_ref":"O1","kind":"RUNTIME","feedback_group":"FG2"}]
        with self.assertRaises(GSLSeedError): parse_obj(x)
    def test_logical_cycle_fails(self):
        x=base(); x["obligations"].append({"id":"O2","proposition":"x","owner":"Engine.Reason","status":"PENDING","dependency_refs":[]}); x["dependencies"]=[{"source_ref":"O1","target_ref":"O2","kind":"LOGICAL"},{"source_ref":"O2","target_ref":"O1","kind":"LOGICAL"}]
        with self.assertRaises(GSLSeedError): parse_obj(x)

if __name__=="__main__": unittest.main()
