# # *args = arguments
# # **kwargs = keyword arguments
# # predefined perimeter

# # 
# # jika ada function seperti ini
# def myfunc(a, b):
#     # return 5% dari jumlah a dan b
#     return sum((a,b))*0.05

# print(myfunc(40,60))
# # bagaimana jika ada perimeter tambahan yang lain 
# # contoh dengan 4 argumen
# def myfunc2(a, b, c=0, d=0):
#     # return 5% dari jumlah a dan b
#     return sum((a,b))*0.05
# # *args memasukan jumlah argumen yang diinginkan 
# def myfunc_args(*args):
#     return sum(args) * 0.05

# print(myfunc_args(10,20,30,50,100,250,1000))

# # contoh : args menghasilkan tuple
# def haha(*args):
#     print(arg) 
#     for item in args:
#         print(item)

# print(haha(1,2,3,4,5,6,7,8))

# ================================================
# # **kwargs 
# def myfunc(**kwargs):
#     print(kwargs) # menghasilkan dictionary
#     if 'buah' in kwargs:
#         print('Buah pilihan saya yaitu {}'.format(kwargs['buah']))
#     else:
#         print('Saya tidak menemukan buah pilihan saya')

# myfunc(buah='pisang')

# ================================================
# kombinasi
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('Saya mau makan {} {}'.format(args[0],kwargs['makanan']))

myfunc(10,20,30,buah='apel', makanan='telur',binatang='kucing')
