# Apa it Dictionaries
'''
dictionaries
    - tempat menaruh objek berpasangan yang tidak berurutan
    - dictionaries menggunakan curly braces {}
        -> contoh: {"key1":"value1","key2":"value2"}
    - objek diambil dengan key name
    - tidak berurutan dan tidak bisa di sort
    - berguna saat mengambil data tanpa tahu lokasi(index)
'''

# Penerapan dictionaries
my_dict = {"key1":"value1","key2":"value2"}
harga_buah = {"pisang":1000, "apel":2000, "jeruk":3000}

print(my_dict["key1"])
print(harga_buah["jeruk"])

# Variable dalam dict
a = 100
b = 200

percobaan = {"k1":a,"k2":b}
print(percobaan["k1"])

# penggunakan index dalam dict
c = {"key1":[1,2,3], "key2":["a","b","c"]}
print(c["key1"][1])
print(c["key2"][1].upper()) #merubah value dalam dict

# merubah  value dalam dict
c["key1"][2] = "TIGA"
print(c)

# melihat values dalam dict
print(c.values())

# melihat items dalam dict
print(c.items()) # menghasilkan tuple
