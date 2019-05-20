# conda install pandas
# pip install pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# myarray = np.array([10,20,30,40,50])
myarray = np.arange(0,21)
# mylist = ['andi','budi','caca']

# pandas series
myseries = pd.Series(
    myarray, 
    name='Students', 
    # index= ['a','b','c']
    )

print(myseries)
# print(mylist['a'])

print(myseries[myseries%2 == 0])

# print(myseries[0:3:2])

plt.plot(myseries,myseries)
plt.show()