import pandas as pd
import joblib
from utils.preprocessing import  processdata

def predict_actions(input_file, output_file):
    df = pd.read_csv(input_file)
    
    df =  processdata(df)
    
    model = joblib.load('models/action_model.joblib')
    
    X = df[['temp', 'sis', 'hygro', 'anem1', 'anem2']]
    df['action'] = model.predict(X)
    
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    predict_actions('data/captor_3_todo.csv', 'data/correctedforest.csv')