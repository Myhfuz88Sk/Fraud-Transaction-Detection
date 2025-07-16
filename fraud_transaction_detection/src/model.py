from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model(X, y, model_path="models/fraud_detector.pkl"):
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(clf, model_path)
    return clf
