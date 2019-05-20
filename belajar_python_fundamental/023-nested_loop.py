# NESTED LOOP

'''
list_saya = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

for baris in list_saya:
    for element in baris:
        print(element)
'''
# ----------------------------------

data = [
    [
        ['Andi','Budi','Caca'],
        ['Dono', 'Eva','Gandi'],
        ['Gigi', 'Hana', 'Ika']
    ],
    [
        ['Jojo','Koko','Lala'],
        ['Momo', 'Nana','Opo'],
        ['Popi', 'Qiqi', 'Raul']
    ]
]

for i in data:
    for j in i:
        for k in j:
            print(k)