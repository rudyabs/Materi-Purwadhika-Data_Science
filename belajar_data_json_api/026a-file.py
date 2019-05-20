# input/output dengan text(.txt) file
# selalu ingat nama file dan tempat directory dimana file disimpan
# error no. 2 - kesalahan dalam penulisan nama atau tempat lokasi directory
# pwd - command utk melihat dimana path kita berada

# read .txt files => 'r'
# write . txt files => w
# open() => access loacal file
'''
# file = open('026-dummy.txt', 'r')
file = open('026-dummy.txt', 'w')
file.write(input('selamat pagi'))
'''
'''
print(file.readable())
print(file.read())
'''
# ============================================
'''
if file.readable():
    # print(file.read())
    open_file = file.readlines()
    print(open_file[1])
else:
    print("File yang ingin dibuka tidak support")
'''
# Buat atau write file based on code editor or .txt dan write (overwrite)
'''
file = open('026-dummy_buat_baru.py', 'w')
file.write("print('halo 1!')\n")
file.write("print('halo 2!')")
'''

# Append file
# file = open('026-dummy_buat_baru.py', 'a')
# file.write("\nprint('halo tes!')")

# membuka file di directory lain
file_saya = open('C:\\Users\\rudya\\OneDrive\\Dokumen\\Training _ Courses\\Data Science Fundamental\\Purwadhika\\Coret\\026-dummy.txt', 'r')
print(file_saya.read())

# menutup file yang sedang dikerjakan
# file_saya.close() #manual

# mengerjakan file tanpa mengganggu file tersebut
with file_saya as file_kerja: #file_saya digantian dengan file yang ingin dikerjakan
    isi_file = file_kerja.read()
