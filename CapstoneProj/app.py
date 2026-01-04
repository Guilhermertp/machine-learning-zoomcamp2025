from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
import os

app = Flask(__name__)  # <-- app is defined here

# Load model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model_xgb.pkl")
model = joblib.load(model_path)

# -----------------------------
# TEST ROUTE
# -----------------------------
@app.route("/test")
def test():
    return "Flask is working!"

# Your existing routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    print("Data received:", data)
    try:
        features = np.array([float(v) for v in data.values()]).reshape(1, -1)
        y_pred = model.predict(features)[0]
        return jsonify({"prediction": float(y_pred)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=9696)
