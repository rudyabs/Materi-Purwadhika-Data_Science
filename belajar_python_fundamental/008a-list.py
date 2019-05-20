# Apa itu list
'''
List 
    - merupakan tempat menampung objek secara berurutan
    - list mendukung indexing dan slicing
    - list juga dapat digabung(nested) dengan list lainnya
Contoh List
    [1,2,3,4,5]
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
'''
# contoh
daftar_list_1 = ["one", "two", "three"]
daftar_list_2 = ["four", "five", "six"]
daftar_list_baru = daftar_list_1 + daftar_list_2

print(daftar_list_1 + daftar_list_2)
print(daftar_list_baru)

# mengganti element dalam list
daftar_list_1[0] = "ONE BIG"
print(daftar_list_1)

# append -> menambahkan element dalam list
daftar_list_2.append("delapaaaan")
print(daftar_list_2)

# pop -> mengeluarkan element terakhir dalam list
print(daftar_list_1.pop())
# mengeluarkan element yang lain
print(daftar_list_1.pop(0))
print(daftar_list_1)

# penggunaan <sort> dalam list
daftar_huruf = ["a", "c", "e", "d", "b"]
daftar_angka = [5, 3, 4, 1, 2]

daftar_huruf.sort()
print(daftar_huruf)

# penggunaan <reverse>
daftar_angka.sort()
daftar_angka.reverse()
print(daftar_angka)
