import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = 10 * np.random.RandomState(1).rand(50)
x = np.sort(x)
y = 2 * x - 5 + np.random.RandomState(1).randn(50)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge

model = make_pipeline(PolynomialFeatures(7),Ridge(alpha=1e-15))
model.fit(x.reshape(-1,1),y)

plt.scatter(x,y)
plt.plot(x,model.predict(x.reshape(-1,1)),'r')
plt.show()