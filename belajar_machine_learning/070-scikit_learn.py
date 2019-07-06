'''
pip install scikit-learn
conda install scikit-learn
'''
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# print(sklearn.__version__)

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,5,4,6,5,7,7,8]
n = len(x)

df = pd.DataFrame({
    'x':np.array(x),
    'y':np.array(y),
    'x2':np.array(x)**2,
    'y2':np.array(y)**2,
    'xy':np.array(x)*np.array(y)
})

# linear regression sklearn
from sklearn import linear_model

model = linear_model.LinearRegression()

# training .fit(data independent[2D], data dependent[1D])
model.fit(df[['x']],df['y'])

print('Slope= ',model.coef_)
print('Intercept= ', model.intercept_)
print(model.predict([[200]])) #prediksi nilai y jika x = 200

df['ybest'] = model.predict(df[['x']])
print(df.head(2))

# plotting
plt.plot(
    df['x'],df['y'],'g-',
    df['x'],df['ybest'],'r-'
)
plt.show()