# Comparison Operators

a = 12
b = 13
c = '12'

# print(a <= b)
# print(a >= int(c))
# print(a > int(c))
# print(a > b)

# if dengan comparison operators
nilai_ujian = 40
    # >= 80 maka 'lulus'
    # >= 60 tapi < 80 maka 'remedial'
    # < 60 maka 'tidak lulus'


# if nilai_ujian >= 80:
#     print('Nilai anda =', nilai_ujian, 'Anda dinyatakan lulus!')
# elif nilai_ujian >= 60 and nilai_ujian < 80: # alternatif: elif 80 > nilai >= 60
#     print('Nilai anda =', nilai_ujian, 'Anda harus remedial!')
# else:
#     print('Nilai anda =', nilai_ujian, 'Anda dinyatakan TIDAK LULUS!')

# ======================================
angka = (input('Silahkan ketik angka: '))

if angka.isdigit():
    if int(angka) % 2 == 0:
        print('Angka', angka, 'tergolong GENAP')
    else:
        print('Angka', angka, 'tergolong GANJIL')
else:
    print('Maaf input yang dimasukan haruslah angka!')

# comparison operators
x = 1
y = 3


# equal to
print(x == y)

# not equal to
print(x != y)

# greater than
print(x > y)

# less than
print(x < y)

# greater than or equal to
print(x >= y)

# less than or equal to
print(x <= y)


