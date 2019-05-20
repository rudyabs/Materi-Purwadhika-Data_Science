import matplotlib.pyplot as plt
# alternatif dari : from matplotlib import pyplot as plt
import numpy as np

# a = [0,1,2,3,4,5,6,7,8,9]
# b = [1,5,6,8,7,2,5,9,7,5]

# # melakukan plotting
# plt.plot(a,b)
# plt.xlabel('Nilai x') # memberi judul parameter x
# plt.ylabel('Nilai y') # memberi judul parameter y
# plt.grid(True) # menambahkan grid
# plt.legend(['Data Saya']) # menambahkan legend
# plt.show() # menampilkan hasil plot

# =====================================================

x = np.arange(10)
y = np.array([5,7,8,6,9,4,5,2,3,4])

print(plt.style.available)
# plt.style.use('grayscale')

plt.plot(x,y, linestyle='-', color='#FF00FF', linewidth='2') # parameter '--' mengganti bentuk garis
# plt.plot(x, y/2, '*', )
# plt.plot(x,y, x, y**2, x, y*3, 'bs')


plt.fill_between(x,y[2],y[4],5, facecolor='yellow', alpha=.3)
plt.text(x[4],y[4], 'titikn/max')

for titik in x:
    plt.text(titik-.1, y[titik]+.2, x[titik])

plt.plot(x,y, 'ro')

plt.annotate('Nilai tertinggi', xy=(4,9), xytext=(1,9), arrowprops = dict(arrowstyle='->', facecolor='blue'))

plt.title('Plot Saya')
plt.xlabel('Nilai x') 
plt.ylabel('Nilai y', color='yellow') # memberi judul parameter y
plt.xticks(np.arange(0,10, step=1)) # rotasi : rotaion =
plt.yticks(np.arange(0,13,2)) 
plt.grid(True) 
plt.legend(['Data Saya'], loc=1) # parameter "loc=<1-10>" untuk menentukan lokasi legend dimana loc=0 berupa default
plt.subplots_adjust(left=0.14, right=0.95, bottom=0.14, top=0.88, wspace=.2, hspace=.2)
# plt.savefig('Figure.png')
plt.show() 

# - : line
# -- : dash
# o : point
# s : square
# ^ : segitiga
# * : star
# . : dot
# r red