import numpy as np

# # variable
# x1 = [1,2,3,4,5,6]
# x2 = (1,2,3,4,5,6)
# x3 = {1,2,3,4,5,6}
# y = np.array(x3) #mengubah ke numpy array

# print(x1)
# print(type(x1))

# print(x2)
# print(type(x2))

# print(x3)
# print(type(x3))

# # print salah satu element
# print(x1[0])
# print(x2[0])
# print(x3[0])

# print(y)
# print(type(y))
# =======================================================================

# numpy array = np.arrange

# z = np.arange(100)
# print(z)

# y = np.arange(50, 100) # dari 50 sampai dengan 99
# print(y)

# z = np.arange(50, 100, 2) # dari 50 sampai 99 loncat 2
# print(z)

# index dalam numpy array
# print(z)
# print(z[0])
# print(z[-1])
# print(z[5::2])

# cek dimensi dalam array (berapa n dimensi)

# print(z)
# print(z.ndim)

# cek panjang list/array

# print(len(z))
# print(z.size)

# # cek item size

# print(z.itemsize) # ukuran dengan bytes

# # cek data type

# print(z.dtype)

# =================================================

# z = np.array([1,'a',2,'b',3,'c'])

# print(z.dtype)

# ==================================================

# membuat data random

# y = np.random.rand(5)
# z = np.random.rand(4, 5)
# u1 = np.random.randint(10) #mengeluarkan 1 angka int tdk lebih dr 10
# u2 = np.random.randint(10, size=10)
# u3 = np.random.randint(10, size=(2,10))

# print(y)
# print(y.ndim)
# print(z)
# print(z.ndim)

# print(u1)
# print(u2)
# print(u2.ndim)
# print(u3)
# print(u3.ndim)

# ====================================================