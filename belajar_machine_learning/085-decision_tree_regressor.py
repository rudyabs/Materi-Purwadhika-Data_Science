import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data1 = np.random.RandomState(1).randn(100)
x1 = np.sort(data1)
y1 = np.sin(-x1)

y1[::10] += 2*(0.5-np.random.RandomState(1),rand(10))


x1 = x1.reshape(-1,1)

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=3)
model.fit(x1,y1)

predictions = model.predict(x1)
print(predictions)

plt.scatter(x1,y1)
plt.plot(x1,predictions,'r-')
plt.show()