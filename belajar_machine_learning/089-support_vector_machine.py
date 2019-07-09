import numpy as np
import pandas as pd

from sklearn.datasets  import load_iris

import matplotlib.pyplot as plt
import seaborn as sns

data = load_iris()
df = pd.DataFrame(data['data'],columns=['SL','SW','PL','PW'])
df['target'] = data['target']
df['species'] = df['target'].apply(lambda x: data['target_names'][x])
print(df.head())

# plotting persebaran data awal
# plt.plot(
#     df[df['target']==0]['PL'],
#     df[df['target']==0]['PW'],
#     'r.'
# )
# plt.plot(
#     df[df['target']==1]['PL'],
#     df[df['target']==1]['PW'],
#     'g.'
# )
# plt.plot(
#     df[df['target']==2]['PL'],
#     df[df['target']==2]['PW'],
#     'b.'   
# )
# plt.show()

# model - SVM
from sklearn.svm import SVC
model_petal = SVC(gamma='auto')
model_sepal = SVC(gamma='auto')

model_petal.fit(df[['PL','PW']], df['target'])
model_sepal.fit(df[['SL','SW']], df['target'])

df['prediksi'] = model_petal.predict(df[['PL','PW']])

# print(df)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(df['target'],df['prediksi']))
print(confusion_matrix(df['target'],df['prediksi']))

# plotting data terluar
x_max_petal = df['PL'].max() +1
x_min_petal = df['PL'].min() -1
y_max_petal = df['PW'].max() +1
y_min_petal = df['PW'].min() -1

x_max_sepal = df['SL'].max() +1
x_min_sepal = df['SL'].min() -1
y_max_sepal = df['SW'].max() +1
y_min_sepal = df['SW'].min() -1

# print(x_max,x_min,y_max,y_min)

# method meshgrid
'''
# contoh penggunaan meshgrid
x = np.linspace(0,1,5)
y = np.linspace(0,1,5)
print(x)
print(y)
xx,yy = np.meshgrid(x,y)
print(xx)
    np.arange(x_min,x_max_petal,0.01),
'''

XP, YP = np.meshgrid(
    np.arange(x_min_petal,x_max_petal,0.01),
    np.arange(y_min_petal,y_max_petal,0.01)
)
XS, YS = np.meshgrid(
    np.arange(x_min_sepal,x_max_sepal,0.01),
    np.arange(y_min_sepal,y_max_sepal,0.01)
)
# print(X)
# print(Y)
# print(len(X))
# print(len(X[0]))
# print(len(X.ravel())) # 440*790

# X_ravel = [x1 x2 x3 x4 xn]
# Y_ravel = [y1 y2 y3 y4 yn]

ZP = model_petal.predict(np.c_[XP.ravel(),YP.ravel()])
ZP = ZP.reshape(XP.shape)
ZS = model_sepal.predict(np.c_[XS.ravel(),YS.ravel()])
ZS = ZS.reshape(XS.shape)


fig = plt.figure('SVM Data Iris')
gambar = plt.subplot(121)
gambar.contourf(XP,YP,ZP, cmap='inferno', alpha=0.5)
plt.plot(
    df[df['target']==0]['PL'],
    df[df['target']==0]['PW'],
    'r.'
)
plt.plot(
    df[df['target']==1]['PL'],
    df[df['target']==1]['PW'],
    'g.'
)
plt.plot(
    df[df['target']==2]['PL'],
    df[df['target']==2]['PW'],
    'y.'
)
gambar = plt.subplot(122)
gambar.contourf(XS,YS,ZS, cmap='inferno', alpha=0.5)
plt.plot(
    df[df['target']==0]['SL'],
    df[df['target']==0]['SW'],
    'r.'
)
plt.plot(
    df[df['target']==1]['SL'],
    df[df['target']==1]['SW'],
    'g.'
)
plt.plot(
    df[df['target']==2]['SL'],
    df[df['target']==2]['SW'],
    'y.'
)


plt.show()