import numpy as np
from scipy import stats

# a = np.array([[1,4],[2,5],[3,6]])
# b = np.array([[3,6],[4,7],[5,8]])
# c = 2
# print(a + b)
# print(c * a)
# ====================================
# dot product

# a = np.array([
#     [2,1,4,3],
#     [2,5,1,2],
#     [1,3,2,2]
# ])
# b = np.array(
#     [[1,3],
#     [3,2],
#     [2,5],
#     [1,4]]
# )
# print(a @ b)
# print(a.dot(b))

# ====================================
# determinan

# a = np.array([[7,5], [2,9]])
# # | 7 5 |
# # | 2 9 |   # DET A / |A| = 7.9 - 5.2 = -2

# print(np.linalg.det(a)) # butuh di round 
# print(round(np.linalg.det(a)))

# b = np.array([
#     [1,0,0],
#     [2,6,0],
#     [4,5,2]
# ])

# print(np.linalg.det(b))
# print(round(np.linalg.det(b)))

# ====================================
# invers

# a = np.array([
#     [3,2,1],
#     [6,5,4],
#     [9,8,7]
# ])

# b = np.array([[4,1],[7,2]])

# print(np.linalg.inv(a))
# print(np.linalg.inv(b))

# ====================================
# transpose
# a = np.array([[4,7,8,1],[3,9,8,6]])

# print(a.transpose())

# ====================================
# pi, cos, sin, tan, exponent

# print(np.pi)
# print(np.cos(0))
# print(np.tan(0))
# print(np.sin(0))
# print(np.exp(2)) # e pangkat 2 -> dimana e = bilangan euler

# ====================================
# logaritma

# print(np.exp(2))
# print(np.log(7.38905609893065)) # e log 7.39 = 2

# 10 log 1000
# print(np.log10(1000))

# ====================================
# median, mode, mean

# a = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# print(a)
# print(np.mean(a))
# print(np.median(a))
# print(stats.mode(a))
# print(np.mean(a, axis=1))

# ==========================================