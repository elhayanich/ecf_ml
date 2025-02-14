import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from utils.models import train_model 

def evaluate_model():
    df = pd.read_csv('data/captor_1_sample_2_with_manual_validation.csv')
    
    X = df[['temp', 'sis', 'hygro', 'anem1', 'anem2']]
    y = df['action_valide']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    
    y_pred = model.predict(X_test)
    

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy :", accuracy)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

if __name__ == '__main__':
    evaluate_model()
