from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

model = joblib.load('models/fraud_detector.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        return jsonify({'fraud': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
