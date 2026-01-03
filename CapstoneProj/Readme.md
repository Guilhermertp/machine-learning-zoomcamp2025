---

# 🚦 Traffic Volume Prediction Flask App

![Python](https://img.shields.io/badge/python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green)
![Docker](https://img.shields.io/badge/Docker-yes-blue)
[![Dataset](https://img.shields.io/badge/dataset-Kaggle-orange)](https://www.kaggle.com/datasets/anshtanwar/metro-interstate-traffic-volume)
![pandas](https://img.shields.io/badge/pandas-2.3.1-blue)
![numpy](https://img.shields.io/badge/numpy-2.3.1-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.0-blue)
![joblib](https://img.shields.io/badge/joblib-1.3.2-blue)

---

## 📚 Table of Contents

* [Project Overview](#project-overview)

  * [Objective](#objective)
  * [Problem Statement](#problem-statement)
* [Project Architectural Diagram](#project-architectural-diagram)
* [Dataset](#dataset)

  * [Sources](#-sources)
* [Dataset Structure](#dataset-structure)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Modeling and Evaluation](#modeling-and-evaluation)

  * [Potential Models](#potential-models)
  * [Evaluation Metrics](#evaluation-metrics)
  * [Why These Evaluation Metrics](#why-these-evaluation-metrics)
  * [Model Performance Comparison](#model-performance-comparison)
* [App Features](#app-features)
* [Prerequisites](#prerequisites)
* [Project Structure](#project-structure)
* [Getting the Dataset](#getting-the-dataset)

  * [Option 1 Direct Download](#option-1-direct-download)
  * [Option 2 Kaggle API](#option-2-kaggle-api)
* [Quick Start](#quick-start)

  * [1 Test via Browser](#1-test-via-browser)
  * [2 Docker Build](#2-docker-build)
  * [3 Docker Run](#3-docker-run)
  * [4 Test via JSON API](#4-test-via-json-api)
* [Demo GIFs](#demo-gifs)

  * [1 Web Form Submission](#1-web-form-submission)
  * [2 Prediction Result](#2-prediction-result)

* [Conclusion](#conclusion)
* [License](#license)

---

## Project Overview

### Objective

The goal of this project is to **predict traffic volume** on westbound I-94, a major interstate highway connecting Minneapolis and St. Paul, Minnesota. Accurate traffic forecasting supports:

* Improved congestion management
* Better traffic planning
* More efficient infrastructure decisions
* Enhanced commuter experience

### Problem Statement

Urban roads face unpredictable congestion driven by weather, time of day, and special events.
This project uses **machine learning** to predict future traffic volume based on:

* Weather conditions
* Temporal features
* Holiday indicators

---

## Project Architectural Diagram

### Local Deployment Architecture

This setup runs the entire application (web server and ML model) on your local machine. It is typically used for development, testing, or personal use.

![Project Architecture](asset/architecture.png)

**Step-by-step flow:**

1. **User opens a web browser** (e.g., Chrome or Firefox) and navigates to `http://localhost:9696/` (a local address on the user's machine).

2. **Browser sends an HTTP GET request** to the Flask app running locally to load the main page (`index.html`).  
   - The Flask app serves the `index.html` file from its templates folder.

3. **User interacts with the web page** (e.g., fills in a form with input features) and submits it.

4. **Browser sends an HTTP POST request** to the `/predict` endpoint of the Flask app, including the input data (usually in JSON or form format).

5. **Flask app receives the POST request** at the `/predict` route.

6. **Flask app loads the trained machine learning model** from the file `model_xgb.pkl` (an XGBoost model saved using pickle or joblib).

7. **Flask app uses the loaded model** to make a prediction based on the input data received from the browser.

8. **Flask app creates a JSON response** containing the prediction (e.g., `{"prediction": value}`).

9. **Flask app sends the JSON response back** to the browser.

10. **Browser receives the JSON** and updates the webpage (using JavaScript) to display the prediction result to the user.

**Key characteristics:**  
- Everything runs on the local machine.  
- No internet required after initial setup.  
- Fast response times (no network latency).  
- Not accessible to others unless the machine is exposed to the network.

---

## Dataset

The dataset contains **hourly traffic volume** recorded by MnDOT from **2012–2018** on I-94 between Minneapolis and St. Paul.

### Sources

* **Kaggle:** [Metro Interstate Traffic Volume](https://www.kaggle.com/datasets/anshtanwar/metro-interstate-traffic-volume)
* **Direct CSV:** [Metro_Interstate_Traffic_Volume.csv](https://raw.githubusercontent.com/Guilhermertp/machine-learning-zoomcamp2025/refs/heads/main/CapstoneProj/Metro_Interstate_Traffic_Volume.csv)

---

## Dataset Structure

| Feature          | Description                  |
| ---------------- | ---------------------------- |
| `temp`           | Temperature (Kelvin)         |
| `rain_1h`        | Rainfall in last hour (mm)   |
| `snow_1h`        | Snowfall in last hour (cm)   |
| `clouds_all`     | Cloud cover (%)              |
| `holiday`        | Whether the day is a holiday |
| `year`           | Year of observation          |
| `month`          | Month                        |
| `hour`           | Hour                         |
| `traffic_volume` | Target variable              |

---

## Exploratory Data Analysis

### 📊 Average Traffic Volume by Weekday

![Average Traffic Volume by Weekday](asset/barchart.png)

The **bar chart** highlights clear differences in traffic intensity across the week:

* **Peak Days:** **Thursday** and **Friday** record the highest average traffic volumes, slightly exceeding **3,600**, making them the busiest days overall.
* **Consistently Busy Weekdays:** **Monday**, **Tuesday**, and **Wednesday** also maintain high traffic levels, clustered closely between **3,300 and 3,600**, indicating steady commuter-driven demand throughout the workweek.
* **Weekend Decline:** **Saturday** shows a noticeable drop in traffic (around **2,800**), while **Sunday** experiences the lowest volume of the entire week (near **2,400**).
* **Sharp Transition:** The decline from **Friday to Saturday** is substantial, confirming a strong distinction between weekday commuting traffic and weekend travel behavior.

---

### 🌡️ Traffic Volume Heatmap: Hour vs Weekday

![Traffic Volume Heatmap](asset/heatmap.png)

The **heatmap** provides a detailed, granular view of the peak traffic hours and patterns across the days of the week. The darker blue/purple colors represent the highest traffic volumes, while the pale yellow represents the lowest. 

---

#### 1. Weekday (Monday – Friday) Patterns

Weekdays exhibit a **classic commuter traffic profile** with two pronounced peaks:

* **Morning Peak (AM Rush Hour):**

  * Occurs between **7:00 and 9:00**.
  * **8:00** stands out as the busiest morning hour across all weekdays, with volumes exceeding **5,700** and climbing above **6,000** midweek.
* **Evening Peak (PM Rush Hour):**

  * Strongest between **16:00 and 18:00**.
  * **17:00** is the **single busiest hour of the entire week**, reaching the darkest intensities on Wednesday, Thursday, and Friday (above **6,300**).
* **Midday Plateau:** Between **10:00 and 15:00**, traffic dips slightly but remains consistently high (roughly **4,500–5,200**), indicating sustained daytime activity.
* **Overnight Low:** The lowest volumes occur between **0:00 and 5:00**, when traffic is minimal across all weekdays.

---

#### 2. Weekend (Saturday – Sunday) Patterns

Weekend traffic follows a very different rhythm:

* **Saturday:**

  * Traffic increases later in the morning (around **8:00–9:00**).
  * Volumes remain elevated from **10:00 through early evening**, forming a broad, sustained peak rather than sharp rush hours.
  * Peak levels are noticeably lower than weekday PM peaks, reflecting leisure and errand-based travel.
* **Sunday:**

  * Overall traffic is the lightest of the week.
  * Volumes gradually rise late morning and peak between **12:00 and 17:00**, then decline steadily into the evening.
  * Even at its peak, Sunday traffic resembles weekday midday levels rather than rush-hour intensity.

---

#### 3. Key Peak Traffic Hours Summary

| Period      | Day(s)                 | Typical Peak Hours        | Highest Volume Hour |
| ----------- | ---------------------- | ------------------------- | ------------------- |
| **Overall** | **Weekdays (Thu–Fri)** | 16:00 – 18:00             | **17:00 (Evening Rush Hour)**           |
| **AM Peak** | Weekdays               | 7:00 – 9:00               | 8:00                |
| **PM Peak** | Weekdays               | 16:00 – 18:00             | 17:00               |
| **Weekend** | Saturday               | 10:00 – 18:00 (Sustained) | 15:00 – 17:00       |

---

**Overall Insight:**
The combined charts clearly show that traffic demand is **strongly driven by weekday commuting**, with pronounced rush-hour peaks, while weekends feature **lower, more evenly distributed traffic**, dominated by discretionary travel rather than work-related movement.

---

## Modeling and Evaluation

### Potential Models

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting (XGBoost / LightGBM)

### Evaluation Metrics

* **MAE** – average absolute error
* **MSE** – penalizes large errors
* **RMSE** – interpretable version of MSE
* **R² Score** – how much variance is explained

### Why These Evaluation Metrics

Traffic volume is a **regression task**, and these metrics:

* Capture average prediction error (MAE)
* Penalize big mistakes (MSE/RMSE)
* Evaluate overall model fit (R²)

### Model Performance Comparison

| Model             | MAE | MSE | RMSE | R² Score |
| ----------------- | --- | --- | ---- | -------- |
| Linear Regression | —   | —   | —    | —        |
| Decision Tree     | —   | —   | —    | —        |
| Random Forest     | —   | —   | —    | —        |
| XGBoost           | —   | —   | —    | —        |

---

## App Features

* Predict traffic with any regression model
* Simple Flask web UI
* JSON API endpoint
* Fully Dockerized

---

## Prerequisites

```bash
pip install Flask==3.1.2 pandas==2.3.1 numpy==2.3.1 scikit-learn==1.7.0 joblib
```

Optional:

```bash
pip install lightgbm==4.6.0
```

---

## Project Structure

```
project_folder/
│
├─ predict.py
├─ model.pkl
│
├─ assets/
│  ├─ app.png
│  ├─ architecture.png
│  ├─ barchart.png
│  └─ heatmap.png
│
└─ templates/
   └─ index.html
```

---

## Getting the Dataset

### Option 1 Direct Download

```bash
wget https://raw.githubusercontent.com/Guilhermertp/machine-learning-zoomcamp2025/refs/heads/main/CapstoneProj/Metro_Interstate_Traffic_Volume.csv -O Metro_Interstate_Traffic_Volume.csv
```

### Option 2 Kaggle API

```bash
pip install kaggle
kaggle datasets download -d anshtanwar/metro-interstate-traffic-volume -p ./data --unzip
```

---

## Quick Start

### 1 Test via Browser

```bash
python predict.py
```

Visit: [http://127.0.0.1:9696/](http://127.0.0.1:9696/)

### 2 Docker Build

```bash
docker build -t traffic-volume-api .
```

### 3 Docker Run

```bash
docker run -p 9696:9696 traffic-volume-api
```

### 4 Test via JSON API

```bash
curl -X POST http://localhost:9696/predict \
-H "Content-Type: application/json" \
-d "{\"temp\":298.15,\"rain_1h\":0,\"snow_1h\":0,\"clouds_all\":75,\"holiday\":0,\"year\":2018,\"month\":6,\"hour\":14}"
```

---

## App Preview

### Web Form Submission and prediction

![App Interface](asset/app.png)
---
## Conclusion

This project provides a complete template for predicting hourly traffic volume using machine learning.
By combining temporal, weather, and holiday features, the model supports smarter traffic forecasting for cities and commuters.

---

## License

MIT License
Author: **Guilherme Pereira**
Project: **Traffic Volume Prediction App**

---
