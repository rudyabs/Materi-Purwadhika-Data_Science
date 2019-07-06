import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(0,10,100)
y = np.sin(x)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Lasso

model = make_pipeline(PolynomialFeatures(7),Lasso(alpha=1e-5,max_iter=10000))
model.fit(x.reshape(-1,1),y)

plt.scatter(x,y)
plt.plot(x,model.predict(x.reshape(-1,1)),'r')
plt.show()