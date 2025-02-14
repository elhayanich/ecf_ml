import pandas as pd
from utils.preprocessing import dfprocess
from utils.models import train_model


df = pd.read_csv('data/captor_1_sample_2_with_manual_validation.csv')  #fichier original
# df = pd.read_csv('data/captor_1_sample_2_cleaned.csv') #fichier test iqr 


dfprocess(df)


X = df[['temp', 'sis', 'hygro', 'anem1', 'anem2']]
y = df['action_valide']
train_model(X, y)