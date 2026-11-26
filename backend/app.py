from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Early Disease Prediction API is running!"

@app.route('/predict/diabetes', methods=['POST'])
def predict_diabetes():
    data = request.json
    # Dummy prediction for testing
    return jsonify({"disease": "Diabetes", "risk_level": "Medium", "score": 65})

if __name__ == '__main__':
    app.run(debug=True)
