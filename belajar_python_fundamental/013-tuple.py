# tuple

# angka_list = [1, 2, 3, 4, 5, 6]
# angka_tuple = (1, 2, 3, 4, 5, 6)

# angka_list[0] = 1234
# print(angka_list)

# angka_tuple[0] = 1234 #immutable = tidak bisa diubah
# print(angka_tuple)

ls_angka = [
    (1, 2),
    (3, 4)
]

tpl_angka = (
    ['a', 'b'],
    ['c', 'd']
)

print(ls_angka[1][0])
print(tpl_angka[1][0])

tpl_angka[0][1] = 'Andi' #yang bisa diubah dari tuple adalah element didalamnya
print(tpl_angka)
print(type(tpl_angka))

# count function
tpl = ("a","a","c","b")
print(tpl.count("a"))

# index function
print(tpl.index("b"))


