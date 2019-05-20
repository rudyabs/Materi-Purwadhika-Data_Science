# method yaitu function yang dibuat dalam built-in objects
# lihat dokumentasi, FAQs, whats new, dan library reference  di python
# library reference

mylist = [1,2,3,]

# contoh method
print(mylist.pop())

# melihat dokumentasi dari built-in object
help(mylist.insert)

# function membuat kita dapat membuat sekumpulan code yang dapat dijalankan berkali-kali, tanpa harus menulis ulang code tersebut
# tujuan dari function yaitu membuat code berulang yang besih  

# struktur function:
a = 'Budi'

def name_of_function(a): # disarankan menggunakan huruf kecil dan underscore untuk memisahkan kata
    '''
    docstring yang menjelaskan function
    '''
    print('Hello' + " " + a)

# function dapat menjalankan perimeter

name_of_function(a)

# menggunakan return keyword untuk menirim kembali hasil dari function
# return dapat menetapkan output dari function ke variable baru

def add_function(num1,num2):
    return num1+num2

result = add_function(1,2)
print(result)

# contoh dari function
def name_function():
    '''
    DOCSTRING: Information about the function 
    INPUT: no input
    OUTPUT: Hello
    '''
    print('hello')

# function dengan default argumen
def say_hello(name='NAME'): #saat argumen tidak deberikan, maka akan memberikan default 'Name'
    print('hello'+ name)

say_hello()

# contoh: pig latin function
# jika huruf depan menggunakan huruf vokal, tambah 'ay' diakhir kata
# jika kata dengan huruf awal tidak dengan huruf vokal, maka pindahkan huruf pertama ke terakhir dan tambah 'ay'

word = input('Masuka kata = ')
def pig_latin(word):
    huruf_pertama = word[0]
    if huruf_pertama in 'aiueo':
        x = word + 'ay'
    else: 
        x = word[1:] + huruf_pertama + 'ay'
    return print(x)

pig_latin(word)

