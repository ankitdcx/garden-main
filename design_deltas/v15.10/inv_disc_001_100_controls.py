"""INV-DISC-001: reproducible analytic positive-control suite.
Run: python3 inv_disc_001_100_controls.py
Requires: sympy. This is NOT a Garden search or SOS/SMT benchmark.
"""
import json
import sympy as s
x,y=s.symbols("x y",real=True)
records=[]
for k in range(100):
    a=s.Rational(2+k%7,3)
    c=s.Rational(3+(k//7)%9,3)
    b=s.Rational((k*7)%17-8,12)
    A=s.Rational(2+k%5,3)
    B=s.Rational(2+(k//5)%5,4)
    h=(x/A)**2+(y/B)**2-1
    fx=-a*x+b*y*y
    fy=-c*y
    lie=s.expand(s.diff(h,x)*fx+s.diff(h,y)*fy)
    margin=s.simplify(c-abs(b)*B*B/A)
    # On h=0, let u=x/A and v=y/B, u^2+v^2=1.
    # Lie(h)=-2*a*u^2-2*c*v^2+2*b*(B^2/A)*u*v^2
    # <= -2*a*u^2-2*(c-|b|*B^2/A)*v^2.
    # Therefore a>0 and margin>0 suffice for forward invariance.
    certified=bool(a>0 and margin>0)
    records.append({"id":f"CTRL-{k+1:03}","a":str(a),"b":str(b),
      "c":str(c),"A":str(A),"B":str(B),"lie":str(lie),
      "margin":str(margin),"sufficient_certificate":certified})
out={"method":"symbolic analytic sufficient condition (not SOS/SMT, not Garden)",
     "family":"xdot=-a*x+b*y^2, ydot=-c*y; ellipse x^2/A^2+y^2/B^2<=1",
     "count":len(records),"certified":sum(r["sufficient_certificate"] for r in records),
     "inconclusive":sum(not r["sufficient_certificate"] for r in records),
     "records":records}
with open("inv_disc_001_100_controls_results.json","w") as f: json.dump(out,f,indent=2)
print("count",out["count"],"certified",out["certified"],"inconclusive",out["inconclusive"])
