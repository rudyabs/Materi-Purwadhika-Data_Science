import numpy as np

# soal cari x, y, z
# x + y - z = -3
# x + 2y + z = 7
# 2x + y + z = 4 

a = np.array([[1,1,-1], [1,2,1], [2,1,1]])
b = np.array([-3,7,4])
c = np.linalg.solve(a, b)

print(a)
print(b)
print(c)

