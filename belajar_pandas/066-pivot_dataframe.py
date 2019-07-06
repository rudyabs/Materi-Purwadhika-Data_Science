import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    '063-tlkm_saham.csv',
    index_col =  False,
    parse_dates = ['Tanggal']
)

# print(df.head(1))
# print(type(df['Tanggal'][0]))

# df1 = [
#     {'id':1,'Jakarta':100,'Jumlah':122,'Nilai':88},
#     {'id':1,'kota':'Bogor','Jumlah':215,'Nilai':96},
#     {'id':2,'kota':'Jakarta','Jumlah':415,'Nilai':78},
#     {'id':2,'kota':'Bogor','Jumlah':54,'Nilai':69},
#     {'id':3,'kota':'Bogor','Jumlah':331,'Nilai':78},
#     {'id':3,'kota':'Jakarta','Jumlah':321,'Nilai':54}
# ]

# df = pd.DataFrame(df1)

# print(df.pivot(
#     index = 'id',
#     columns='kota'
# ))

# print(df.pivot(
#     index = 'id',
#     columns='kota'
# )['Nilai'])

df2 = [
    {'Lokasi':'Jakarta','Jan-2019':25,'Feb-2019':27,'Mar-2019':28},
    {'Lokasi':'Bogor','Jan-2019':22,'Feb-2019':25,'Mar-2019':24},
    {'Lokasi':'Depok','Jan-2019':24,'Feb-2019':24,'Mar-2019':26},
    {'Lokasi':'Tanggerang','Jan-2019':23,'Feb-2019':27,'Mar-2019':28},
    {'Lokasi':'Bekasi','Jan-2019':21,'Feb-2019':26,'Mar-2019':27}
    ]

df2 = pd.DataFrame(df2)

# print(df2)
dfmelt = pd.melt(
    df2,
    id_vars=['Lokasi'],
    var_name='Date',
    value_name='Value'
    )

print(dfmelt)

# dfcrosstab =  pd.crosstab(
#     df['Lokasi']
# )

# croostabnya BELOM