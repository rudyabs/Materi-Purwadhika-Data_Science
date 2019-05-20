# syntax while loop
'''
while some_boolean_condition:
    # do something
else:
    # do something else

'''
x = 50
while x < 5:
    print(f'Posisi X berada di = {x}')
    x = x + 1
else:
    print("X tidak kurang dari 5")

# keyword: break, continue, pass
# break: break out current closest enclosing loop
# continue: Goes to the top of the closest enclosing loop
# pass: does nothing at all

# pass berguna saat ingin menghindari error
y = [1,2,3]
for item in y:
    # comment
    pass

# continue
nama = 'Bamboe'
for huruf in nama:
    if huruf == "a":
        continue
    print(huruf)

# break
nama = 'Bamboe'
for huruf in nama:
    if huruf == "a":
        break
    print(huruf)

z = 0
while z < 5:
    if x == 2:
        break
    print(x)
    x += 1
