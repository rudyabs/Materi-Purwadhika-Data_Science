# Umumnya terdapat 2 cara untuk memformat string

# .format() method

# contoh
print("Hari ini {} {} {}".format("Andi", "tampar", "Budi"))
print("Hari ini {2} {1} {0}".format("Andi", "tampar", "Budi"))
print("Hari ini {0} {1} {2}".format("Andi", "tampar", "Budi"))

# contoh menggunakan list
nama1 = ["Andi", "Budi", "Caca"]
nama2 = ["Dodi", "Eka", "Fani"]
print("Ini adalah string buatan {}".format(nama1[1]))

# float formatting dengan .format() method
# "{value:width.precision f}"
hasil = 100/777
print(hasil)

print("Hasil dari 100/666 adalah {h:1.3f}".format(h=hasil))

# f-string method
nama3 = "Bobo Widodo"
umur = 51
print(f"Pegawai baru itu bernama {nama3} berumur {umur}.")