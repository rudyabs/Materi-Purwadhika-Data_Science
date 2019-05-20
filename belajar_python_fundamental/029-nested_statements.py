# python rules LEJB format

# built-in
help(len )

# Global
'''
name = 'String ini GLOBAL'

def greet():

    # Enclosing
    name = 'Rudy'

    def hello():
        # Local
        name = 'Saya LOCAL'
        print('Hello '+ name)
    
    hello()

greet()
'''

# =========================================

x = 50

def func():
    global x # fungsi akan mengambil x secara global -- tidak disarankan utk digunakan (gunakan return untuk mengganti variable global)
    print(f'X adalah {x}')

    # local reassignment untuk mempengaruhi global variable
    x = 'NILAI YANG BARU'    
    print(f'X GLOBAL diganti secara LOCAL menjadi {x}')


print(x)
func()
print(x)

# 