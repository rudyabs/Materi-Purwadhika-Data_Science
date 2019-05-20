import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dataframe
'''
angka = [4,5,8,6,4,7,2,1,3,5]
huruf = ['a','b','c','d','e','f','g','h','i','j']


# df_value = pd.DataFrame([value, nama], columns=[1,2,3,4,5,6,7,8,9,10])
# print(df_value)

my_df = pd.DataFrame()
my_df['Score'] = angka
my_df['Name'] = huruf
print(my_df)
'''
# dataframe: list dari list, tuple dari list(optional)
'''
data = [
    ['Andi', 90],
    ['Budi', 80],
    ['Caca', 70],
    ['Dedi', 60],
    ['Endo', 50]
]
# data = np.arange(11)

df_data = pd.DataFrame(data, columns=['nama','score'])
print(df_data)
print(df_data.shape)
row, column = df_data.shape
print(row)
print(column)
'''
# dataframe: dict
'''
data = {
    'nama': ['Andi','Bui','Coco'],
    'score': [88,58,63]
}

df_data=pd.DataFrame(data)
print(df_data)
'''
# contoh dict
data = [
    {'nama': 'Andi', 'nilai':90},
    {'nama': 'Budi', 'nilai':80},
    {'nama': 'Caca', 'nilai':70},
    {'nama': 'Deni', 'nilai':60},
    {'nama': 'Edi', 'nilai':50}
]

df_data = pd.DataFrame(
    data,
    index = list('abcde') # ubah index default menjadi 'abcde'
    )
print(df_data)
baris, kolom = df_data.shape
print(f'Dataframe ini mempunyai {baris} baris')
print(f'Dataframe ini mempunyai {kolom} kolom')

print('head(3) mengambil 3 baris pertama')
print(df_data.head(3)) # ambil 3 baris pertama dalam dataframe
print('tail(2) mengambil 2 baris terakhir')
print(df_data.tail(2)) # ambil 2 baris terakhir dalam dataframe
print(df_data.columns) # menampilkan nama kolom
print(df_data.index) # menampilkan index

print(df_data.values) # ambil values dari dataframe
print(df_data.describe()) # memperlihatkan statistikal analisis

# print(df_data.sort_index(ascending=False))
# print(df_data.sort_values(by = 'nilai', ascending=False))
# print(df_data.sort_values(
#     by=['nama','nilai'],
#     ascending=[False,False]
# ))

# print(df_data['nama'])
# print(df_data['nilai'])
# print(type(df_data['nama']))
# print(type(df_data['nilai']))

# print(df_data[0:5:2])
# print(df_data[df_data['nilai']>50])
# print(df_data.loc['a'])
# print(df_data.loc['a':'c', ['nama']])

# print(df_data.iloc[0:5:2, 0:2])

# print(df_data.at['a', 'nama']) # panggil value dgn nama index dan nama kolom
# print(df_data.iat[0, 1]) # panggil value dgn urutan nama index dan urutan nama kolom

# multifilter
'''
print(df_data
    .iloc[0:5:2]
    .sort_values(
        by = ['nilai','nama'],
        ascending = [True, False]
    )[['nilai','nama']]
)
'''

plt.plot(df_data['nama'], df_data['nilai'])
plt.show()