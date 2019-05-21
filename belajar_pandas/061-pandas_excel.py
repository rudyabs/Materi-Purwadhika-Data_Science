import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pip install xlrd

# df = pd.read_excel('061-test.xlsx')

excel = pd.ExcelFile('061-test.xlsx')

df1 = pd.read_excel(excel, 'Usia Pegawai')
df1 = df1.set_index('id')
df1 = df1.sort_values(by='id')
df2 = pd.read_excel(excel, 'Gaji Pegawai') # baca dengan sheet 'Gaji Pegawai'
df2 = df2.set_index('id')
df2 = df2.sort_values(by='id')

print(df1)
print(df2)

df1['gaji']=df2['gaji'] # direkomendasikan data disortir terlebih dahulu
print(df1)