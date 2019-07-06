'''
random forest tutorial
'''

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_digits

digits = load_digits()

# print(dir(digits))
# print(digits['target_names'])
# print(len(digits['target']))
# print(digits['data'][0])
# print(digits['images'][0])

df = pd.DataFrame(digits['data'])
df['target'] = digits['target']
# print(df.head(3))

X = df.drop(['target'],axis=1)
y = df['target']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1)

# print(X_train[0])
# print(y_train.iloc[0])

# random forest
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=50)
model.fit(X_train,y_train)

# extreme random forest
from sklearn.ensemble import ExtraTreesClassifier
model_extra = ExtraTreesClassifier(n_estimators=50)
model_extra.fit(X_train,y_train)

predictions = model.predict([X_test.iloc[0]])
predictions_extra = model_extra.predict([X_test.iloc[0]])


print(y_test.iloc[0])
print(predictions)
print(model.score(X_test,y_test))
print(model_extra.score(X_test,y_test))

# plotting
import matplotlib.pyplot as plt
plt.imshow(X_test.iloc[0].values.reshape(8,8))
plt.title(f'Dataset: {y_test.iloc[0]} Prediction R-Forest: {predictions} Score R-Forest: {model.score(X_test,y_test)} Prediction E-Forest: {predictions_extra} Score E-Forest: {model_extra.score(X_test,y_test)}')
plt.show()