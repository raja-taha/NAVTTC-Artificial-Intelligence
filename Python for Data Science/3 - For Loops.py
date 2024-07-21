fruits = ['banana', 'apple', 'pear', 'pineapple', 'orange']

for fruit in fruits:
    print(fruit)

string = 'banana'
for char in string:
    print(char)

for fruit in fruits:
    for char in fruit:
        print(char)

for i in range(5,10):
    print(i)

for i in range(10):
    for j in range(11, 20):
        print(i, " + ", j, " = ", i+j )