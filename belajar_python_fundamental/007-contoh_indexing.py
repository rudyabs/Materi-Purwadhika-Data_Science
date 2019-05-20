# strings
# test

nama = 'Andi Susilo Wijaya Kusumo'

print(nama.lower())
print(nama.upper())
print(nama.isupper())
print(nama.isupper())

print(nama.lower().islower())
print(nama.upper().isupper())
print(type(nama.upper().isupper()))

# mengitung jumlah
print(len(nama))

# mengambil karakter dari (0-...)
print(nama[0])

# mengambil karakter terakhir

print(nama[len(nama) - 1])

print(nama.index('Wijaya'))

print(nama.replace('Kusumo', 'Kusumowibowo'))

print(nama.split('i'))
print(nama.split(' ')[1])

# menghitung jumlah huruf dinama seseorang (spasi tdk dihitung)
# penghitung jumlah huruf tertentu dalam suatu kata

'''
kata = 'And Iadi'
cari = 'i'
cari?
'''

print(nama.split(' '))