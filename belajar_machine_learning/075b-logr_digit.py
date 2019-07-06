import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_digits

data_digit = load_digits()

# print(dir(data_digit))
# print(len(data_digit['data']))
# print(data_digit['data'][0])
# print(len(data_digit['images']))
# print(data_digit['images'][0])
# print(len(data_digit['target_names']))
# print(data_digit['target_names'])


# dataframe
df = pd.DataFrame(data_digit['data'])
# print(df.head(2))
# print(df.shape[0])

# split, train
# manual
# train = round(0.9*df.shape[0])
# train = df.iloc[:train]
# test = df.iloc[train:]

# dari sklearn
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data_digit['data'],data_digit['target'],test_size=0.33,random_state=101)

# model
from sklearn.linear_model import LogisticRegression
lgr = LogisticRegression(solver='liblinear',multi_class='auto')

# training
lgr.fit(X_train,y_train)
print(lgr.score(X_train,y_train))

# prediksi
print(y_test[0])
print(lgr.predict(X_test[0].reshape(1,-1)))

# draw image, real data, real predict
fig = plt.figure(figsize=(5,5))
plt.imshow(X_test[0].reshape(8,8))
plt.title(
    'Data Asli = {} // Prediksi = {}'
    .format(y_test[0],lgr.predict(X_test[0].reshape(1,-1))[0])
)
plt.show()