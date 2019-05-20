import numpy as np

# x = np.array([[1,2,3], [4,5,6]])

# # bentuk matriks
# # | 1 2 3 |
# # | 4 5 6 |

# # print(x + x)

# x =np.array([
#     [1,3,2,5],
#     [3,4,6,9],
#     [2,6,7,8],
#     [5,9,8,2]
# ])
# y = np.array([2])

# print(x)
# print(x * y)

# ==========================================

# soal persamaan 2 variable (linear algebra)
# \[2x + y = 5 \]
# \[x + y = 7 \]

# | 2 1 | | x | = | 5 |
# | 1 1 | | y |   | 7 |

# a = np.array([[2,1],[1,1]])
# b = np.array([5,7])
# c = np.linalg.solve(a, b) 

# print(a)
# print(b)
# print(c)

# ================================================
# 2 persamaan
# 3x + y = 9
# x + 2y = 8
#  x? y?

# a = np.array([[3,1], [1,2]])
# b = np.array([9,8])
# c = np.linalg.solve(a,b)

# print(a)
# print(b)
# print(c)
# ================================================
# 1 persamaan
# 3x = 9

# a = np.array([[3]])
# b = np.array([9])
# c = np.linalg.solve(a, b)
# print(c)
# ================================================
# 3 persamaan

# x + y - z = -3
# x + 2y + z = 7
# 2x + y + z = 4

# a = np.array([[1,1,-1],[1,2,1],[2,1,1]])
# b = np.array([-3,7,4])
# c = np.linalg.solve(a,b)

# print(c)