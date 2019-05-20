# dictionaries

nama_hari = {
    'Monday': 'Senin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
}



print(type(nama_hari))
print(nama_hari.keys())
print(list(nama_hari.keys())[0])
print(list(nama_hari.values()))

# akses key by value (hanya diketahui value nya)
print(
    list(nama_hari.keys())[list(nama_hari.values()).index('Selasa')]
)

# print(nama_hari['Monday'])
# print(nama_hari.get('Tuesday'))
# print(nama_hari.get('Friday', 'Maaf data tidak ada'))

# nama_hari['Monday'] = 'Senen'
# print(nama_hari)
# nama_hari['Thursday'] = 'Kamis'
# print(nama_hari)

# nama_hari.pop('Monday')
# print(nama_hari)