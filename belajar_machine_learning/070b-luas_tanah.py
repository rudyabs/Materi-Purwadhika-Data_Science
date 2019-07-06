import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# print(sklearn.__version__)

x = [5000,20000,25000,13000,8439]
y = [11.5,50,55,32.5,27]
n = len(x)

df = pd.DataFrame({
    'x':np.array(x),
    'y':np.array(y),
    'x2':np.array(x)**2,
    'y2':np.array(y)**2,
    'xy':np.array(x)*np.array(y)
}).sort_values(by='x')

# linear regression sklearn
from sklearn import linear_model

model = linear_model.LinearRegression()

# training .fit(data independent[2D], data dependent[1D])
model.fit(df[['x']],df['y'])

print('Slope= ',model.coef_)
print('Intercept= ', model.intercept_)
print(model.predict([[13000]])) #prediksi nilai y jika x = 200

df['ybest'] = model.predict(df[['x']])
print(df.head(2))

# plotting
plt.plot(
    df['x'],df['y'],'o-',
    df['x'],df['ybest'],'r-'
)
plt.show()