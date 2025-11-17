import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier

path = 'https://raw.githubusercontent.com/Guilhermertp/machine-learning-zoomcamp2025/refs/heads/main/MidTermProj/data/earthquake_data_tsunami.csv'

!wget $path

df = pd.read_csv(path)

df_full_train, df_test = train_test_split(df,test_size=0.2,random_state=1,stratify=df['tsunami'])
df_train, df_val = train_test_split(df_full_train,test_size=0.25,random_state=1,stratify=df_full_train['tsunami'])

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train['tsunami'].values
y_val = df_val['tsunami'].values
y_test = df_test['tsunami'].values

# Delete the target variable for the datasets I will use for training,validate and test to avoid future problems
del df_train['tsunami']
del df_val['tsunami']
del df_test['tsunami']

X_train = df_train.values
X_val   = df_val.values
X_test  = df_test.values

### Training model LIGHTGBM

from lightgbm import LGBMClassifier


# LightGBM Model
lgbm = LGBMClassifier(
    n_estimators=800,
    learning_rate=0.005,
    num_leaves=31,
    max_depth=3,
    subsample=0.7,
    colsample_bytree=0.9,
    random_state=42
)

lgbm.fit(X_train, y_train)

# Predictions
train_pred = lgbm.predict(X_train)
val_pred = lgbm.predict(X_val)
test_pred = lgbm.predict(X_test)

## Save the model

import joblib

# Save the trained model
joblib.dump(lgbm, "lgbm_model.pkl")
print("Model saved to lgbm_model.pkl")