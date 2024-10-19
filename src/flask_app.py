from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open("../models/health_risk_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return "Health Risk Assessment API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    # Extract the data from the POST request
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    
    # Perform the prediction
    prediction = model.predict(df)
    
    # Return the result as JSON
    result = {'prediction': int(prediction[0])}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)