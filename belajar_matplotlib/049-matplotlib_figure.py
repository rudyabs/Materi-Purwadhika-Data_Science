import matplotlib.pyplot as plt
import numpy as np


x =  np.arange(5)
y = np.array([1,2,3,4,5])
z = 2 * y

print(x)
print(y)
print(z)

# buat 2 figure
'''
# buat figure 1
plt.figure('Figure 1 - XY')
plt.plot(x,y, 'r-')
plt.grid(True)
plt.title('Fig 1')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.legend(['Hubungan XY'])

# buat figure 2
plt.figure('figure 2 - XZ')
plt.plot(x, z, 'g--')
plt.grid(True)
plt.title('Fig 2')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.legend(['Hubungan xz'])
'''
# Buat 1 Fugure 2 subplot
plt.figure('Figure XYZ', figsize=(10,5)) # figsize(lebar, tinggi)

# buat plot 1
plt.subplot(1,2,1)
plt.plot(x,y, 'r-')
plt.grid(True)
plt.title('Plot 1')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.legend(['Hubungan XY'])

# buat plot 2
plt.subplot(1,2,2)
plt.plot(x, z, 'g--')
plt.grid(True)
plt.title('Plot 2')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.legend(['Hubungan xz'])

plt.suptitle('Hubungan XY dan XZ')
plt.show()
