from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
import os
import pandas as pd

app = Flask(__name__)

# Locate model file inside the project folder
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "lgbm_model.pkl")  # model file name should be a string

print("Model directory:", current_dir)
print("Loading model from:", model_path)

# Load the LightGBM model
model = joblib.load(model_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Extract features from form (or JSON)
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    try:
        # Convert input values to numeric
        features = np.array([float(v) for v in data.values()]).reshape(1, -1)

        # Predict
        y_pred = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        result = {
            "prediction": int(y_pred),
            "probability": round(float(probability), 4)
        }

        # JSON response
        if request.is_json:
            return jsonify(result), 200
        else:
            return render_template("index.html", prediction=result)

    except Exception as e:
        return jsonify({"error": f"Error making prediction: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
