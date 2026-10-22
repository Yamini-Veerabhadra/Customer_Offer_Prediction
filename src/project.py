"""Customer offer prediction: reproducible UCI Bank Marketing analysis."""
from pathlib import Path
import argparse, json
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import roc_auc_score, average_precision_score, precision_score, recall_score, f1_score, brier_score_loss
import joblib

ROOT = Path(__file__).resolve().parents[1]
NUM = ['age','pdays','previous','emp.var.rate','cons.price.idx','cons.conf.idx','euribor3m','nr.employed']
CAT = ['job','marital','education','default','housing','loan','poutcome']
FEATURES = NUM + CAT
REQUIRED = FEATURES + ['duration','campaign','contact','month','day_of_week','y']

def load(path):
    p = Path(path)
    if not p.exists(): raise FileNotFoundError(f'Missing CSV: {p}. See README.md for UCI download.')
    df = pd.read_csv(p, sep=';')
    absent = set(REQUIRED) - set(df)
    if absent: raise ValueError(f'Expected bank-additional-full.csv; missing columns: {sorted(absent)}')
    if not df.y.isin(['yes','no']).all(): raise ValueError('Expected yes/no target')
    for c in NUM:
        df[c] = pd.to_numeric(df[c], errors='raise')
    return df

def preprocessing():
    return ColumnTransformer([
        ('numeric', Pipeline([('fill',SimpleImputer(strategy='median')),('scale',StandardScaler())]),NUM),
        ('categorical',Pipeline([('fill',SimpleImputer(strategy='most_frequent')),('onehot',OneHotEncoder(handle_unknown='ignore'))]),CAT),
    ])

def metrics(y,p):
    pred = (p >= 0.5).astype(int)
    return {k:round(float(v),4) for k,v in {
        'roc_auc':roc_auc_score(y,p),'pr_auc':average_precision_score(y,p),
        'precision':precision_score(y,pred,zero_division=0),'recall':recall_score(y,pred,zero_division=0),
        'f1':f1_score(y,pred,zero_division=0),'brier':brier_score_loss(y,p)}.items()}

def run(data, output):
    df=load(data); out=Path(output); out.mkdir(parents=True,exist_ok=True)
    if len(df)<200: raise ValueError('Provide at least 200 records')
    profile={'rows':len(df),'subscriptions':int((df.y=='yes').sum()),'response_rate':round(float((df.y=='yes').mean()),5),'duplicated_contact_rows':int(df.duplicated().sum()),'unknown_values':int((df.astype(str)=='unknown').sum().sum())}
    (out/'profile.json').write_text(json.dumps(profile,indent=2))
    business=df.copy();business['subscribed']=(business.y=='yes').astype(int)
    business.insert(0,'contact_record_id',np.arange(1,len(df)+1))
    business.to_csv(out/'powerbi_campaign_contacts.csv',index=False)
    for name,cols in {'job':['job'],'education':['education'],'month':['month'],'prior_campaign':['poutcome'],'channel':['contact']}.items():
        a=business.groupby(cols,dropna=False).agg(contacts=('subscribed','size'),subscriptions=('subscribed','sum'),response_rate=('subscribed','mean')).reset_index()
        a.to_csv(out/f'kpi_by_{name}.csv',index=False)
    # Temporal holdout: UCI full variant is described as ordered chronologically.
    i,j=int(.65*len(df)),int(.8*len(df))
    tr,va,te=df.iloc[:i],df.iloc[i:j],df.iloc[j:]
    ytr=(tr.y=='yes').astype(int);yva=(va.y=='yes').astype(int);yte=(te.y=='yes').astype(int)
    if any(x.nunique()<2 for x in (ytr,yva,yte)):
        raise ValueError('All chronological splits must contain yes and no targets.')
    models={'logistic_regression':LogisticRegression(max_iter=1000,class_weight='balanced',random_state=42),
            'random_forest':RandomForestClassifier(n_estimators=120,min_samples_leaf=10,n_jobs=-1,class_weight='balanced_subsample',random_state=42)}
    validation={}
    for name,est in models.items():
        p=Pipeline([('preprocess',preprocessing()),('model',est)])
        p.fit(tr[FEATURES],ytr)
        validation[name]=metrics(yva,p.predict_proba(va[FEATURES])[:,1])
    best=max(validation,key=lambda name:validation[name]['pr_auc'])
    model=Pipeline([('preprocess',preprocessing()),('model',models[best])])
    model.fit(df.iloc[:j][FEATURES],(df.iloc[:j].y=='yes').astype(int))
    pred=model.predict_proba(te[FEATURES])[:,1]
    test=metrics(yte,pred)
    joblib.dump(model,out/'model.joblib')
    predictions=te[['age','job','education','y']].copy()
    predictions['probability']=pred
    predictions.to_csv(out/'held_out_predictions.csv',index=False)
    # Exploratory campaign-history clusters, not unique customer segmentation.
    behavior=df[['pdays','previous']].copy()
    behavior['pdays']=behavior.pdays.replace(999,-1)
    labels=KMeans(n_clusters=3,n_init=10,random_state=42).fit_predict(StandardScaler().fit_transform(behavior))
    clusters=business[['subscribed']].copy();clusters['segment']=labels
    clusters.groupby('segment').agg(contacts=('subscribed','size'),subscriptions=('subscribed','sum'),response_rate=('subscribed','mean')).to_csv(out/'campaign_history_segments.csv')
    evaluation={'data_source':'synthetic demo' if 'synthetic' in str(data).lower() else 'supplied input: check source',
                'chosen_model':best,'validation_metrics':validation,'held_out_test_metrics':test,
                'chronological_split':{'train':len(tr),'validation':len(va),'test':len(te)},
                'predictor_columns':FEATURES,'excluded_contact_time_columns':['duration','campaign','contact','month','day_of_week'],
                'caveat':'Historical contact response prediction, not causal campaign uplift, credit approval, or unique customer scoring.'}
    (out/'evaluation.json').write_text(json.dumps(evaluation,indent=2))
    print(json.dumps({'rows':len(df),'chosen_model':best,'test_metrics':test,'output':str(out)},indent=2))
    return evaluation

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--data',default=str(ROOT/'data/raw/bank-additional-full.csv'))
    ap.add_argument('--output',default=str(ROOT/'outputs'))
    args=ap.parse_args();run(args.data,args.output)
