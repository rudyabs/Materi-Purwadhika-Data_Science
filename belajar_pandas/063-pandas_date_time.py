import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
# review
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([0,1,2,3,4])
s3 = pd.Series(np.arange(1,6))

# contoh pengaplikasian tanggal pada pandas dataframe
df = pd.DataFrame({
    'nomor':[1,2,3,4,5],
    'nama':['Andi','Budi','Caca','Dani','Eka'],
    'gender': pd.Categorical(['L','L','P','L','L']),
    'kota': 'Jakarta',
    'tanggal-1': pd.Timestamp('20191228'),
    'tanggal-2': pd.date_range('20190527', periods=5)
})

# print(df)

# tanggal pandas
tgl = pd.Timestamp('20190527')
print(tgl)
print(type(tgl))

tgl2 = pd.date_range('20190928', periods=3)
print(tgl2)
print(type(tgl2))
'''

df = pd.read_csv('063-tlkm_saham.csv',index_col=False,parse_dates=['Tanggal'])

# print(df.head())
# print(df.info())

df = df.set_index('Tanggal')
df = df.sort_index()

# print(df.head())

# print(df['2019-02'])
# print(df['2019-02-27':'2019-02-28'])
# print(df['27-02-2019':'28-02-2019'])
# print(df.loc['27-02-2019'])

# print(df['2019-03']['Close'].mean())
# print(df['2019-03']['Close'].max())
# print(df['2019-03']['Close'].min())

print(df[df['Close']==df['2019-03']['Close'].max()])

plt.plot(
    df.index, df['Close'], 'r-',
    df.index, df['Open'], 'b:'
)


plt.xlabel('Tanggal')
plt.ylabel('Rp')
plt.xticks(rotation=65)
plt.grid(True)


plt.show()
