"""Adversarial conformance, exact algebra and physical null tests for SIC-0.1."""
import copy
import itertools
import random
import unittest
from dataclasses import replace
from fractions import Fraction
import electricity_closure as c
import electricity_experiment as e
from electricity_seed import build_seed
try:
    from scipy.optimize import linprog
except ImportError:
    linprog=None


def det(a):
    if len(a)==1: return a[0][0]
    return sum((-1)**j*a[0][j]*det([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)))


def rank_minors(a):
    for size in range(min(len(a),len(a[0])),0,-1):
        for rows in itertools.combinations(range(len(a)),size):
            for cols in itertools.combinations(range(len(a[0])),size):
                if det([[a[i][j] for j in cols] for i in rows]): return size
    return 0


class AlgebraTests(unittest.TestCase):
    def test_nullspace_against_independent_minor_rank(self):
        rng=random.Random(921)
        for _ in range(120):
            m,n=rng.randint(1,3),rng.randint(1,5)
            a=[[rng.randint(-3,3) for _ in range(n)] for _ in range(m)]
            k=[rng.randint(-3,3) for _ in range(n)]
            w=c.projection_witness(a,k)
            closed=rank_minors(a)==rank_minors(a+[k])
            self.assertEqual(closed,w['status']=='CLOSED_FOR_DECLARED_LINEAR_RESPONSE')
            if not closed:
                x1,x2=list(map(Fraction,w['x1'])),list(map(Fraction,w['x2']))
                self.assertGreaterEqual(min(x1+x2),0)
                self.assertEqual([c.dot(r,x1) for r in a],[c.dot(r,x2) for r in a])
                self.assertNotEqual(c.dot(k,x1),c.dot(k,x2))

    def test_basis_synthesis_and_resource_boundary(self):
        self.assertEqual(c.synthesize_interface(((1,1),),[('k',(1,2))],0)['status'],'INCOMPLETE')
        r=c.synthesize_interface(((1,1),),[('k',(1,2))])
        self.assertEqual(c.projection_witness(r['rows'],[1,2])['status'],'CLOSED_FOR_DECLARED_LINEAR_RESPONSE')
        with self.assertRaises(ValueError): c.projection_witness([[1,2]],[1])

    def test_lp_extrema_and_dual_certificate(self):
        a=[[1,1,1],[1,0,0]]; y=['1','1/5']; k=[2,5,11]
        b=c.moment_bounds(a,y,k)
        self.assertEqual(Fraction(b['lower']),Fraction(22,5))
        self.assertEqual(Fraction(b['upper']),Fraction(46,5))
        self.assertTrue(c.verify_bounds_certificate(b,a,y,k))
        fake=copy.deepcopy(b); fake['upper']='1'
        self.assertFalse(c.verify_bounds_certificate(fake,a,y,k))
        self.assertFalse(c.verify_bounds_certificate(b,a,y,[20,50,110]))

    def test_lp_failed_prerequisites(self):
        self.assertEqual(c.moment_bounds([[1,1]],[-1],[1,2])['status'],'INFEASIBLE')
        self.assertEqual(c.moment_bounds([[1,0]],[1],[1,2])['status'],'UNKNOWN')
        self.assertEqual(c.moment_bounds([[1,1],[2,2]],[1,2],[1,2])['status'],'UNKNOWN')
        self.assertEqual(c.moment_bounds([[1,1]],[1],[1,2],0)['status'],'INCOMPLETE')
        self.assertEqual(c.interval_decision({'status':'INCOMPLETE'},10),'UNKNOWN')

    def test_interval_ambiguity(self):
        b=c.moment_bounds([[1,1]],[1],[1,3])
        self.assertEqual(c.interval_decision(b,2),'NEED_ADDITIONAL_MEASUREMENT')
        self.assertEqual(c.interval_decision(b,3),'MODEL_FEASIBLE')
        self.assertEqual(c.interval_decision(b,0),'MODEL_INFEASIBLE')

    def test_noisy_dual_encloses_corners(self):
        a=[[1,0,0],[1,1,1]]; y=[Fraction(1,5),1]; k=[2,5,11]
        b=c.moment_bounds(a,y,k)
        lo=[Fraction(1,10),Fraction(9,10)]; hi=[Fraction(3,10),Fraction(11,10)]
        outer=c.uncertain_bounds(b,lo,hi,coefficient_error=1)
        self.assertEqual(outer['status'],'CERTIFIED_OUTER_MODEL_BOUND')
        for v in itertools.product(*zip(lo,hi)):
            truth=c.moment_bounds(a,v,k)
            self.assertLessEqual(Fraction(outer['lower']),Fraction(truth['lower']))
            self.assertGreaterEqual(Fraction(outer['upper']),Fraction(truth['upper']))
        self.assertEqual(c.uncertain_bounds(b,[2,2],[3,3])['status'],'UNKNOWN')

    def test_profile_cannot_launder_other_model_certificate(self):
        profile=dict(kernel_id='K',harmonics=[1,5],units='W',window_id='W1',aggregate_terminal_scope=True,
                     mathematics=dict(A=[[1,1]],y=[1],k=[1,2]))
        packet={k:v for k,v in profile.items() if k!='mathematics'}
        packet['bounds']=c.moment_bounds([[1,1]],[1],[1,2])
        self.assertEqual(c.qualified_decision(packet,profile,3),'MODEL_FEASIBLE')
        profile['mathematics']['k']=[10,20]
        self.assertEqual(c.qualified_decision(packet,profile,3),'UNKNOWN')
        packet['kernel_id']='old'
        self.assertEqual(c.qualified_decision(packet,profile,3),'NEEDS_REVALIDATION')


class GraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.seed=build_seed(c.ROOT)

    def test_source_and_hierarchy_bindings(self):
        ids={x['id'] for x in self.seed['decomposition']}
        self.assertEqual({s['stage'] for s in self.seed['situations']},set(range(1,15)))
        for s in self.seed['situations']:
            self.assertIn(s['parent_id'],ids); self.assertTrue(s['expansion_reason'])
        for src in self.seed['garden_sources']:
            self.assertEqual(src['status'],'NONCANONICAL_SOURCE_BOUND')
            raw=(c.ROOT/src['path']).read_bytes()
            import hashlib
            self.assertEqual(hashlib.sha256(raw).hexdigest(),src['source_sha256'])
            self.assertEqual(hashlib.sha256(raw[src['byte_start']:src['byte_end']]).hexdigest(),src['span_sha256'])

    def test_missing_signature_never_defaults_to_success(self):
        self.assertEqual(c.classify_triple('THING','dependsOn','THING',{}),'UNRESOLVED')
        self.assertEqual(c.classify_triple(None,'dependsOn','THING'),'UNRESOLVED')
        self.assertEqual(c.l0_inventory()['raw'],2400)

    def test_unknown_and_malformed_binding_preserved(self):
        s=copy.deepcopy(self.seed['situations'][0]); s['objects'][0].pop('id')
        s['relations'][0].pop('source')
        s['facets']['EffectsSafety']={'status':'UNKNOWN','reason':'not determined'}
        r=c.sal(s)
        self.assertIn('UNRESOLVED',r['structural_status'])
        self.assertIn('UNKNOWN_FACET:EffectsSafety',r['missing_bindings'])
        self.assertEqual(r['completeness_status'],'CONTEXT_REQUIRED')

    def test_consumer_missing_port_and_fake_external_binding(self):
        a=dict(id='a',inputs=[],outputs=[dict(name='power',unit='W')])
        b=dict(id='b',inputs=[dict(name='power',unit='W'),dict(name='temp',unit='K')],outputs=[],
               external_bindings=[dict(name='temp',unit='kg',source_ref='missing')])
        seed=dict(situations=[a,b],transitions=[dict(id='ab',source='a',target='b',transfers=['power'])],sources=[])
        self.assertEqual(c.audit_consumer_inputs(seed)[1]['unbound_inputs'],['temp'])

    def test_units_and_unknown_endpoint(self):
        seed=copy.deepcopy(self.seed)
        edge=seed['transitions'][0]; edge['target']='missing'
        self.assertIn('UNKNOWN_ENDPOINT',c.audit_transitions(seed)[0]['diagnostics'])
        with self.assertRaises(ValueError): c.audit_combinations(seed,-1)

    def test_finite_resource_boundary(self):
        self.assertEqual(c.bounded_dependency_closure(self.seed,0)['status'],'INCOMPLETE')
        out=c.bounded_dependency_closure(self.seed)
        self.assertEqual(out['status'],'BOUNDED_FIXED_POINT')
        self.assertEqual(out['physical_completeness'],'UNKNOWN')

    def test_deterministic_replay(self):
        self.assertEqual(c.run(self.seed),c.run(self.seed))


