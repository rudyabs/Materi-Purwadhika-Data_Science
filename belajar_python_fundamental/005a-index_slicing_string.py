# penerapan indexing dan slicing dalam "string"
# ref: 005-indexing_slicing.txt

nama_lengkap = "Totok Dimianto Minto Dihardjo"
panjang_nama = len(nama_lengkap)

# mengambil karakter tertentu - indexing

#ambil huruf awal
print(nama_lengkap[0])
# ambil huruf akhir 
print(nama_lengkap[-1]) 
# ambil karakter ke-6
print(nama_lengkap[6]) 

# ====================================================

# penerapan slicing

# ambil karakter ke-6 dan seterusnya
print(nama_lengkap[6:]) 
# ambil karater sampai ke-4
print(nama_lengkap[:5])
# ambil karakter dari 6 sampai 13
print(nama_lengkap[6:14])
# penerapan step size :loncat 2 karakter
print(nama_lengkap[::2])
# mulai dari ke-2 stop di-7 loncat 2
print(nama_lengkap[2:7:2])
# membuat kebalikan nama
print(nama_lengkap[::-1])