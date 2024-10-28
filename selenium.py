from flask import Flask, request, jsonify
import Prediction_Script  # assuming your prediction logic is in this file

app = Flask(__name__)

@app.route('/')
def home():
    return "market recommendation API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Call your prediction script's function here
    prediction = Prediction_Script.predict(data['features'])
    return jsonify({'recommendation': prediction})

if __name__ == '__main__':
    app.run(debug=True)
