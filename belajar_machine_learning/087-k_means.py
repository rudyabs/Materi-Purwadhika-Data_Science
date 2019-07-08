'''
K-Means
'''
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()

# checking the data
# print(dir(data))
# print(data['data'][0])
# print(data['feature_names'])
print(data['target_names'])

# making DataFrame from data
df = pd.DataFrame(data['data'],columns=['SL','SW','PL','PW'])
df['target'] = data['target'] # making target(dependent variable)
df['species'] = df['target'].apply(lambda x: data['target_names'][x])
print(df.head())
print(df.tail())

print(df.isnull().sum()) # checking the sum of null in dataframe (df)


# ML Model: k-means
from sklearn.cluster import KMeans
model_sepal = KMeans(n_clusters=len(data['target_names']), random_state=1)
model_petal = KMeans(n_clusters=len(data['target_names']), random_state=1)

model_sepal.fit(df[['SL','SW']],df['target'])
model_petal.fit(df[['PL','PW']],df['target'])

df['prediksi_sepal'] = model_sepal.predict(df[['SL','SW']])
df['prediksi_petal'] = model_petal.predict(df[['PL','PW']])

df0 = df[df['target']==0]
df1 = df[df['target']==1]
df2 = df[df['target']==2]

df_sep0 = df[df['prediksi_sepal']==0]
df_sep1 = df[df['prediksi_sepal']==1]
df_sep2 = df[df['prediksi_sepal']==2]


df_pet0 = df[df['prediksi_petal']==0]
df_pet1 = df[df['prediksi_petal']==1]
df_pet2 = df[df['prediksi_petal']==2]

print(model_sepal.predict(df[['SL','SW']]))
print(model_petal.predict(df[['PL','PW']]))

# centroid
centroid_sepal = model_sepal.cluster_centers_
centroid_petal = model_petal.cluster_centers_

# plotting
import matplotlib.pyplot as plt
fig = plt.figure('Data Iris', figsize=(10,6))

plt.subplot(221)
plt.plot(df0['SL'],df0['SW'],'r.')
plt.plot(df1['SL'],df1['SW'],'g.')
plt.plot(df2['SL'],df2['SW'],'b.')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.scatter(centroid_sepal[:,0],centroid_sepal[:,1], marker='o',color='lightblue',s=500)
plt.legend(['Sentosa','Versicolor','Virginica','Centroid'])

plt.subplot(222)
plt.plot(df0['PL'],df0['PW'],'r.')
plt.plot(df1['PL'],df1['PW'],'g.')
plt.plot(df2['PL'],df2['PW'],'b.')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.scatter(centroid_petal[:,0],centroid_petal[:,1], marker='o',color='lightblue',s=500)
plt.legend(['Sentosa','Versicolor','Virginica','Centroid'])

plt.subplot(223)
plt.plot(df_sep0['SL'],df_sep0['SW'],'r.')
plt.plot(df_sep1['SL'],df_sep1['SW'],'g.')
plt.plot(df_sep2['SL'],df_sep2['SW'],'b.')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.scatter(centroid_sepal[:,0],centroid_sepal[:,1], marker='o',color='lightblue',s=500)
plt.legend(['Sentosa','Versicolor','Virginica','Centroid'])

plt.subplot(224)
plt.plot(df_pet0['PL'],df_pet0['PW'],'r.')
plt.plot(df_pet1['PL'],df_pet1['PW'],'g.')
plt.plot(df_pet2['PL'],df_pet2['PW'],'b.')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.scatter(centroid_petal[:,0],centroid_petal[:,1], marker='o',color='lightblue',s=500)
plt.legend(['Sentosa','Versicolor','Virginica','Centroid'])

plt.show()
plt.close()

# ML Model: KNN

def nNeihbors(): # menentukan patokan KNeighborsClassifier untuk n_neighbors parameter
    '''
    1.  sqrt(total jml data) = sqrt(150) = 12,2 = 13/11
    2.  ambil yg ganjil +1 / -1
    '''
    x = round(len(len(data['data'])**.5))
    if x % 2 == 0:
        return x + 1
    else:
        return x

from sklearn.neighbors import KNeighborsClassifier
model_knn = KNeighborsClassifier(n_neighbors= nNeihbors())

model_knn.fit(df[['SL','SW','PL','PW']], df['target'])

df['prediksi_knn'] = model_knn.predict(df[['SL','SW','PL','PW']])

print(df[df['target']]==0)
print(df[df['target']]==1)
print(df[df['target']]==2)


