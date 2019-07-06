import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston # import datasets boston dr sklearn

data_boston = load_boston()

'''
print(data_boston)              # data sample
print(len(data_boston.data))    # total rows data sample
print(data_boston.data[0])      # 1st data sample
print(len(data_boston.data[0])) # total column
print(data_boston.data.shape)

print(data_boston['data'].shape)
print(data_boston['feature_names']) # nama column tanpa target

print(data_boston['target']) # data target yang ingin di prediksi
print(len(data_boston['target']))
'''

'''
buat dataframe dari boston dataset
'''
# dataframe boston
df_boston = pd.DataFrame(data_boston['data'],columns = data_boston['feature_names'])

# dataframe target yang akan di predik
df_boston['MEDV'] = data_boston['target']
# print(df_boston)

'''
feature dari dataset boston
'''
# print(dir(data_boston))
# print(data_boston['filename']) # tempat dimana dataset boston dapat di cari
# print(data_boston['DESCR']) # PENJELASAN TENTANG DATASET BOSTON

'''
model linear regression
'''
# import model
from sklearn.linear_model import LinearRegression
model_ln = LinearRegression()

'''
training
'''
model_ln.fit(df_boston[data_boston['feature_names']], df_boston['MEDV'])

print(model_ln.coef_)
print(model_ln.intercept_)
print(model_ln.score(
    df_boston[data_boston['feature_names']],
    df_boston['MEDV']
))


