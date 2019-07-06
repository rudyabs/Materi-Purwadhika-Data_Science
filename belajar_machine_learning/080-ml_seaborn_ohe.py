import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('titanic')

# Labelling
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()

data['sex'] = label.fit_transform(data['sex'])
# print(label.classes_)
data['who'] = label.fit_transform(data['who'])
# print(label.classes_)
data['adult_male'] = label.fit_transform(data['adult_male'])
# print(label.classes_)
data['alone'] = label.fit_transform(data['alone'])
# print(label.classes_)

data = data.drop(
    ['embarked','class','deck','embark_town','alive'],axis=1
)

data = data.dropna(subset=['age'])

# Menentukan X dan y
X = data.drop('survived',axis=1)
y = data['survived']

# OHE
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

col_trans = ColumnTransformer([('OHE',OneHotEncoder(categories='auto'),[1,6])], remainder='passthrough')

X = np.array(col_trans.fit_transform(X),dtype=np.float64) # dtype : jika ditemukan data float atau integer secara bersamaan akan dikonvert

# print(X)
# print(X[0])
# [ 0.    1.    0.    1.    0.    3.   22.    1.    0.    7.25  1.    0.  ]
# fm male child man woman pclass age sibsp par fare adultM alone 

# train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1,random_state=1)

# print(X_train[0])
# print(y_train.iloc[0])
# print(X_test[0])
# print(y_test.iloc[0])

# model - logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear')
model.fit(X_train,y_train)

predictions = model.predict(X_test)

# print(model.score(X_train,y_train))
# print(model.score(X_test,y_test))   

# from sklearn.metrics import mean_squared_error
# print(mean_squared_error(y_test,predictions))

from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,predictions))

import joblib as jb
model_jb = jb.dump(model, '080-logreg_deploy.joblib')