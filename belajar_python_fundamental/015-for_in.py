# # 'in' untuk mengetahui jika terdapat data dalam ...

# data_set = {1, 2, 3}
# data_list = [1, 2, 3]
# data_tuple = (1, 2, 3)

# print(2 in data_set)
# print(2 in data_list)
# print(2 in data_tuple)

# # eksperimen dengan data dalam tuple
# print(data_tuple[0:2:1])
# print(data_tuple + data_tuple)
# print(data_tuple * 3)

data_st = {'Andi', 'Budi', 'Cacad'}

for elemen in data_st:
    print(elemen)

# data_st.add('Doni')
# print(data_st)

# untuk menambahkan dan mengupdate element
print(data_st)
data_st.add('Don')
print(data_st)
data_st.update(['Ela', 'Firdo'])
print(data_st)
data_st.update({'Gidi', 'Hani'})
print(data_st)

# untuk menghapus element
data_st.remove('Firdo')
print(data_st)
data_st.discard('Don')
print(data_st)
data_st.discard('Xonk')
print(data_st)
# data_st.remove('Bonk')

print(data_st)

# data_st.clear()
# print(data_st)
del data_st
print(data_st)