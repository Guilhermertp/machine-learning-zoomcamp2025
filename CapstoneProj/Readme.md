---

# 🚦 Traffic Volume Prediction Flask App

![Python](https://img.shields.io/badge/python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green)
![Docker](https://img.shields.io/badge/Docker-yes-blue)
[![Dataset](https://img.shields.io/badge/dataset-Kaggle-orange)](https://www.kaggle.com/datasets/anshtanwar/metro-interstate-traffic-volume)

## **Project Overview**

### **Objective**

The goal of this project is to **predict traffic volume** on westbound I-94, a major interstate highway connecting Minneapolis and St. Paul, Minnesota. By forecasting traffic patterns, city planners and transportation agencies can:

* Improve traffic management and reduce congestion.
* Optimize transportation infrastructure.
* Enable predictive planning for events and roadworks.

### **Problem Statement**

Traffic congestion and unexpected surges in volume are common challenges in urban transportation systems. Accurate predictions help:

* Minimize delays and congestion.
* Reduce environmental impact from idling vehicles.
* Enhance commuter experience with proactive traffic management.

This project leverages **predictive modeling** to estimate traffic volume based on weather conditions, temporal factors, and holidays.

---

## **Project Architectural Diagram**

The architecture of the app includes:

1. **Data Input** – User provides weather, temporal, and holiday information.
2. **Preprocessing** – Data is cleaned, encoded, and scaled for model input.
3. **Predictive Model** – Any chosen regression or machine learning model can be used (e.g., Random Forest, XGBoost, LightGBM).
4. **Output** – Predicted traffic volume returned via a web form or JSON API.

![Project Architecture](assets/architecture.png)

---

## **Dataset**

The dataset contains **hourly traffic volume observations** collected by the Minnesota Department of Transportation (MnDOT) from 2012 to 2018, at a station midway between Minneapolis and St. Paul.

### Sources:

* **Kaggle:** [Metro Interstate Traffic Volume](https://www.kaggle.com/datasets/anshtanwar/metro-interstate-traffic-volume)
* **Direct from Repo:** [Metro_Interstate_Traffic_Volume.csv](https://raw.githubusercontent.com/Guilhermertp/machine-learning-zoomcamp2025/refs/heads/main/CapstoneProj/Metro_Interstate_Traffic_Volume.csv)

---

## **Dataset Structure**

| **Feature**      | **Description**                        |
| ---------------- | -------------------------------------- |
| `temp`           | Temperature (Kelvin)                   |
| `rain_1h`        | Rainfall in last hour (mm)             |
| `snow_1h`        | Snowfall in last hour (cm)             |
| `clouds_all`     | Cloud cover (%)                        |
| `holiday`        | Indicator if the day is a holiday      |
| `year`           | Year of observation                    |
| `month`          | Month of observation                   |
| `hour`           | Hour of observation                    |
| `traffic_volume` | Target variable: hourly traffic volume |

> The data captures **temporal patterns, weather effects, and holiday influences** on traffic volume.

---

## **Exploratory Data Analysis**

* Hourly traffic patterns: Peaks during morning and evening rush hours.
* Weather influence: Rain and snow slightly reduce traffic volumes.
* Holiday effect: Traffic volume is lower during public holidays.

Visualization examples can be added in `assets/`.

---

## **Modeling and Evaluation**

### **Potential Models**

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting (XGBoost / LightGBM)

### **Evaluation Metrics**

For traffic volume prediction, the following regression metrics are used:

- **Mean Absolute Error (MAE)** – Average absolute difference between predicted and actual traffic volume.  
- **Mean Squared Error (MSE)** – Penalizes larger errors more heavily.  
- **Root Mean Squared Error (RMSE)** – Square root of MSE; more interpretable in original units.  
- **R² Score** – Proportion of variance explained by the model (1.0 is perfect).

---

### **Why These Evaluation Metrics?**

Traffic volume prediction is a **regression problem**, meaning the goal is to estimate a continuous value (vehicles per hour).  
For this reason, regression metrics are the most appropriate:

- **MAE (Mean Absolute Error)** – Measures the average prediction error in real units (vehicles/hour). Helpful for understanding how far off predictions are in practical terms.
- **MSE (Mean Squared Error)** – Penalizes large errors more strongly, which is important because big mistakes during peak hours or weather events are more costly.
- **RMSE (Root Mean Squared Error)** – Same units as the target variable, making results easy to interpret while still emphasizing large errors.
- **R² Score** – Shows how much of the natural variation in traffic volume the model can explain. Useful for comparing models and detecting underfitting.

Together, these metrics provide a complete understanding of model performance by balancing error magnitude, sensitivity to large mistakes, and overall predictive power.

---

### **Model Performance Comparison**

| **Model**                | **MAE** | **MSE** | **RMSE** | **R² Score** |
|--------------------------|---------|---------|----------|--------------|
| Linear Regression        | —       | —       | —        | —            |
| Decision Tree Regressor  | —       | —       | —        | —            |
| Random Forest Regressor  | —       | —       | —        | —            |
| XGBoost Regressor        | —       | —       | —        | —            |

---

## **App Features**

* Predict traffic volume using any trained model.
* Minimal HTML form interface for quick predictions.
* JSON endpoint for programmatic access.
* Dockerized for seamless deployment.

---

## **Prerequisites**

* **Python 3.13**
* Python packages:

```bash
pip install Flask==3.1.2 pandas==2.3.1 numpy==2.3.1 scikit-learn==1.7.0 joblib
```

* Optional: `lightgbm==4.6.0` for gradient boosting models
* Docker (optional)

---

## **Project Structure**

```
project_folder/
│
├─ predict.py              # Flask application
├─ model.pkl               # Placeholder for trained model
│
├─ assets/                 # Demo GIFs, architecture diagrams
│  ├─ demo-form.gif
│  ├─ demo-result.gif
│  └─ architecture.png
│
└─ templates/
   └─ index.html           # Web form
```

---

## **Getting the Dataset**

### Option 1: Direct Download

```bash
wget https://raw.githubusercontent.com/Guilhermertp/machine-learning-zoomcamp2025/refs/heads/main/CapstoneProj/Metro_Interstate_Traffic_Volume.csv -O Metro_Interstate_Traffic_Volume.csv
```

### Option 2: Kaggle API

```bash
pip install kaggle
kaggle datasets download -d anshtanwar/metro-interstate-traffic-volume -p ./data --unzip
```

---

## **Quick Start**

### 1️⃣ Test via Browser

```bash
python predict.py
```

Open: [http://127.0.0.1:9696/](http://127.0.0.1:9696/)

Sample input JSON:

```json
{
  "temp": 298.15,
  "rain_1h": 0,
  "snow_1h": 0,
  "clouds_all": 75,
  "holiday": 0,
  "year": 2018,
  "month": 6,
  "hour": 14
}
```

---

### 2️⃣ Docker Build

```bash
docker build -t traffic-volume-api .
```

---

### 3️⃣ Docker Run

```bash
docker run -p 9696:9696 traffic-volume-api
```

---

### 4️⃣ Test via JSON API

```bash
curl -X POST http://localhost:9696/predict \
-H "Content-Type: application/json" \
-d "{\"temp\":298.15,\"rain_1h\":0,\"snow_1h\":0,\"clouds_all\":75,\"holiday\":0,\"year\":2018,\"month\":6,\"hour\":14}"
```

---

## **Demo GIFs**

### 1️⃣ Web Form Submission

![Form Submission](assets/demo-form.gif)

### 2️⃣ Prediction Result

![Prediction Result](assets/demo-result.gif)

---

## **Deployment to Cloud**

This project can be deployed for free using **Streamlit Cloud**, which hosts both the model and the user interface directly from your GitHub repository.

### **Why Streamlit Cloud?**
- 100% free for personal projects  
- Zero-configuration deployment  
- Automatic redeploy on every GitHub commit  
- Built-in support for Python, ML models, and interactive UI elements  

### **How Deployment Works**
Your backend model and prediction logic will run inside a Streamlit app.  
The React frontend shown in this repository is optional — Streamlit can render interactive sliders, inputs, charts, and model outputs natively.  

If you prefer to use the React interface you developed, it can still be hosted separately (e.g., Vercel or Netlify) while the API remains on Streamlit or FastAPI.

### **Deploying to Streamlit Cloud**
1. Push your project to GitHub.  
2. Go to **https://streamlit.io/cloud**.  
3. Click **Deploy an app**.  
4. Select your GitHub repository and branch.  
5. Set the entry file, e.g.: app.py

6. Add required Python packages to `requirements.txt`.

Streamlit Cloud automatically builds and launches your app.

### **Frontend (Optional React UI)**
The repository includes a React-based frontend (`TrafficPredictor`) that allows users to:
- Adjust weather & time features  
- Send input to the backend predictor  
- Visualize the predicted traffic volume  
- Display model insights (MAE, R², SHAP importance)  

If using this frontend:
- Deploy it to **Vercel** or **Netlify**  
- Set the backend URL to your cloud API instead of `localhost:8000`

Example:
```js
const res = await fetch("https://your-streamlit-or-fastapi-url/predict", {...});
```
---

## **Conclusion**

This project provides a template for predicting hourly traffic volume using any regression model. By incorporating temporal, weather, and holiday features, the app can aid city planners, traffic managers, and commuters in better understanding and anticipating traffic patterns.

---

## **License**

MIT License
Author: **Guilherme Pereira**
Project: **Traffic Volume Prediction APP**

---
