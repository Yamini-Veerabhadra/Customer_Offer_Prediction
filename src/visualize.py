"""Create clearly labeled campaign visuals from pipeline outputs."""
from pathlib import Path
import argparse, json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from src.project import ROOT

def main(output):
    out=Path(output)
    metrics=json.loads((out/'evaluation.json').read_text())
    synthetic=metrics['data_source']=='synthetic demo'
    tag='SYNTHETIC DEMO — NOT REAL BANK DATA' if synthetic else 'Supplied bank dataset — verify source'
    fig,ax=plt.subplots(figsize=(9,4.5))
    data=pd.read_csv(out/'kpi_by_job.csv').sort_values('contacts',ascending=False)
    ax.bar(data['job'],data['contacts'])
    ax.set_title('Marketing contacts by job category\n'+tag)
    ax.set_ylabel('Contact records');ax.tick_params(axis='x',rotation=40)
    fig.tight_layout();fig.savefig(out/'contacts_by_job.png',dpi=160);plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,4.5))
    data=pd.read_csv(out/'kpi_by_prior_campaign.csv')
    ax.bar(data['poutcome'],data['response_rate']*100)
    ax.set_title('Term-deposit response rate by earlier campaign outcome\n'+tag)
    ax.set_ylabel('Response rate (%)')
    fig.tight_layout();fig.savefig(out/'response_by_previous_campaign.png',dpi=160);plt.close(fig)
    print('Saved chart previews under',out)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(ROOT/'outputs'));a=ap.parse_args();main(a.output)
