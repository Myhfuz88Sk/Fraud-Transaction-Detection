import joblib

def predict(model_path, X):
    model = joblib.load(model_path)
    return model.predict(X)
