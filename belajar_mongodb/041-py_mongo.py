# mengecek apakah sudah connect database (cek fitur mongo)
from pymongo import MongoClient


# cek path server
x = MongoClient('mongodb://localhost:27017/') # alternatif: dengan langsung import mongoclient

# menentukan database dan collection
db = x["belajar_mongo"]
col = db["produk"]

# mencari data tertentu (harga > 1000000)
cari = {"harga": {"$gt": 10000000}}
cari_2 = {'nama': 'headset'}


# memasukan data
nama = input('Ketik nama produk: ')
harga = input('Ketik harga produk: ')

data = {'nama': nama, 'harga': int(harga)} # belum dinamis
z = col.insert_one(data)
print(z.inserted_id)

# cek data sudah masuk atau belum
for i in col.find({'_id': z.inserted_id}):
    print('Data tersimpan!')
    print(i)

# print(list(col.find()))

# melihat list database
# print(x.list_database_names())

# melihat semua data di collection
# for x in col.find():
#     print(x)

# melihat data dengan parameter tertentu
# for x in col.find(cari):
#     print(x)

# for x in col.find(cari_2):
#     print(x)

