# 🌊 Tsunami Prediction Flask App

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.0-green) ![Docker](https://img.shields.io/badge/docker-yes-blue)  

A **Flask web application** for predicting tsunamis using a **LightGBM** model. Interact via a web form or JSON API. Docker support included for easy deployment.

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Project Structure](#project-structure)  
- [Quick Start](#quick-start)  
  - [1️⃣ Test via Browser](#1️⃣-test-via-browser)  
  - [2️⃣ Docker Build](#2️⃣-docker-build)  
  - [3️⃣ Docker Run](#3️⃣-docker-run)  
  - [4️⃣ Test via JSON API](#4️⃣-test-via-json-api)  
- [Demo GIFs](#demo-gifs)  
- [License](#license)  

---

## Features

- Predict tsunami occurrence and probability based on earthquake data.  
- Minimal web form interface for quick testing.  
- API endpoint for JSON-based predictions.  
- Dockerized for portability and easy deployment.  

---

## Prerequisites

- Python 3.8+  
- Required Python packages:
```bash
pip install Flask numpy pandas joblib lightgbm
Docker (optional, for containerized deployment)

Project Structure
project_folder/
│
├─ predict.py           # Flask application
├─ lgbm_model.pkl       # Pre-trained LightGBM model
└─ templates/
   └─ index.html        # HTML form for input

Quick Start
1️⃣ Test via Browser
Ensure index.html exists in templates/.
Run the Flask app:
python predict.py
Open http://127.0.0.1:9696/
Fill in the form with sample values and click Predict:
{
  "magnitude":7.0,"cdi":8,"mmi":7,"sig":768,"nst":117,
  "dmin":0.509,"gap":17.0,"depth":14.0,"latitude":-9.7963,
  "longitude":159.596,"Year":2022,"Month":11
}

Minimal index.html Example
<!DOCTYPE html>
<html>
<head>
    <title>Tsunami Prediction</title>
</head>
<body>
    <h1>Tsunami Prediction Form</h1>
    <form action="/predict" method="post">
        <label>Magnitude: <input type="text" name="magnitude"></label><br>
        <label>CDI: <input type="text" name="cdi"></label><br>
        <label>MMI: <input type="text" name="mmi"></label><br>
        <label>SIG: <input type="text" name="sig"></label><br>
        <label>NST: <input type="text" name="nst"></label><br>
        <label>Dmin: <input type="text" name="dmin"></label><br>
        <label>Gap: <input type="text" name="gap"></label><br>
        <label>Depth: <input type="text" name="depth"></label><br>
        <label>Latitude: <input type="text" name="latitude"></label><br>
        <label>Longitude: <input type="text" name="longitude"></label><br>
        <label>Year: <input type="text" name="Year"></label><br>
        <label>Month: <input type="text" name="Month"></label><br>
        <input type="submit" value="Predict">
    </form>

    {% if prediction %}
        <h2>Prediction Result:</h2>
        <p>Predicted Tsunami: 
            {% if prediction.prediction == 1 %} Tsunami {% else %} No Tsunami {% endif %}
        </p>
        <p>Probability: {{ prediction.probability }}</p>
    {% endif %}
</body>
</html>

2️⃣ Docker Build
docker build -t lightgbm-api .
Packages Python, dependencies, the model, and Flask app into a portable container.

3️⃣ Docker Run
docker run -p 9696:9696 lightgbm-api
Maps container port 9696 to host port 9696.
Access the app at http://127.0.0.1:9696/

4️⃣ Test via JSON API
curl -X POST http://127.0.0.1:9696/predict \
     -H "Content-Type: application/json" \
     -d '{"magnitude":7.0,"cdi":8,"mmi":7,"sig":768,"nst":117,"dmin":0.509,"gap":17.0,"depth":14.0,"latitude":-9.7963,"longitude":159.596,"Year":2022,"Month":11}'
Returns JSON with prediction and probability.

Demo GIFs
1️⃣ Web Form Submission

2️⃣ Prediction Result

3️⃣ Dockerized App Running

Replace the GIFs in assets/ with your recorded demos.

License
MIT License
Author: Your Name | Project: Tsunami Prediction API
