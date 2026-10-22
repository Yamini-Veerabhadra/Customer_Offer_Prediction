"""Educational, read-only pre-contact prediction endpoint."""
from functools import lru_cache
from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.project import ROOT, FEATURES

app=FastAPI(title='Customer Offer Prediction API',version='1.0')

class Contact(BaseModel):
    age:int=Field(ge=18,le=110)
    job:str
    marital:str
    education:str
    default:str
    housing:str
    loan:str
    pdays:int=Field(ge=0)
    previous:int=Field(ge=0)
    poutcome:str
    emp_var_rate:float
    cons_price_idx:float
    cons_conf_idx:float
    euribor3m:float
    nr_employed:float

@lru_cache
def trained_model():
    path=ROOT/'outputs/model.joblib'
    if not path.is_file(): raise FileNotFoundError('Run python -m src.project first')
    return joblib.load(path) # only trust your own locally created model

@app.get('/health')
def health():
    return {'status':'ok','model_ready':(ROOT/'outputs/model.joblib').is_file()}

@app.post('/predict')
def predict(record:Contact):
    data=record.model_dump()
    for s,d in [('emp_var_rate','emp.var.rate'),('cons_price_idx','cons.price.idx'),('cons_conf_idx','cons.conf.idx'),('nr_employed','nr.employed')]:
        data[d]=data.pop(s)
    try:
        p=float(trained_model().predict_proba(pd.DataFrame([data])[FEATURES])[0,1])
    except FileNotFoundError as e: raise HTTPException(status_code=503,detail=str(e)) from e
    return {'estimated_response_probability':round(p,4),'prediction_at_0_5':'yes' if p>=.5 else 'no',
            'note':'Educational model; not a financial eligibility or credit decision.'}
