number = 10

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

number2 = 11
if number2 > 0:
    if number2 % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
elif number2 < 0:
    print("Number is negative")
else:
    print("Number is zero")

age = 20
income = 1000
if age >=18 and income >=5000:
    print("Buy a Car")
else:
    print("Don't buy a Car")

for number in range(5, 10):
    if number >=5:
        print(number)
        break