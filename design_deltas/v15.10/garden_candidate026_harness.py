#!/usr/bin/env python3
"""Reproducible candidate-026 synthetic closure experiment; no empirical/novelty claim."""
import json
import numpy as np
from scipy.linalg import expm

DT=0.25
TRAIN=320
TEST=160

def trajectory(seed, two_body, sigma=0.012):
    rng=np.random.default_rng(seed)
    n=TRAIN+TEST+2
    u=np.zeros(n)
    for t in range(n):
        u[t]=1.2*np.sin(0.073*t)+0.6*np.sin(0.019*t+0.7)+(0.8 if (t//29)%2 else -0.4)+0.2*rng.normal()
    if two_body:
        C1,C2,h,g=2.0,4.0,0.9,0.24
        # C1 dT1/dt = u - g*T1 - h*(T1-T2); C2 dT2/dt = h*(T1-T2)
        A=np.array([[-(g+h)/C1,h/C1],[h/C2,-h/C2]])
        B=np.array([[1/C1],[0.]])
        M=np.zeros((3,3));M[:2,:2]=A;M[:2,2:]=B
        E=expm(M*DT);Ad=E[:2,:2];Bd=E[:2,2]
        x=np.array([0.1,-0.6]); y=[]
        for k in range(n):
            y.append(x[0]);x=Ad@x+Bd*u[k]
    else:
        C,g=2.0,0.35
        a=np.exp(-g/C*DT);b=(1-a)/g
        x=0.1;y=[]
        for k in range(n):
            y.append(x);x=a*x+b*u[k]
    return np.asarray(y)+sigma*rng.normal(size=n),u

def matrices(y,u,p):
    # ARX(p,p) uses current and p-1 previous y and u to predict next sample
    X=[];z=[];ts=[]
    for t in range(p-1,len(y)-1):
        X.append([*([y[t-j] for j in range(p)]),*([u[t-j] for j in range(p)]),1.])
        z.append(y[t+1]);ts.append(t)
    return np.array(X),np.array(z),np.array(ts)

def evaluate(y,u,p):
    X,z,t=matrices(y,u,p)
    tr=t<TRAIN-1;te=t>=TRAIN
    # Fixed ridge is part of the preregistered model, not tuned on test.
    lam=1e-5
    L=np.eye(X.shape[1]);L[-1,-1]=0
    beta=np.linalg.solve(X[tr].T@X[tr]+lam*L,X[tr].T@z[tr])
    pred=X@beta
    train_mse=np.mean((z[tr]-pred[tr])**2)
    test_mse=np.mean((z[te]-pred[te])**2)
    # Training BIC with parameter penalty
    bic=tr.sum()*np.log(max(train_mse,1e-15))+X.shape[1]*np.log(tr.sum())
    return dict(train_mse=float(train_mse),test_mse=float(test_mse),bic=float(bic),coefficients=beta.tolist())

def run():
    # Calibrate the threshold on independent one-body null simulations; measurement noise can make ARX2 look better even when no hidden physical state exists.
    null_calibration=[]
    for seed in range(100):
        yc,uc=trajectory(seed+5000,False)
        bc=evaluate(yc,uc,1);ec=evaluate(yc,uc,2)
        null_calibration.append(1-ec['test_mse']/bc['test_mse'])
    null_threshold=float(np.quantile(null_calibration,0.95))
    allout={}
    for label,two in [('null_one_body',False),('hidden_two_body',True)]:
        entries=[]
        for seed in range(100):
            y,u=trajectory(seed+1000,two)
            b=evaluate(y,u,1);e=evaluate(y,u,2)
            improvement=1-e['test_mse']/b['test_mse']
            # require >= 10% test improvement AND BIC improvement of at least 10
            selected=improvement>null_threshold and e['bic']<=b['bic']-10
            entries.append({'seed':seed,'baseline_test_mse':b['test_mse'],'extension_test_mse':e['test_mse'],'fractional_improvement':improvement,'selected':selected,'delta_bic':e['bic']-b['bic']})
        allout[label]={'n':len(entries),'selection_rate':sum(x['selected'] for x in entries)/len(entries),'median_test_improvement':float(np.median([x['fractional_improvement'] for x in entries])),'median_baseline_mse':float(np.median([x['baseline_test_mse'] for x in entries])),'median_extension_mse':float(np.median([x['extension_test_mse'] for x in entries])),'cases':entries}
    allout['design']={'null_calibration_quantile':0.95,'null_calibration_threshold':null_threshold,'calibration_seeds':100,'dt':DT,'train_steps':TRAIN,'test_steps':TEST,'noise_sd':0.012,'seeds_per_condition':100,'comparison':'ARX(1,1) vs ARX(2,2) with equal train/test sequences','selection_rule':'heldout MSE improvement above independent null 95th percentile AND training BIC decreases by >=10','scope':'synthetic only; comparator is not strongest modern system identification; no novelty claim'}
    return allout
if __name__=='__main__':
    r=run()
    with open('/mnt/data/garden_candidate026_harness_results.json','w') as f:json.dump(r,f,indent=2)
    print('calibrated_null_threshold=',round(r['design']['null_calibration_threshold'],4))
    for key in ['null_one_body','hidden_two_body']:
        a=r[key];print(key,'n=',a['n'],'selection=',a['selection_rate'],'median_gain=',round(a['median_test_improvement'],4),'baseline_mse=',round(a['median_baseline_mse'],7),'extended_mse=',round(a['median_extension_mse'],7))