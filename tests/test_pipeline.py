import pytest
from src.make_demo import generate
from src.project import load,run,FEATURES
from api.main import health

def test_read(tmp_path):
    p=tmp_path/'synthetic.csv'
    generate(900).to_csv(p,sep=';',index=False)
    assert len(load(p))==900
    assert 'duration' not in FEATURES

def test_complete_pipeline(tmp_path):
    p=tmp_path/'synthetic.csv';out=tmp_path/'out'
    generate().to_csv(p,sep=';',index=False)
    result=run(p,out)
    assert result['chosen_model'] in ('logistic_regression','random_forest')
    assert (out/'model.joblib').exists()
    assert (out/'powerbi_campaign_contacts.csv').exists()

def test_missing_data(tmp_path):
    with pytest.raises(FileNotFoundError):load(tmp_path/'missing.csv')
