"""100 domain×motif synthetic sanity checks; no empirical scientific validation."""
import csv, numpy as np
rng=np.random.default_rng(20261010)
domains=["battery","water","heat_exchanger","grid","robot","PFAS","bioreactor","soil","solar","bearing"]
motifs=["boundary-history","sensor-loss","coupling-cross-term","switching-dwell","delayed-feedback","uncertainty-budget","spatial-decomposition","rare-transition","actuator-budget","multi-timescale"]
rows=[]
for i,domain in enumerate(domains):
 a=.3+.1*i;c=.4+.07*i;b=.08+.025*i
 A=np.array([[-a,b],[-b,-c]])
 xs=rng.uniform(-1,1,(2000,2))
 vdot=np.einsum("ni,ij,nj->n",xs,A+A.T,xs)
 for j,m in enumerate(motifs):
  if j==0: ok=bool(np.max(vdot)<=1e-12)
  elif j==1:
   C=np.array([[1.,0.]])
   ok=bool(np.linalg.matrix_rank(np.vstack((C,C@A)))==2)
  elif j==2: ok=bool(np.max(np.abs((A+A.T)-np.diag(np.diag(A+A.T))))<1e-12)
  elif j==3:
   A2=np.array([[-a*.7,b*.8],[-b*.8,-c*.7]])
   ok=bool(max(np.linalg.eigvalsh(A+A.T).max(),np.linalg.eigvalsh(A2+A2.T).max())<0)
  elif j==4: ok=bool(-np.linalg.eigvals(A).real.max()>0) # NOT a delay certificate
  elif j==5: ok=bool(min(a,c)>0)
  elif j==6: ok=bool(np.linalg.eigvalsh(-(A+A.T)).min()>0)
  elif j in (7,8): ok=None # No rare event or actuator model
  else: ok=bool(max(a,c)/min(a,c)>=3) # Illustrative ratio only
  rows.append({"id":f"INV-{i*10+j+1:03d}","domain":domain,"motif":m,
               "toy_status":"NOT_TESTABLE" if ok is None else "PASS_TOY" if ok else "FAIL_TOY",
               "scientific_status":"UNTESTED","novelty":"UNKNOWN"})
with open("inv_disc_100_screen_results.csv","w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
from collections import Counter
print(Counter(r["toy_status"] for r in rows))
