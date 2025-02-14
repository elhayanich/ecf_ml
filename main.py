from fastapi import FastAPI
from pydantic import BaseModel
import json
import pandas as pd
import joblib

app = FastAPI()

class InputData(BaseModel):
    temp: float
    sis: float
    hygro: float | None
    anem1: float
    anem2: float


def correct_data(input_dict):
    with open('models/process.json', 'r') as f:
        params = json.load(f)
    
    df = pd.DataFrame([input_dict])
    
    numerical_cols = ['temp', 'sis', 'hygro', 'anem1', 'anem2']
    for col in numerical_cols:
        if pd.isna(df[col].iloc[0]):
            df[col] = params[col]['median']
        df[col] = df[col].clip(
            lower=params[col]['lower_bound'],
            upper=params[col]['upper_bound']
        )
    
    model = joblib.load('models/action_model.joblib')
    X = df[numerical_cols]
    action = model.predict(X)[0]
    
    corrected = input_dict.copy()
    for col in numerical_cols:
        corrected[col] = df[col].iloc[0]
    corrected['action'] = action
    
    return corrected


@app.post("/correct")
def correct(input_data: InputData):
    corrected_data = correct_data(input_data.dict())
    return corrected_data
