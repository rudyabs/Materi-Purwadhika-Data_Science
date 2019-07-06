import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

data_iris = load_iris()

'''
print(dir(data_iris)) # cek feature yang ada di data iris
print(len(data_iris['data']))
print(data_iris['data'][0:5])
print(len(data_iris['feature_names']))
print(data_iris['feature_names'])
print(len(data_iris['target']))
print(data_iris['target'])
print(data_iris['target_names'])
'''

df = pd.DataFrame(data_iris['data'],columns = ['sL','sW','pL','pW'])
df['target'] = data_iris['target']
df['spesies'] = df['target'].apply(
    lambda x:data_iris['target_names'][x]
)

df0 = df[df['target']==0]
df1 = df[df['target']==1]
df2 = df[df['target']==2]

print(df.head())
print(df.tail())

# plotting
import matplotlib.pyplot as plt
import seaborn as sns


'''
fig = plt.figure('Data Iris',figsize=(10,5))

plt.subplot(121)
plt.scatter(df0['sL'],df0['sW'])
plt.scatter(df1['sL'],df1['sW'])
plt.scatter(df2['sL'],df2['sW'])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(data_iris['target_names'])
plt.title('Sepal Length (cm) VS Sepal Width (cm)')
plt.grid(True)

plt.subplot(122)
plt.scatter(df0['pL'],df0['pW'])
plt.scatter(df1['pL'],df1['pW'])
plt.scatter(df2['pL'],df2['pW'])
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(data_iris['target_names'])
plt.title('Petal Length (cm) VS Petal Width (cm)')
plt.grid(True)
'''
# plt.show()

# split train test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df[['sL','sW','pL','pW']],df['target'],test_size=0.1)

# print(len(x_train))
# print(len(x_test))
# print(x_train.iloc[0])

# logistic regression
from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression(solver='liblinear',multi_class='auto')

log_model.fit(x_train,y_train)

skor = log_model.score(x_train,y_train)
m = log_model.coef_
c = log_model.intercept_

# print(skor,m,c)

# print(x_test.iloc[0].values)
# print(y_test.iloc[0])
# print(log_model.predict([x_test.iloc[0].values]))

# print(df[['sL','sW','pL','pW']])
# print(log_model.predict(df[['sL','sW','pL','pW']]))

df['t_model'] = log_model.predict(df[['sL','sW','pL','pW']])
df['s_model'] = df['t_model'].apply(lambda x: data_iris['target_names'][x])

# print(df)

# sns.violinplot(x='target',y='t_model',hue='spesies',data=df)
# plt.show()

df0 = df[df['t_model']==0]
df1 = df[df['t_model']==1]
df2 = df[df['t_model']==2]

fig = plt.figure('Data Prediksi',figsize=(10,5))

plt.subplot(121)
plt.scatter(df0['sL'],df0['sW'])
plt.scatter(df1['sL'],df1['sW'])
plt.scatter(df2['sL'],df2['sW'])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(data_iris['target_names'])
plt.title('Sepal Length (cm) VS Sepal Width (cm)')
plt.grid(True)

plt.subplot(122)
plt.scatter(df0['pL'],df0['pW'])
plt.scatter(df1['pL'],df1['pW'])
plt.scatter(df2['pL'],df2['pW'])
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(data_iris['target_names'])
plt.title('Petal Length (cm) VS Petal Width (cm)')
plt.grid(True)



# from sklearn.metrics import classification_report, confusion_matrix

# predictions = log_model.predict(x_test)
# print(confusion_matrix(y_test,predictions))
# print('\n')
# print(classification_report(y_test,predictions))


plt.show()