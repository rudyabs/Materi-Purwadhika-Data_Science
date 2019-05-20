# if statement

# sudah_kerja = True

# if sudah_kerja == True:
#     print('Traktiran donk!')
# else:
#     print('Makanya cari kerja yang bener!')

# alternatif khusus untuk boolean
# if sudah_kerja:
#     print('Traktiran donk!')
# else:
#     print('Makanya cari kerja yang bener!')

# job = 'PNS'

# if job == 'PNS':
#     print('Anda PNS')
# elif job == 'Swasta':
#     print('Anda swasta')
# else:
#     print('Pengangguran')

bekerja = True
jomblo = True

if bekerja and jomblo:
    print('Anda sudah kerja, kok jomblo?')
elif bekerja and not(jomblo):
    print('Selamat ~ ~ ~')
elif not(bekerja) and jomblo:
    print('Mau dikasih makan apaan?')
else:
    print('Cari kerja dulu sana!')