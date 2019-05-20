# variables
nama = 'Rudy Aunallah Bumi Satrio' # menghitung jumlah spasi dengan split
total = len(nama)
jumlah_spasi = len(nama.split(' ')) - 1
total_tanpa_spasi = total - jumlah_spasi

print('Nama', nama, 'mengandung: ', total_tanpa_spasi, 'huruf')

# mencari karakter tertentu dengan replace
nama = 'Rudy Aunallah Bumi Satrio'
cari_huruf = 'i'
nama_tanpa_cari = nama.lower().replace(cari_huruf.lower(), '') 
# lower()/upper() digunakan agar dapat mencari huruf yg berbeda upper/lower case
jumlah_cari = len(nama) - len(nama_tanpa_cari)

print(nama_tanpa_cari)
print('Jumlah', cari_huruf, 'dalam', nama, 'adalah', jumlah_cari)

