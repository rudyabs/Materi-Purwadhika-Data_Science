import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(
    'indo_12_1.xls',
    skipfooter=3,
    header=3,
    index_col=0,
    na_values='-'
)
df_sum = pd.read_excel(
    'indo_12_1.xls',
    skipfooter=2,
    header=3,
    index_col=0,
    na_values='-'
)
 
# print(df)

# variable untuk plotting

dfmax_2010 = df[df[2010]==df[2010].max()]
dfmin_1971 = df[df[1971]==df[1971].min()]
x_2010 = dfmax_2010.columns.values
y_2010 = dfmax_2010.iloc[0]
x_1971 = dfmin_1971.columns.values
y_1971 = dfmin_1971.iloc[0]

df_indo = df_sum[df_sum[2010]==df_sum[2010].max()]
nama_indo = df_indo.iloc[-1].name
x_indo = df_indo.columns.values
y_indo = df_indo.iloc[0]

# print(df_indo)
# print(nama_indo)
# print(x_indo)
# print(y_indo)

# print(dfmax_2010.index)
# print(dfmax_2010.index[0])
# print(df.loc[dfmax_2010.index[0]])

# Linear Regression
from sklearn.linear_model import LinearRegression

modelmax2010 = LinearRegression()
modelmin1971 = LinearRegression()
modelindo = LinearRegression()

# training - model fit
'''
print(dfmax_2010.columns.values.reshape(-1,1)) # "-1" kebalikan dari 6
print(dfmax_2010.values[0])
print(dfmin_1971.columns.values.reshape(-1,1)) 
print(dfmin_1971.values[0])
print(df_indo.columns.values.reshape(-1,1)) 
print(df_indo.values[0])
'''

x = dfmax_2010.columns.values.reshape(-1,1)
y = dfmax_2010.values[0]
modelmax2010.fit(x,y)
print(modelmax2010.score(x,y))

x = dfmin_1971.columns.values.reshape(-1,1)
y = dfmin_1971.values[0]
modelmin1971.fit(x,y)
print(modelmin1971.score(x,y))

x = df_indo.columns.values.reshape(-1,1)
y = df_indo.values[0]
modelindo.fit(x,y)
print(modelindo.score(x,y))

# pembulatan
max2050 = int(round(modelmax2010.predict([[2050]])[0]))
min2050 = int(round(modelmin1971.predict([[2050]])[0]))
indo2050 = int(round(modelindo.predict([[2050]])[0]))

# Jumlah Penduduk Tahun 2050
# print(modelmax2010.predict([[2050]]))
# print(modelmin1971.predict([[2050]]))
# print(modelindo.predict([[2050]]))

print(max2050)
print(min2050)
print(indo2050)

# plotting

# database
plt.plot(x_2010,y_2010,'b-o')
plt.plot(x_1971,y_1971,'r-o')
plt.plot(x_indo,y_indo,'g-o')

# best fit line
plt.plot(x_2010,modelmax2010.coef_*x_2010+modelmax2010.intercept_,'y-')
plt.plot(x_1971,modelmin1971.coef_*x_1971+modelmin1971.intercept_,'y-')
plt.plot(x_indo,modelindo.coef_*x_indo+modelindo.intercept_,'y-')

plt.grid()
plt.legend()
plt.title(f'Jumlah Penduduk {nama_indo} (1971-2010)')

plt.show()

