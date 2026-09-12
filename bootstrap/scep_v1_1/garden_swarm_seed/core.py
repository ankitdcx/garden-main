from __future__ import annotations
import sqlite3, hashlib, json, time, uuid, random

RINGS={'R0':0,'R1':1,'R2':2,'R3':3,'R4':4}
VERIFIER_CLASSES={'COMPILE','FORMAL','SMT','SEMANTIC','PROPERTY_TEST','FUZZ','EMPIRICAL','SECURITY','INTEGRATION'}
SCHEMA='''
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS genesis_roots(root_id TEXT PRIMARY KEY,kind TEXT,version TEXT,artifact_hash TEXT,source_ref TEXT,protected INTEGER,status TEXT,created_at REAL);
CREATE TABLE IF NOT EXISTS gaps(gap_id TEXT PRIMARY KEY,title TEXT,gap_class TEXT,severity INTEGER,status TEXT,source_root TEXT,design_epoch TEXT,parent_gap_id TEXT,frontier TEXT,created_at REAL,closed_at REAL,accepted_submission_id TEXT);
CREATE TABLE IF NOT EXISTS gap_dependencies(gap_id TEXT,depends_on_gap_id TEXT,PRIMARY KEY(gap_id,depends_on_gap_id));
CREATE TABLE IF NOT EXISTS agents(agent_id TEXT PRIMARY KEY,provider TEXT,model_family TEXT,checkpoint TEXT,operator TEXT,parent_agent_id TEXT,roles_json TEXT,capabilities_json TEXT,network_scope_json TEXT,correlation_key TEXT,ring TEXT,compute_credit REAL DEFAULT 0,technical_reputation REAL DEFAULT 0,created_at REAL);
CREATE TABLE IF NOT EXISTS work_packages(wp_id TEXT PRIMARY KEY,gap_id TEXT,classification TEXT,source_root TEXT,design_epoch TEXT,required_capability TEXT,required_verifiers_json TEXT,max_budget REAL,spent_budget REAL DEFAULT 0,state TEXT,claimed_by TEXT,write_scope_json TEXT,network_scope_json TEXT,parent_wp_id TEXT,created_at REAL);
CREATE TABLE IF NOT EXISTS verifiers(verifier_id TEXT PRIMARY KEY,version TEXT,verifier_class TEXT,artifact_hash TEXT,pin_status TEXT,protected INTEGER,owner_agent_id TEXT,operator TEXT,correlation_key TEXT,scope_json TEXT,semantics TEXT,created_at REAL);
CREATE TABLE IF NOT EXISTS submissions(submission_id TEXT PRIMARY KEY,wp_id TEXT,agent_id TEXT,artifact_hash TEXT,artifact_text TEXT,claimed_frontier_value REAL,resource_cost REAL,status TEXT,created_at REAL);
CREATE TABLE IF NOT EXISTS verifier_receipts(receipt_id TEXT PRIMARY KEY,submission_id TEXT,verifier_id TEXT,result TEXT,evidence_hash TEXT,evidence_text TEXT,created_at REAL);
CREATE TABLE IF NOT EXISTS review_receipts(review_id TEXT PRIMARY KEY,submission_id TEXT,reviewer_agent_id TEXT,role TEXT,result TEXT,finding TEXT,correlation_key TEXT,created_at REAL);
CREATE TABLE IF NOT EXISTS frontier_reports(report_id TEXT PRIMARY KEY,gap_id TEXT,agent_id TEXT,kind TEXT,evidence_hash TEXT,evidence_text TEXT,value REAL,created_at REAL);
CREATE TABLE IF NOT EXISTS credits(credit_id TEXT PRIMARY KEY,agent_id TEXT,reason TEXT,amount REAL,source_ref TEXT,created_at REAL);
CREATE TABLE IF NOT EXISTS closure_receipts(closure_id TEXT PRIMARY KEY,gap_id TEXT,submission_id TEXT,artifact_hash TEXT,independent_review_clusters INTEGER,verifier_passes INTEGER,result TEXT,reward REAL,created_at REAL);
'''

def sha(s:str)->str: return hashlib.sha256(s.encode()).hexdigest()

