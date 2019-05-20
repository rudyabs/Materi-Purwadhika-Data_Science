# set -> koleksi elemen "unik" yang tidak berurutan
# set {1, 2, 3}

data_set = set()
data_set.add(1)
data_set.add(1)
data_set.add(3)
data_set.add(2)
print(data_set)
print(type(data_set))

# print(data_set[0]) #tidak bisa karena 'set' tidak mengenal indexing
