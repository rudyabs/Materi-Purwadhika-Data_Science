import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing

data_cal = fetch_california_housing()

# print(dir(data_cal))
# print(len(data_cal['data']))
# print(len(data_cal['data']))
# print(len(data_cal['data'][0]))
# print(data_cal['feature_names'])
# print(data_cal['target'][0])

df = pd.DataFrame(data_cal['data'],columns=data_cal['feature_names'])
df['target'] = data_cal['target']
# print(df.head())

# split
from sklearn.model_selection import train_test_split
X = df.drop('target',axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# print(len(X_train),len(y_train))
# print(len(X_test),len(y_test))

# Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

predictions = model.predict(X_test)
print(predictions)
df['predictions'] = model.predict(df[df.columns.values[0:8]])
print(df.head())

print(df.corr())

sns.heatmap(df.corr(),annot=True)
plt.show()