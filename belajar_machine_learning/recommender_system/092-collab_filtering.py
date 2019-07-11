'''
Collaborative Filtering
'''
import numpy as np
import pandas as pd

df = pd.read_csv('092-sample.csv',delimiter=',',index_col=0,)
df.fillna(0,inplace=True)
print(df)

# Correlation
'''
pearson : standard correlation coefficient
kendall : Kendall Tau correlation coefficient
spearman : Spearman correlation coefficient
'''
df_corr = df.corr()
# print(df_corr)

# testing
preferensi_saya = [
    ('kartun_a',4),
    ('sinetron_b',1)
]

skor_sama = pd.DataFrame()
for produk, rating in preferensi_saya:
    skor = df_corr[produk] * (rating - 2.5) # standarisasi dengan nilai median 2.5
    skor = skor.sort_values(ascending = False)
    skor_sama = skor_sama.append(skor,ignore_index=False)
   
print(skor_sama.sum().sort_values(ascending=False))