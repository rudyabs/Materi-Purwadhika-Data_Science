import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('071-harga_rumah.csv')
# print(df.head())

# plt.plot(df['luas'],df['harga'])
# sns.pairplot(df)

# sns.lmplot(df['luas'],df['harga'],data=df)
# plt.show()

# Linear Regression
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

lm.fit(df[['luas']],df['harga'])
# slope/gradien m best fit line
m = lm.coef_
# intercept c best fit line
c = lm.intercept_

df['harga_terbaik'] = m*df['luas']+c
print(df)

# plot dengan best fit line (linear regression)
# plt.plot(df['luas'],df['harga'],'r-')
# plt.plot(df['luas'],df['harga_terbaik'],'g-')
# plt.grid()
# plt.legend(['Harga Real','Harga Terbaik'])
# plt.show()
