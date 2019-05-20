import numpy as np
import matplotlib.pyplot as plt

# menggambar 3x + 2y =12
# titik potong sumbu y ketika x=0 => 2y=12
# | 2 || y | = | 12 |
a = np.array([[2]])
b = np.array([[12]])
c = np.linalg.solve(a, b)
print(c)

# titik potong sumbu x ketika y=0 => 3x=12
# | 3 || x | = | 12 |
d = np.array([[3]])
e = np.array([[12]])
f = np.linalg.solve(d, e)
print(f)

# titik potong
x = np.array([f,0])
y = np.array([0, c])

plt.plot(x,y)
plt.xticks(np.arange(0,7,1))
plt.show()