#!/usr/bin/env python3
"""Noise-aware output-error thermal RC benchmark; synthetic research only."""
import argparse, json
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
from garden_candidate026_harness import trajectory, TRAIN, TEST, DT

def simulate(u, p, order):
    # Parameters positive, initial temperatures unrestricted; zero-order-held forcing.
    if order == 1:
        C,g=np.exp(p[:2]); x=p[2]; a=np.exp(-g/C*DT); b=-np.expm1(-g/C*DT)/g
        y=np.empty(len(u))
        for t,ut in enumerate(u):
            y[t]=x;x=a*x+b*ut
        return y
    C1,C2,h,g=np.exp(p[:4]); x=np.array(p[4:6],float)
    A=np.array([[-(g+h)/C1,h/C1],[h/C2,-h/C2]])
    B=np.array([[1/C1],[0.]])
    M=np.zeros((3,3));M[:2,:2]=A;M[:2,2:]=B
    E=expm(M*DT);ad=E[:2,:2];bd=E[:2,2]
    y=np.empty(len(u))
    for t,ut in enumerate(u):
        y[t]=x[0];x=ad@x+bd*ut
    return y

def fit(y,u,order):
    starts=([np.log(2),np.log(.35),float(y[0])],) if order==1 else ([np.log(2),np.log(4),np.log(.9),np.log(.24),float(y[0]),float(y[0])],)
    best=None
    for start in starts:
        start=np.array(start)
        nphys=2 if order==1 else 4
        lo=np.r_[np.full(nphys,-5.),np.full(order,-20.)]
        hi=np.r_[np.full(nphys,5.),np.full(order,20.)]
        result=least_squares(lambda p:simulate(u[:TRAIN],p,order)-y[:TRAIN],start,bounds=(lo,hi),max_nfev=250,ftol=1e-8,xtol=1e-8,gtol=1e-8)
        sse=float(np.sum(result.fun**2))
        if best is None or sse<best[0]:best=(sse,result.x,result.success)
    sse,p,success=best
    full=simulate(u,p,order)
    test_mse=float(np.mean((full[TRAIN:TRAIN+TEST]-y[TRAIN:TRAIN+TEST])**2))
    bic=TRAIN*np.log(max(sse/TRAIN,1e-15))+len(p)*np.log(TRAIN)
    return dict(bic=float(bic),test_mse=test_mse,fit_success=bool(success),params=p.tolist())

def run(n,noise,seed_start):
    out={'settings':{'n_per_class':n,'noise_sd':noise,'seed_start':seed_start,'selection_rule':'training BIC improvement >=10; output-error model, holdout reported independently','scope':'synthetic, structure-aware comparator; not blind discovery'}}
    for label,two in [('null_one_body',False),('hidden_two_body',True)]:
        cases=[]
        for k in range(n):
            y,u=trajectory(seed_start+k+(100000 if two else 0),two,sigma=noise)
            a=fit(y,u,1);b=fit(y,u,2)
            cases.append({'seed':k,'selected_two_body':b['bic']<=a['bic']-10,'delta_bic':b['bic']-a['bic'],'one_body_test_mse':a['test_mse'],'two_body_test_mse':b['test_mse'],'fit_success':a['fit_success'] and b['fit_success']})
        out[label]={'n':n,'selected':sum(c['selected_two_body'] for c in cases),'selection_rate':float(np.mean([c['selected_two_body'] for c in cases])),'median_one_body_test_mse':float(np.median([c['one_body_test_mse'] for c in cases])),'median_two_body_test_mse':float(np.median([c['two_body_test_mse'] for c in cases])),'cases':cases}
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=20);ap.add_argument('--noise',type=float,default=.012);ap.add_argument('--seed',type=int,default=9100);ap.add_argument('--output',default='garden_candidate026_strong_results.json');a=ap.parse_args()
    r=run(a.n,a.noise,a.seed)
    with open(a.output,'w') as f:json.dump(r,f,indent=2)
    print({k:(r[k]['selected'],r[k]['n']) for k in ['null_one_body','hidden_two_body']})