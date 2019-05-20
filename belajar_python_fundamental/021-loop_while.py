# looping

# angka = 1
# while angka <= 10:
#     print('HAHAHA ke-', angka)
#     angka += 1

# angka = (0,1,2,3,4,5,6,7,8,9)
# i = 0
# while i <= len(angka)-1:
#     print(angka[i])
#     i += 1


# angka = [0,1,2,3,4,5,6,7,8,9]
# angka2 = []
# i = 0
# while i <= len(angka)-1:
#     angka2.append(angka[i] * 2)
#     i += 1

# print(angka)
# print(angka2)

# break
# i = 0
# while i < 6:
#     print(i)
#     if i == 4:
#         break
#     i += 1

i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)