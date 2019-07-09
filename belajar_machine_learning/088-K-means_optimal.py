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

# print(df.head())
# print(df.tail())

# K optimeal K-means: SSE (Sum Square Error) + elbow method

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(df[['SL','SW','PL','PW']])
print(model.inertia_)

sse = []
for x in range(1,15):
    model =KMeans(n_clusters=x)
    model.fit(df[['SL','SW','PL','PW']])
    sse.append(model.inertia_)

# plot
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16,10))
plt.plot(range(1,15),sse,color='blue',linestyle='--',marker='o',markerfacecolor='red',markersize=10)
plt.title('SSE vs K')
plt.xlabel('K')
plt.ylabel('SSE')
plt.grid(True)
plt.tight_layout()
plt.show()