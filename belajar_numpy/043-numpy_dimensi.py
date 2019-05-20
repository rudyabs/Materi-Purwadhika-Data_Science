import numpy as np

satu = np.array([1,2,3])
dua = np.array([[1,2,3]])
tiga = np.array([[[1,2,3]]])

# print(satu)
# print(satu.ndim)
# print(dua)
# print(dua.ndim)
# print(tiga)
# print(tiga.ndim)

# ===========================================
# a = [[[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12]
# ]]]

# b = np.array(a)

# print(b)
# print(b.ndim)

# # melihat bentuk/shape
# print(b.shape)
# =============================================

# reshape = mengubah dimensi dari suatu array
# a = [
#     [1,2,3,4,5],
#     [4,5,6,8,9]
# ]

# a = np.array(a)

# print(a)
# print(a.shape)

# b = a.reshape(10,1)
# print(b)
# print(b.shape)

# index dan slicing

# print(a[0,2])
# print(a[0][2])
# print(a[0:, [0, -1]])
# print(a[0:, 0:])

# ====================================

# line spacing
# x = np.linspace(1, 2, 10)
# print(x)
# print(x.size)

# ====================================

# x = np.random.randint(10, size=(1,10))
# print(x)
# print(x.shape)
# print(x.max())
# print(x.min())

# =======================================

x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([[1,2,3]])

x1 = [1,2,3]
y1 = [4,5,6]

# print(x1 + y1)
# print(x + y)
# print(x * y)
# print(x / y)

print(z.ndim)
print(z.shape)