import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = 10 * np.random.RandomState(1).rand(50)
x = np.sort(x)
y = 2 * x - 5 + np.random.RandomState(1).randn(50)

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Linear Regression
model_linear = LinearRegression()

# Pipeline: Polynomial + Lasso
model_lasso = make_pipeline(PolynomialFeatures(8),Lasso(alpha=1e-15, max_iter=1e5))

# Pipeline: Polynomial + Ridge
model_ridge = make_pipeline(PolynomialFeatures(8),Ridge(alpha=1e-15))


# training model
model_linear.fit(x.reshape(-1,1),y)
model_lasso.fit(x.reshape(-1,1),y)
model_ridge.fit(x.reshape(-1,1),y)

# plot
fig = plt.figure('Regression', figsize=(15,6))

plt.subplot(1,3,1)
plt.scatter(x,y,color='y', marker='.')
plt.plot(x, model_linear.predict(x.reshape(-1,1)),'r-')

plt.subplot(1,3,2)
plt.scatter(x,y,color='y', marker='.')
plt.plot(x, model_lasso.predict(x.reshape(-1,1)),'r-')

plt.subplot(1,3,3)
plt.scatter(x,y,color='y', marker='.')
plt.plot(x, model_ridge.predict(x.reshape(-1,1)),'r-')

plt.show()