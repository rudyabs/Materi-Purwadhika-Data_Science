# install seaborn -- pip install seaborn
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
sn.set(style='darkgrid') # style dalam seaborn


mydata = sn.load_dataset('flights')
# print(data)
data_pivot = mydata.pivot('month', 'year', 'passengers')
# print(data_pivot)

# sn.relplot(x='year', y='passengers', data=mydata, hue='month', size='year')
# sn.catplot(x='year', y='passengers', data=mydata, hue='month', kind='bar')
# sn.barplot(x='year', y='passengers', data=mydata, hue='month')
# sn.lmplot(x='year', y='passengers', data=mydata, hue='month')
# sn.heatmap(data_pivot, cmap='hot_r') # cmamp='r' dimana r mereverse 
sn.swarmplot(x='year', y='passengers', data=mydata)
plt.xticks(rotation=90)


plt.show()