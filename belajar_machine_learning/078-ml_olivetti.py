import numpy as np
import pandas as pd

from sklearn.datasets import fetch_olivetti_faces

import matplotlib.pyplot as plt
import seaborn as sns

data = fetch_olivetti_faces()
print(dir(data))

print(data['data'][0])
print(len(data['images'][0]))
print(len(data['images'][0][0]))
print(data['images'][0].shape)

# plotting wajaha dalam database
# fig = plt.figure('Wajah?')
# for i in range(10):
#     orangke = 10
#     plt.subplot(2,5,i+1)
#     plt.imshow(data['images'][i+(10*(orangke-1))],cmap='gray')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data['data'], data['target'], test_size=0.33, random_state=42)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear',multi_class='auto')
model.fit(X_train,y_train)

print(model.predict(X_test[0].reshape(1,-1)))
print(y_test[0])

plt.imshow(X_test[0].reshape(64,64),cmap='gray')
plt.title(f'Data aktual: {y_test[0]} \\ Prediksi {model.predict(X_test[0].reshape(1,-1))[0]} \\ Model Score {model.score(X_train,y_train)}')
plt.show()