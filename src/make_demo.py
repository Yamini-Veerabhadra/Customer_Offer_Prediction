"""Reproducible synthetic smoke-test data. NOT the UCI bank dataset."""
import numpy as np
import pandas as pd
from pathlib import Path

def generate(n=900,seed=42):
    r=np.random.default_rng(seed)
    prev=r.poisson(.6,n); rate=r.uniform(.5,5,n)
    jobs=r.choice(['admin.','student','technician','retired','blue-collar','services'],n)
    outcome=np.where(prev>0,r.choice(['failure','success','nonexistent'],n,p=[.5,.2,.3]),'nonexistent')
    logits=-2.5+1.4*(outcome=='success')+.5*(jobs=='retired')-.24*rate+.15*prev
    response=np.where(r.random(n)<1/(1+np.exp(-logits)),'yes','no')
    return pd.DataFrame({'age':r.integers(18,81,n),'job':jobs,'marital':r.choice(['married','single','divorced'],n),
        'education':r.choice(['high.school','university.degree','basic.9y'],n),'default':r.choice(['no','unknown'],n),
        'housing':r.choice(['yes','no'],n),'loan':r.choice(['yes','no'],n),
        'contact':r.choice(['cellular','telephone'],n),'month':r.choice(['may','jun','jul','aug'],n),
        'day_of_week':r.choice(['mon','tue','wed','thu','fri'],n),'campaign':r.integers(1,8,n),
        'duration':r.integers(20,700,n),'pdays':np.where(prev==0,999,r.integers(1,28,n)),
        'previous':prev,'poutcome':outcome,
        'emp.var.rate':r.uniform(-3,1.4,n).round(2),'cons.price.idx':r.uniform(92,95,n).round(2),
        'cons.conf.idx':r.uniform(-50,-27,n).round(2),'euribor3m':rate.round(3),
        'nr.employed':r.uniform(4960,5230,n).round(1),'y':response})

if __name__=='__main__':
    p=Path(__file__).resolve().parents[1]/'data/demo/synthetic_campaign_demo.csv'
    p.parent.mkdir(parents=True,exist_ok=True)
    generate().to_csv(p,sep=';',index=False)
    print('Created synthetic demo:',p)
