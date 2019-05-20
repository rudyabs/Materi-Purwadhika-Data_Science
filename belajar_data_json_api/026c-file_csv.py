# untuk buka file csv
'''
file = open('./contoh3.csv', 'r')
print(file.readable())
print(file.read())
'''

# membaca file csv dengan package 'csv'
'''
import csv

with open('contoh3.csv', 'r', encoding = "utf-8-sig") as file_saya:
    baca = csv.reader(file_saya, delimiter = ",")
    # print(baca)
    for i in baca:
        print(i)
'''
# jika membaca dengan format dictionaries
'''
import csv

with open('contoh3.csv', 'r', encoding = "utf-8-sig") as file_saya:
    baca = csv.DictReader(file_saya, delimiter = ",")
    # print(baca)
    for i in baca:
        print(dict(i))
'''

# Akses data dan ubah data csv
import csv
data_saya = []

with open('contoh3.csv', 'r', encoding = "utf-8-sig") as file_saya:
    baca = csv.DictReader(file_saya, delimiter = ",")
    # print(baca)
    for i in baca:
        data_saya.append(dict(i))

print(data_saya)