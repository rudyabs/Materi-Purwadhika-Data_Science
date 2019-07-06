import numpy as np
import pandas as pd

df = pd.read_csv('071-harga_rumah.csv')

# print(df.head(3))
# print(df.info())
# print(df.describe())

# metode dengan dummy
df_dummy = pd.get_dummies(df['kota'])
# print(df_dummy)

# hapus kolom kota dari df
df = df.drop(['kota'],axis=1)
# print(df)

# concat df_dummy ke df utama
df = pd.concat([df,df_dummy],axis=1)
# print(df)

# linear regression
from sklearn.linear_model import LinearRegression

X = df.drop(['harga'],axis=1)
y = df['harga']
# print(X)
# print(y)

lm = LinearRegression()
lm.fit(X,y)

# print(lm.predict([[200,10,2,1,0,0]]))

dfnew = pd.DataFrame({
    'realvalue':y,
    'bestvalue':lm.predict(X).astype('int64')
})

print(dfnew)
import matplotlib.pyplot as plt
import seaborn as sns

sns.lmplot(x='realvalue',y='bestvalue',data=dfnew)
plt.show()