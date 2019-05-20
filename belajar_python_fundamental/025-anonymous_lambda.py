# map function
# contoh penggunaan map
# contoh 1
def square(num):
    result = num ** 2
    return result

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))

# contoh 2
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andi', 'Budi', 'Cacad']

for x in map(splicer, names):
    print(x)

print(list(map(splicer, names)))
# ------------------------------------
# filter function
# digunakan untuk function dgn output boolean dan iterasi yang mengeluarkan output sesuai dengan function
# contoh
def check_even(num):
    return num%2== 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even, mynums)))

for n in filter(check_even, mynums):
    print(n)

# ------------------------------------
# lambda function

'''
digunakan untuk membuat fungsi tanpa nama(anonymous),
satu kali penggunaan dan tidak digunakan kembali
'''

print(list(map(lambda num:num**2, my_nums)))

mynames = ['Andi', 'Budi', 'Caca']
print(list(map(lambda x:x[0], mynames)))
print(list(map(lambda x:x[-1], mynames)))

# ------------------------------------
# contoh lambda function
'''
def x(a):
    return a * 2

y = lambda a : a * 2

print(x(23))
print(y(22))
'''
# ------------------------------------
'''
def x(a,b,c):
    return a+b+c

y = lambda a,b,c : a+b+c

print(x(1,2,3))
print(y(1,2,3))
'''
# ------------------------------------
'''
def kali(n):
    return lambda x : x * n

kali_dua = kali(2)
kali_tiga = kali(3)

print(kali_dua(20))
print(kali_tiga(20))
'''
# -------------------------------------
'''
def y(a):
    return a
def x(a):
    print (y(a))

x(12)
'''
# --------------------------------------
'''
def x():
    return lambda c : c + c
b = x()
print(b(13))
'''