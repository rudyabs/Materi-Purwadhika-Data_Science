import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
y = np.array([7,5,6,9,8])
z = np.random.randn(5)

# buat plot
'''
plt.plot(x,y, 'r--')
'''

# membuat scatter
'''
plt.scatter(x, y, color='r', marker='o', s=50)
'''

# membuat bar
'''
plt.bar(x,z, color='y', yerr=.9)
plt.bar(x,y, color='r', bottom=z) #bottom digunakan utk menumpuk bar
# tanpa bottom akan membuat depan belakang bar
'''

# membuat histogram
'''
plt.hist([y,z],x, histtype='bar', rwidth=.5)
'''

# membuat pie
warna = ['orange','y','g','b','red']
plt.pie(y, labels=('Andi','Budi','Caca','Doni','Egi'), startangle=90, colors=warna, shadow=True, explode=(0,0,0,0.1,0), autopct='%1.1f%%', pctdistance=1.2, labeldistance=1.35, textprops={'color':'red'})
plt.legend(y, loc='upper left', bbox_to_anchor=(0.5,0.5,0.5,0.5))


plt.show()