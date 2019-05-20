# import library: math (bult-in)

import math

# print(math.pi)
# print(math.sqrt(16))
# print(math.floor(2.98))
# print(math.ceil(5.21))

# ================================

# factorial

z = 6
# print(math.factorial(z))

# modulus

# print(10 % 2)
# print(10 % 3)
# print(10 % 4)
# print(10 % 10)
# print(1 % 2)

# ================================

total = int(input('Total usia = '))
rasio = float(input('Rasio usia = '))

org1 = int(total / (1 + rasio))
org2 = int(total - org1)

print('Usia org1= ', org1, 'th & usia org2 = ', org2, 'th')