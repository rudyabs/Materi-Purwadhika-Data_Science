mystring = 'hello'
mylist =[]

for letter in mystring:
    mylist.append(letter)

print(mylist)

# bisa digantikan dengan
mylist =  [letter for letter in mystring]

print(mylist)

angka = [num for num in range(0, 11)]
print(angka)

angka = [num**2 for num in range(0, 11)]
print(angka)

angka_genap = [x for x in range(0,11) if x%2==0]
print(angka_genap)

# ================================ 

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp +32) for temp in celcius]
print(fahrenheit)

fahrenheit_2 = []
# dimana sama saja dengan menggunakan
for temp in celcius:
    fahrenheit_2.append((9/5)*temp + 32)

print(fahrenheit_2)

# ================================ 
daftar_angka=[]

for x in [2,4,6]:
    for y in [1,10,1000]:
        daftar_angka.append(x*y)

print(daftar_angka)