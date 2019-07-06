'''
multivariate analysis - linear regression
multiple variable
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('071-harga_rumah.csv')

# sns.pairplot(df)
# plt.show()

# linear regression
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(df[['usia','kamar','luas']],df['harga'])

m = lm.coef_
c = lm.intercept_
print(m)
print(c)

# predictions
predictions = lm.predict([[5,10,2000]])
print(predictions)

print(round(lm.score(df[['usia','kamar','luas']],df['harga'])*100,2),'%')
