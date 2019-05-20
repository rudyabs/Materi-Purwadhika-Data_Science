# mencari karakter tertentu dengan count
nama = 'Andi tidak masuk sekolah hari ini karena sekolah kebanjiran'
cari = 'sekolah'

print(nama.count('sekolah'))

# mencari karakter tertentu dengan count
kalimat = 'Andi tidak sekolah masuk sekolah hari ini karena sekolah kebanjiran'
cari = 'sekolah'
kalimat_tanpa_cari = kalimat.replace(cari, '')

selisih_karakter = len(kalimat) - len(kalimat_tanpa_cari)
jumlah_cari = int(selisih_karakter / len(cari)) #agar menjadi bilangan integer

print(kalimat)
print(kalimat_tanpa_cari)
print(selisih_karakter)
print(jumlah_cari)