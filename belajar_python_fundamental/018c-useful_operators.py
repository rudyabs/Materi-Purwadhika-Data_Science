# range
# mylist = [1,2,3,4]

# for num in range(0,11,2):
#     print(num)

# print(list(range(0,11,2)))
# =================================

# enumerate
# index_count = 0
# for huruf in 'abcde':
#     print('At index {} the letter is {}'.format(index_count, huruf))
#     index_count+=1

# word = "abcde"
# for item in enumerate(word):
    # print(item)
# =================================

# zip
# mylist1 = [1,2,3]
# mylist2 = ['a','b','c']

# for item in zip(mylist1, mylist2):
#     print(item)
    
# print(list(zip(mylist1, mylist2)))

# print("x" in ["x","y","z"])
# print("x" in [1,2,3])
# print('a' in 'Bank')
# print('mykey' in {'mykey':1})

# d = {'key1':100}
# print(100 in d.keys())
# print(100 in d.values())

# =================================
# shuffle function
from random import shuffle, randint
mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)

# randint function
print(randint(0,100))
nomor_keberuntungan = randint(0,100)

