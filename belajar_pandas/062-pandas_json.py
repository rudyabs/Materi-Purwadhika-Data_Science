import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_json('062-test.json')
cols = df.columns.tolist()

print(cols)

cols = cols[-1:] + cols[:-1]
df = df[cols]

print(df)
# print(df['nama])
# print(df.nama)
# print(df[df['kota']=='Ambon'])


# butuh install openpyxl
# conda install openpyxl
# pip install openpyxl

df.to_csv('062-test_convert_csv.csv', index = False)
df.to_excel('062-test_convert_xlsx.xlsx', index = False)
df.to_json('062-test_convert_json.json', orient='records')
# orient = records, values, index, table, columns