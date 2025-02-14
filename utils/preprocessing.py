import json
import pandas as pd

def dfprocess(df, save_path='models/process.json'):
    numerical_cols = ['temp', 'sis', 'hygro', 'anem1', 'anem2']
    params = {}
    for col in numerical_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        mean = df[col].mean()
        median = df[col].median()
        params[col] = {
            'mean': mean,
            'median': median,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound
        }
    with open(save_path, 'w') as f:
        json.dump(params, f)

def processdata(df, params_path='models/process.json'):
    with open(params_path, 'r') as f:
        params = json.load(f)
    numerical_cols = ['temp', 'sis', 'hygro', 'anem1', 'anem2']
    for col in numerical_cols:
        df[col] = df[col].fillna(params[col]['median'])
        df[col] = df[col].clip(lower=params[col]['lower_bound'], upper=params[col]['upper_bound'])
    return df