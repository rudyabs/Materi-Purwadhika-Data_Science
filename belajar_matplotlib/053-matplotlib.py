import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d # membuat 3d graphic

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

# z1 = np.array([0,0,0,0,0])
# x1 = np.array([1,1,1,1,1]) 
# y1 = np.array([1,1,1,1,1])

z1 = np.zeros(5) # membuat array yang berisi 0 berjumlah 5 lement
x1 = np.ones(5) # membuat array yang berisi 1 berjumlah 5 element
y1 = np.ones(5)

z = np.array([1,3,5,7,9])

plt.figure('My 1st 3D Plot/Scatter/Bar')
ax3  = plt.subplot(111, projection='3d') #projection = 3d -- memproyeksikan 3d plot

# ax1.plot_wireframe(ax1, x,y,z) # plot 3d -- menentukan sumbu pada plot 3d
# ax1.set_xlabel('Nilai X')
# ax1.set_ylabel('Nilai Y')
# ax1.set_zlabel('Nilai Z')


# ax2.scatter(ax2,x,y,z, color='y', marker='*', s=200) # membuat diagram 3d scatter
# ax2.set_xlabel('Nilai X')
# ax2.set_ylabel('Nilai Y')
# ax2.set_zlabel('Nilai Z')

ax3.bar3d ( x,y, z1, x1, y1, z,
    color= ['red', 'blue', 'yellow', 'green', 'cyan'])

ax3.set_xlabel('Nilai X')
ax3.set_ylabel('Nilai Y')
ax3.set_zlabel('Nilai Z')
ax3.set_title(label='Tes 3D Bar', loc='left')

plt.show()