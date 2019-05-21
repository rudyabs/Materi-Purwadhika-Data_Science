'''
menunjukan selection dengan
menggunakan contoh file fifa19
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_main = pd.read_csv('data.csv')
# print(df['Name'])

df = df_main.copy()
'''
print(df['Overall'].max())
print(df['Overall'].min())
print(df['Overall'].mean())

print(df[df['Overall']==df['Overall'].max()])
print(df[df['Overall']==df['Overall'].max()]['Name'])
print(df[df['Overall']==df['Overall'].max()][['Name','Club']])

print(df[df['Overall']>=90][['Name','Position','Club']])
print(df[
    ['Name','Position','Club']]
    [df['Overall']>=90]
    )

print(
    df[['Name','Position','Club']]
    [df['Overall']>=90]
    [df['Club']=='Real Madrid']
)
'''

# tanpa warning deklarasikan ke df
'''
df = df[['Name','Position','Club']][df['Overall']>=90]
df = df[df['Club']=='Real Madrid']
print(df)
print(df['Overall'])
dfTranspose = df.T
print(dfTranspose)
print(dfTranspose.index)

'''


young_good = df[df['Age']<25][df['Overall']>=85]
young_bad = df[df['Age']<25][df['Overall']<85]
old_good = df[df['Age']>=25][df['Overall']>=85]
old_bad = df[df['Age']>=25][df['Overall']<85]

plt.scatter(young_good['Age'], young_good['Overall'], c='red')
plt.scatter(young_bad['Age'], young_bad['Overall'], c='blue')
plt.scatter(old_good['Age'], old_good['Overall'], c='yellow')
plt.scatter(old_bad['Age'], old_bad['Overall'], c='green')
plt.grid(True)
plt.legend(['Young_Good', 'Young_Bad', 'Old_Good','Old_Bad'])

plt.show()