class GardenSwarm:
    def __init__(self,path=':memory:'):
        self.db=sqlite3.connect(path); self.db.row_factory=sqlite3.Row; self.db.executescript(SCHEMA)
    def close(self): self.db.close()
    def add_genesis_root(self,root_id,kind,version,artifact_text,source_ref='',protected=True,status='ACTIVE'):
        self.db.execute('INSERT INTO genesis_roots VALUES(?,?,?,?,?,?,?,?)',(root_id,kind,version,sha(artifact_text),source_ref,1 if protected else 0,status,time.time())); self.db.commit(); return sha(artifact_text)
    def root_hash(self,root_id): return self.db.execute('SELECT artifact_hash FROM genesis_roots WHERE root_id=?',(root_id,)).fetchone()['artifact_hash']
    def register_agent(self,agent_id,provider,family,checkpoint,operator,roles=(),capabilities=(),network_scope=(),parent_agent_id=None,correlation_key=None,ring='R2'):
        if ring not in RINGS or ring in {'R0','R1'}: raise PermissionError('ordinary agent registration limited to R2-R4')
        ck=correlation_key or sha('|'.join([provider,family,checkpoint,operator,parent_agent_id or '']))[:24]
        self.db.execute('INSERT INTO agents VALUES(?,?,?,?,?,?,?,?,?,?,?,0,0,?)',(agent_id,provider,family,checkpoint,operator,parent_agent_id,json.dumps(list(roles)),json.dumps(list(capabilities)),json.dumps(list(network_scope)),ck,ring,time.time())); self.db.commit(); return ck
    def add_gap(self,gap_id,title,gap_class,severity,source_root,design_epoch,dependencies=(),frontier=None,parent_gap_id=None):
        if gap_class not in {'DERIVATION','DESIGN','DISCOVERY','BLOCKED'}: raise ValueError('gap_class')
        status='BLOCKED' if gap_class=='BLOCKED' else 'OPEN'
        self.db.execute('INSERT INTO gaps VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(gap_id,title,gap_class,severity,status,source_root,design_epoch,parent_gap_id,frontier,time.time(),None,None))
        for d in dependencies:self.db.execute('INSERT INTO gap_dependencies VALUES(?,?)',(gap_id,d))
        self.db.commit(); self.refresh_claimability()
    def refresh_claimability(self):
        for r in self.db.execute('SELECT gap_id,gap_class,status FROM gaps').fetchall():
            if r['gap_class']=='BLOCKED' or r['status'] in {'CLOSED','IN_PROGRESS','CANDIDATE'}: continue
            deps=self.db.execute('SELECT g.status FROM gap_dependencies d JOIN gaps g ON g.gap_id=d.depends_on_gap_id WHERE d.gap_id=?',(r['gap_id'],)).fetchall()
            self.db.execute('UPDATE gaps SET status=? WHERE gap_id=?',('CLAIMABLE' if all(x['status']=='CLOSED' for x in deps) else 'OPEN',r['gap_id']))
        self.db.commit()
    def create_work_package(self,wp_id,gap_id,max_budget,required_capability=None,required_verifiers=(),write_scope=(),network_scope=(),parent_wp_id=None):
        g=self.db.execute('SELECT * FROM gaps WHERE gap_id=?',(gap_id,)).fetchone()
        if not g: raise KeyError(gap_id)
        if parent_wp_id:
            p=self.db.execute('SELECT * FROM work_packages WHERE wp_id=?',(parent_wp_id,)).fetchone()
            if not p: raise KeyError(parent_wp_id)
            if max_budget>p['max_budget']-p['spent_budget']+1e-12: raise ValueError('child budget exceeds inherited remaining budget')
        st='CLAIMABLE' if g['status']=='CLAIMABLE' else 'BLOCKED'
        self.db.execute('INSERT INTO work_packages VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(wp_id,gap_id,g['gap_class'],g['source_root'],g['design_epoch'],required_capability,json.dumps(list(required_verifiers)),float(max_budget),0.0,st,None,json.dumps(list(write_scope)),json.dumps(list(network_scope)),parent_wp_id,time.time())); self.db.commit()
    def claim_work(self,wp_id,agent_id):
        w=self.db.execute('SELECT * FROM work_packages WHERE wp_id=?',(wp_id,)).fetchone(); a=self.db.execute('SELECT * FROM agents WHERE agent_id=?',(agent_id,)).fetchone()
        if not w or not a: raise KeyError('work/agent')
        if w['state']!='CLAIMABLE': raise ValueError('not claimable')
        if w['required_capability'] and w['required_capability'] not in json.loads(a['capabilities_json']): raise PermissionError('missing capability')
        needed=set(json.loads(w['network_scope_json'])); have=set(json.loads(a['network_scope_json']))
        if not needed.issubset(have): raise PermissionError('missing network/retrieval capability')
        self.db.execute("UPDATE work_packages SET state='CLAIMED',claimed_by=? WHERE wp_id=?",(agent_id,wp_id)); self.db.execute("UPDATE gaps SET status='IN_PROGRESS' WHERE gap_id=?",(w['gap_id'],)); self.db.commit()
    def spend(self,wp_id,amount):
        w=self.db.execute('SELECT * FROM work_packages WHERE wp_id=?',(wp_id,)).fetchone()
        if amount<0 or w['spent_budget']+amount>w['max_budget']+1e-12: raise ValueError('budget exceeded')
        self.db.execute('UPDATE work_packages SET spent_budget=spent_budget+? WHERE wp_id=?',(amount,wp_id)); self.db.commit()
    def submit(self,wp_id,agent_id,artifact_text,frontier_value,resource_cost):
        w=self.db.execute('SELECT * FROM work_packages WHERE wp_id=?',(wp_id,)).fetchone()
        if w['state']!='CLAIMED' or w['claimed_by']!=agent_id: raise PermissionError('not owner')
        self.spend(wp_id,resource_cost); sid='sub-'+uuid.uuid4().hex[:16]; ah=sha(artifact_text)
        self.db.execute('INSERT INTO submissions VALUES(?,?,?,?,?,?,?,?,?)',(sid,wp_id,agent_id,ah,artifact_text,float(frontier_value),float(resource_cost),'CANDIDATE',time.time())); self.db.execute("UPDATE work_packages SET state='SUBMITTED' WHERE wp_id=?",(wp_id,)); self.db.execute("UPDATE gaps SET status='CANDIDATE' WHERE gap_id=?",(w['gap_id'],)); self.db.commit(); return sid,ah
    def register_verifier(self,verifier_id,version,verifier_class,artifact_text,operator,semantics,scope=(),protected=True,owner_agent_id=None,correlation_key=None,pin_status='PINNED'):
        if verifier_class not in VERIFIER_CLASSES: raise ValueError('verifier_class')
        if pin_status=='PINNED' and not artifact_text: raise ValueError('cannot pin empty verifier artifact')
        ck=correlation_key or sha('|'.join([operator,verifier_class,version]))[:24]
        self.db.execute('INSERT INTO verifiers VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(verifier_id,version,verifier_class,sha(artifact_text) if artifact_text else '',pin_status,1 if protected else 0,owner_agent_id,operator,ck,json.dumps(list(scope)),semantics,time.time())); self.db.commit()
    def add_verifier_receipt(self,submission_id,verifier_id,result,evidence_text):
        s=self.db.execute('SELECT * FROM submissions WHERE submission_id=?',(submission_id,)).fetchone(); v=self.db.execute('SELECT * FROM verifiers WHERE verifier_id=?',(verifier_id,)).fetchone()
        if not s or not v: raise KeyError('submission/verifier')
        if v['pin_status']!='PINNED': raise PermissionError('un-pinned verifier cannot issue admission receipt')
        if v['protected'] and v['owner_agent_id']==s['agent_id']: raise PermissionError('protected self-verification')
        if result not in {'PASS','FAIL','UNKNOWN','INCONCLUSIVE'}: raise ValueError('result')
        rid='vr-'+uuid.uuid4().hex[:16]; self.db.execute('INSERT INTO verifier_receipts VALUES(?,?,?,?,?,?,?)',(rid,submission_id,verifier_id,result,sha(evidence_text),evidence_text,time.time())); self.db.commit(); return rid
    def add_review(self,submission_id,reviewer_agent_id,role,result,finding):
        a=self.db.execute('SELECT * FROM agents WHERE agent_id=?',(reviewer_agent_id,)).fetchone(); rid='rr-'+uuid.uuid4().hex[:16]
        self.db.execute('INSERT INTO review_receipts VALUES(?,?,?,?,?,?,?,?)',(rid,submission_id,reviewer_agent_id,role,result,finding,a['correlation_key'],time.time())); self.db.commit(); return rid
    def _credit(self,agent_id,reason,amount,source_ref):
        cid='cr-'+uuid.uuid4().hex[:16]; self.db.execute('INSERT INTO credits VALUES(?,?,?,?,?,?)',(cid,agent_id,reason,float(amount),source_ref,time.time())); self.db.execute('UPDATE agents SET compute_credit=compute_credit+?,technical_reputation=technical_reputation+? WHERE agent_id=?',(float(amount),max(0.0,float(amount)),agent_id)); return cid
    def report_frontier(self,gap_id,agent_id,kind,evidence_text,value=0.0):
        if kind not in {'BLOCKED','DISCOVERY','COUNTEREXAMPLE','REGRESSION'}: raise ValueError('kind')
        rid='fr-'+uuid.uuid4().hex[:16]; self.db.execute('INSERT INTO frontier_reports VALUES(?,?,?,?,?,?,?,?)',(rid,gap_id,agent_id,kind,sha(evidence_text),evidence_text,float(value),time.time()))
        if value>0:self._credit(agent_id,'frontier_'+kind.lower(),value,rid)
        self.db.commit(); return rid
    def independent_review_clusters(self,submission_id): return self.db.execute('SELECT COUNT(DISTINCT correlation_key) n FROM review_receipts WHERE submission_id=?',(submission_id,)).fetchone()['n']
    def review_roles(self,submission_id): return {r['role'] for r in self.db.execute('SELECT DISTINCT role FROM review_receipts WHERE submission_id=?',(submission_id,)).fetchall()}
    def try_close(self,submission_id,min_independent_review_clusters=1,required_review_roles=()):
        s=self.db.execute('SELECT * FROM submissions WHERE submission_id=?',(submission_id,)).fetchone(); w=self.db.execute('SELECT * FROM work_packages WHERE wp_id=?',(s['wp_id'],)).fetchone(); g=self.db.execute('SELECT * FROM gaps WHERE gap_id=?',(w['gap_id'],)).fetchone()
        rs=self.db.execute('SELECT r.*,v.verifier_class FROM verifier_receipts r JOIN verifiers v ON v.verifier_id=r.verifier_id WHERE r.submission_id=?',(submission_id,)).fetchall()
        if any(r['result']=='FAIL' for r in rs): return False,'verifier failure'
        if any(r['result'] in {'UNKNOWN','INCONCLUSIVE'} for r in rs): return False,'unresolved verifier result'
        passed={r['verifier_class'] for r in rs if r['result']=='PASS'}
        required=set(json.loads(w['required_verifiers_json']))
        missing=required-passed
        if missing:return False,'missing verifier '+','.join(sorted(missing))
        if self.independent_review_clusters(submission_id)<min_independent_review_clusters:return False,'insufficient independent review clusters'
        mr=set(required_review_roles)-self.review_roles(submission_id)
        if mr:return False,'missing roles '+','.join(sorted(mr))
        if self.db.execute("SELECT COUNT(*) n FROM review_receipts WHERE submission_id=? AND result='BLOCKER'",(submission_id,)).fetchone()['n']:return False,'unresolved blocker'
        if g['gap_class']=='DISCOVERY' and not ({'EMPIRICAL','SECURITY'} & passed):return False,'discovery gap requires empirical/security evidence path'
        sev={1:1,2:2,3:4,4:8,5:16}[g['severity']]; total=self.db.execute('SELECT COUNT(*) n FROM review_receipts WHERE submission_id=?',(submission_id,)).fetchone()['n']; clusters=self.independent_review_clusters(submission_id); redundancy=max(0,total-clusters)*0.05
        reward=max(0.0,sev*s['claimed_frontier_value']-s['resource_cost']-redundancy); cid='cl-'+uuid.uuid4().hex[:16]
        self.db.execute('INSERT INTO closure_receipts VALUES(?,?,?,?,?,?,?,?,?)',(cid,g['gap_id'],submission_id,s['artifact_hash'],clusters,sum(1 for r in rs if r['result']=='PASS'),'PASS_SCOPED',reward,time.time())); self.db.execute("UPDATE submissions SET status='ACCEPTED' WHERE submission_id=?",(submission_id,)); self.db.execute("UPDATE work_packages SET state='CLOSED' WHERE wp_id=?",(w['wp_id'],)); self.db.execute("UPDATE gaps SET status='CLOSED',closed_at=?,accepted_submission_id=? WHERE gap_id=?",(time.time(),submission_id,g['gap_id'])); self._credit(s['agent_id'],'verified_frontier_reduction',reward,cid); self.db.commit(); self.refresh_claimability(); return True,cid
    def agent_credit(self,agent_id):return self.db.execute('SELECT compute_credit FROM agents WHERE agent_id=?',(agent_id,)).fetchone()['compute_credit']
    def gap_status(self,gap_id):return self.db.execute('SELECT status FROM gaps WHERE gap_id=?',(gap_id,)).fetchone()['status']
    def simulation_10k(self,n=10000):
        for i in range(n):self.register_agent(f'sim-{i}',f'p-{i%11}',f'f-{i%17}',f'c-{i%97}',f'o-{i%37}',roles=('WORKER',),capabilities=('CODE',),correlation_key=f'corr-{i%503}')
        return {'agents':n,'unique_correlation_clusters':self.db.execute("SELECT COUNT(DISTINCT correlation_key) n FROM agents WHERE agent_id LIKE 'sim-%'").fetchone()['n']}
