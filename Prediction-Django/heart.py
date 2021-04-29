import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
from sklearn.linear_model import LogisticRegression
# warnings.filterwarnings("ignore", category=DeprecationWarning)
from sklearn.preprocessing import StandardScaler
import random
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_validate

data = pd.read_csv("heart.csv")
data["trestbps"] = np.log(data["trestbps"])

data = data.drop(["fbs"], axis=1)
data = data.drop(["ca"], axis=1)
data["chol"] = np.log(data["chol"])
target = data["target"]
print(data.shape[1])

np.random.shuffle(data.values)
data = data.drop(["target"], axis=1)
print(data.columns)
sc = StandardScaler()
data = sc.fit_transform(data)

lr = LogisticRegression()
print("this is data...........",data)
lr.fit(data, target)
cv_results = cross_validate(lr, data, target, cv=10)
print(cv_results)

import joblib

joblib.dump(lr, "heart_model")

# While Giving the values for the prediction we need to covert the input to standard scalar
# sconvert= StandardScaler()
# converting_factor=scconvert.fit_transform("Two Dimensional Input")