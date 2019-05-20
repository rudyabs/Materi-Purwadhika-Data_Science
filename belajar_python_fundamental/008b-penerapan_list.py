# list

'''
contoh list
matkul = ['Kalkulus', 'Astronomi', 'Elektronika']
genap = [0, 2, 4, 6, 8, 10, 12]
ganjil = [1.0, 3.0, 5.0]
boolean = [True, False]
campur = ['Andi', 21, 'Budi', 22]
'''
# =========================================================
'''
x = 0
y = 1
z = 2
xyz = [x, y, z, 3, 4, 5, 6, 7, 8]

print(xyz)
# print(len(xyz))
print(xyz[0])
print(xyz[1])
print(xyz[2])
print(xyz[len(xyz)-1])
print(xyz[-1])

print(xyz[0:3]) # start : end
print(xyz[0:8:2]) # start : end : step
print(xyz[0::2]) # start : until the end : end
print(xyz[::2]) # genap
print(xyz[1::2]) # ganjil
'''

# =========================================================

'''
students = ['Andi', 'Budi', 'Caca', 'Deni', 'Ela']
new_students = ['Fifi', 'Gandi', 'Hari']
additional_students = 'Ina'

# print(students.index('Caca'))
# print(students.count('Budi'))

students.extend(new_students)
print(students)

# students.append(new_students)
# print(students)
# print(students[-1][0])

students.insert(3, 'Zaza')
print(students)

students.remove('Andi')
print(students)

# students.clear() #menghapus semua list
# print(students)

students.pop() #menghapus element terakhir list
students.pop(2) #menghapus element index ke-x
print(students)

students.sort() #sort by alphabet
students.reverse() # reverse by index
print(students)
'''

# =========================================================

'''
angka = [14, 1, 34, 122, 67, 22]
x = angka[0:3]
x.sort()
print(angka)
print(x)

angka[0:3] = x # bisa juga menggunakan angka[0:len(x)] = x
print(angka)
'''
