"""INV-DISC-001 preliminary control. No Garden search or SOS/SMT baseline."""
import json
from pathlib import Path
import sympy as sp
x,y=sp.symbols('x y',real=True)
rows=[]
for i in range(20):
    a=sp.Rational(2+(i%4),2)
    c=sp.Rational(2+((i*3)%5),2)
    b=sp.Rational((i%9)-4,5)
    f=-a*x+b*y*y
    g=-c*y
    derivative=sp.expand(2*x*f+2*y*g)
    # For x^2+y^2=1: |x*y^2| <= 2/(3*sqrt(3)).
    # Thus d(x^2+y^2-1)/dt <= -2*min(a,c)+4*abs(b)/(3*sqrt(3)).
    upper=-2*min(a,c)+4*abs(b)/(3*sp.sqrt(3))
    certified=bool(sp.simplify(upper<0))
    rows.append(dict(case_id=f'INV-{i+1:02}',a=str(a),b=str(b),c=str(c),derivative=str(derivative),boundary_upper_bound=str(upper),certified_by_sufficient_bound=certified))
result={'test':'INV-DISC-001 preliminary control','method':'symbolic sufficient-bound check, NOT SOS/SMT, NOT Garden comparison','safe_set':'x^2+y^2<=1','family':'dx/dt=-a*x+b*y^2; dy/dt=-c*y','cases':rows}
Path('INV_DISC_001_preliminary_receipts.json').write_text(json.dumps(result,indent=2))
print(f'Certified {sum(r["certified_by_sufficient_bound"] for r in rows)}/{len(rows)}')
