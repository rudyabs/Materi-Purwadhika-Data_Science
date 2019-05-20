import matplotlib.pyplot as plt
import numpy as np
import csv

'''
x, y= np.loadtxt(
    '051-test.csv', delimiter= ",", usecols=range(2), unpack=True) 

plt.plot(x, y)
plt.show()
'''

x=[]
y=[]

with open('051-test.csv','r') as dataku:
    data = csv.reader(dataku)
    for i in data:
        x.append(int(i[0]))
        y.append(int(i[1]))

plt.plot(x,y)
plt.show()
