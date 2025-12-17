import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib

# Link to the dataset on my github
url = 'https://raw.githubusercontent.com/Guilhermertp/machine-learning-zoomcamp2025/refs/heads/main/CapstoneProj/Metro_Interstate_Traffic_Volume.csv'

df = pd.read_csv(url)

# Convert to datetime with dayfirst=True
df['date_time'] = pd.to_datetime(df['date_time'], dayfirst=True)

# Extract only the hour into a new column, as the year, month, and day are unnecessary since the analysis does not focus on seasonal or long-term trends.
df['hour'] = df['date_time'].dt.hour

df['weekday'] = df['date_time'].dt.day_name()  # Monday, Tuesday, etc.

# There are some columns that are redundant or won't be necessary for the analysis
col_keep = ['traffic_volume', 'holiday', 'temp', 'rain_1h', 'snow_1h', 'clouds_all','hour','weekday']

df = df[col_keep]

# Binary encoding of column holiday
df['is_holiday'] = df['holiday'].notna().astype(int)

# Drop original column holiday since is not needed
df.drop(columns=['holiday'], inplace=True)

# One-hot encoding for the categorical features
df_final = pd.get_dummies(df, columns=['weekday'], drop_first=True)

# **************Setting Up the Validation Framework**************

df_full_train, df_test = train_test_split(df_final,test_size=0.2,random_state=1)
df_train, df_val = train_test_split(df_full_train,test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train['traffic_volume']
y_val = df_val['traffic_volume']
y_test = df_test['traffic_volume']

# Delete the target variable for the datasets I will use for training,validate and test to avoid future problems
del  df_train['traffic_volume']
del  df_val['traffic_volume']
del  df_test['traffic_volume']

# Train
X_train = df_train

# Validation
X_val = df_val

# Test
X_test = df_test

# **************Modeling - Gradient Boosting (XGBoost)**************

# ******Training model******
xgb_model = XGBRegressor(n_estimators=500, max_depth=6, learning_rate=0.1, subsample=0.8, colsample_bytree=1.0, random_state=42)
xgb_model.fit(X_train, y_train)

# ******Predictions******
y_val_pred_xgb = xgb_model.predict(X_val)
y_test_pred_xgb = xgb_model.predict(X_test)



# **************Saving the model (XGBoost)**************
filename = "model_xgb.pkl"
joblib.dump(xgb_model, filename)

print(f"Model saved as {filename}")
