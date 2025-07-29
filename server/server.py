#server.py
from flask import Flask, request, jsonify
import util
util.load_saved_artifacts()

app = Flask(__name__)

# Endpoint to get location names
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({'locations': util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Endpoint to predict home price
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])      # ✅ Cast to int
    bath = int(request.form['bath'])    # ✅ Cast to int

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response  # ✅ return the response object here

# Main entry point
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction.....")
    app.run()
