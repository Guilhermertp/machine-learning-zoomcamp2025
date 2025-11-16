**Tsunami Prediction API**

Description

This project predicts whether an earthquake will generate a tsunami based on earthquake features such as magnitude, depth, location, and other seismic parameters. The target variable is:

- `1` → Tsunami occurred  
- `0` → No tsunami  

The model is trained using machine learning algorithms (Logistic Regression, Random Forest, LightGBM) and saved using `joblib`. A REST API is provided using Flask, and the application can be containerized with Docker for easy deployment.

---

**Requirements**

- Python 3.8+
- Flask
- pandas
- scikit-learn
- joblib
- lightgbm (if using LightGBM model)
- Docker (for containerization)

---

**Project Structure**


**How to run the project**
1) To deploy the model, in the command line, go to the environment where is the file predict.py and run the following:

python predict.py 

+++ NEWER VERSIONS OF PYTHON RUN +++ 
py predict.py

Note: Running predict.py, starts a live web service (API server) on your machine using Flask

2) To get 