class PhysicsTests(unittest.TestCase):
    def test_null_and_strong_baseline(self):
        contract=e.Contract()
        for h in (5,7,11,13):
            s=e.spectrum_at(800,h)
            self.assertAlmostEqual(e.full_loss(s,contract),e.moment_loss(s,contract),places=8)
        pure={1:800}
        self.assertAlmostEqual(e.full_loss(pure,contract),e.coarse_loss(pure,contract))
        resistive=replace(contract,eddy_w=0,stray_w=0)
        self.assertAlmostEqual(e.full_loss(e.spectrum_at(800,13),resistive),e.coarse_loss(e.spectrum_at(800,13),resistive))

    def test_negative_and_out_of_domain_rejected(self):
        for fn in (lambda:e.feasible({1:10},-1,e.Contract()),lambda:e.spectrum_at(10,1),
                   lambda:e.capacity_oracle(15,.2,e.Contract()),lambda:e.coarse_loss({1:10},e.Contract(),-1)):
            with self.assertRaises(ValueError): fn()
        self.assertIsNone(e.capacity_oracle(5,.2,replace(e.Contract(),core_w=100000)))
        self.assertGreater(e.capacity_oracle(5,.2,replace(e.Contract(),dc_w=0,eddy_w=0,stray_w=0)),0)

    def test_predeclared_physical_prediction(self):
        c0=e.Contract(); lo=e.full_loss(e.spectrum_at(950,5),c0); hi=e.full_loss(e.spectrum_at(950,13),c0)
        self.assertGreater(hi-lo,1500)
        self.assertLess(e.thermal_proxy(lo,c0),105)
        self.assertGreater(e.thermal_proxy(hi,c0),105)
        self.assertGreater(e.capacity_oracle(5,.2,c0)-e.capacity_oracle(13,.2,c0),150)


@unittest.skipIf(linprog is None,'optional SciPy independent-solver comparison')
class IndependentSolverTests(unittest.TestCase):
    def test_exact_lp_against_highs(self):
        rng=random.Random(8198); certified=0
        for _ in range(200):
            n=rng.randint(2,7); m=rng.randint(1,min(4,n))
            a=[[1]*n]+[[rng.randint(-3,3) for _ in range(n)] for _ in range(m-1)]
            x=[Fraction(rng.randint(0,10),10) for _ in range(n)]
            y=[c.dot(row,x) for row in a]; k=[rng.randint(-5,5) for _ in range(n)]
            bound=c.moment_bounds(a,y,k)
            if bound['status']!='CERTIFIED_FOR_SUPPLIED_RATIONAL_MODEL':
                self.assertEqual(bound['status'],'UNKNOWN'); continue
            certified+=1
            low=linprog(k,A_eq=a,b_eq=list(map(float,y)),bounds=(0,None),method='highs')
            high=linprog([-v for v in k],A_eq=a,b_eq=list(map(float,y)),bounds=(0,None),method='highs')
            self.assertTrue(low.success and high.success)
            self.assertAlmostEqual(float(Fraction(bound['lower'])),low.fun,places=8)
            self.assertAlmostEqual(float(Fraction(bound['upper'])),-high.fun,places=8)
            self.assertTrue(c.verify_bounds_certificate(bound,a,y,k))
        self.assertEqual(certified,195)


if __name__=='__main__': unittest.main()
