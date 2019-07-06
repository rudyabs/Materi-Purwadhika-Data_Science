import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    {'luas':1000,'harga':1000,'kota':'Bekasi'},
    {'luas':2000,'harga':2000,'kota':'Bekasi'},
    {'luas':3000,'harga':3000,'kota':'Bekasi'},
    {'luas':1000,'harga':1000,'kota':'Depok'},
    {'luas':2000,'harga':2000,'kota':'Depok'},
    {'luas':3000,'harga':3000,'kota':'Depok'},
    {'luas':1000,'harga':1000,'kota':'Jakarta'},
    {'luas':2000,'harga':2000,'kota':'Jakarta'},
    {'luas':3000,'harga':3000,'kota':'Jakarta'},
]

df = pd.DataFrame(data)
# print(df.head(5))

# pandas get dummies
df_dummy = pd.get_dummies(df['kota'],drop_first=True) # drop_first : digunakan untuk menghindari 'silent' multicolinearity
# print(df_dummy.head())
df = pd.concat([df,df_dummy],axis=1).drop('kota',axis=1)
# print(df)

# 2a. sklearn One Hot Encoding
df = pd.DataFrame(data)
# sklearn labelling
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
df_label = df
df['kota'] = label.fit_transform(df['kota'])
# print(df) # kolom kota masih numerical sehingga muncul asumsi bahwa nilai satu lebih besar dr yg lain.
# solusi masalah numerical maka
df_X = df[['kota','luas']].values
# print(df_X)
df_y = df['harga']
# print(df_y)

# 2b. one hot encoder (OHE)
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

coltrans = ColumnTransformer(
    [('OHE',OneHotEncoder(categories='auto'),[0])],
    remainder='passthrough'
)


df_X = np.array(coltrans.fit_transform(df_X), dtype=np.int64)
print(df_X)

# model: Linear Regression
from sklearn.linear_model import LinearRegression
model_lr = LinearRegression()
model_lr.fit(df_X,df_y)
print(model_lr.predict([[0,0,1,1000]]))



