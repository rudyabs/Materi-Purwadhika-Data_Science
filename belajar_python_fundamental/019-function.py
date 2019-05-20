# function

'''
def nama_fungsi():
    program

nama_fungsi()
'''
# # function tanpa parameter/argumen
# def tes():
#     print('Hello World')

# tes()

# # function dengan parameter
# def parmet(x):
#     print('Halo', x)

# parmet('Andi')
# parmet('Budi')
# parmet(input("Masukan nama anda: "))

# def kalkulator(x, y):
#     z = x**y
#     print("Hasil kali", x, "dan", y, "=", x*y)
#     print("Hasil", x, "pangkat", y, "=", z)

# kalkulator(2, 3)

# ================================

import math

def luas_lingkaran(r):
    luas = math.pi * r * r
    print('Luas lingkaran dengan r=', r, 'adalah', luas)

# luas_lingkaran(5)

def luas_trapesium(a, b, t):
    luas = (a + b) * (t / 2)
    print("Luas trapesium a=", a, "b=", b, "t=", t, "adalah", luas)

# luas_trapesium(1,2,3)

# return function

def halo():
    return 'Halo Andi'

# print(halo())
x = int(input('Masukan angka pertama: '))
y = int(input('Masukan angka kedua: '))

def jumlah(x, y):
    return x + y
    
print("Jumlah dari", x, "dan", y, "adalah", jumlah(x, y))    

def kuadrat(x):
    return x ** 2

print(kuadrat(2) + kuadrat(2))
print(kuadrat(8))