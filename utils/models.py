from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression
import joblib

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, 'models/action_model.joblib')
    return model

# def train_model(X_train, y_train):
#     model = LogisticRegression(random_state=42, max_iter=1000)
#     model.fit(X_train, y_train)
#     joblib.dump(model, 'models/action_model.joblib')
#     return model


