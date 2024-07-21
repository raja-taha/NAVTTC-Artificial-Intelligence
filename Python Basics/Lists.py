list0 = []
list1 = ['one', 'two', 'three', 'four']
list2 = ['1', '2', '3', '4']
list3 = [[1, 2], [3, 4]]
list4 = [1, 'Alex', 12, 1.5]

print(len(list1))

list1.append('five')
print(list1)

list1.insert(2, 'three')
print(list1)

list1.remove('four')
print(list1)

list1.append(list4)
print(list1)

list2.extend(list4)
print(list2)

del(list4[0])
print(list4)

list6 = ['5', '6', '7', '8', '9']
list6.reverse()
print(list6)

numbers = [67, 89, 45, 32, 12, 6, 4, 9, 0]
sorted_list = sorted(numbers)
print(sorted_list)

print("Reverse sorted list", sorted(numbers, reverse=True))

list7 = "one, two, three, four, five"
spl = list7.split(',')
print(spl)

list8 = "A lab is being conducted"
spl1 = list8.split()
print(spl1)

list9 = [78, 89, 56, 77, 66, 45, 33, 21]
print(list9[3])
print(list9[-2])
print(list9[:])
print(list9[:4])
print(list9[4:])
print(list9[2:6])
print(list9[::2])
print(list9[2::2])

list10 = [1, 2, 3, 4]
list11 = ['Alex', 'John', 'Harry']
list12 = list10 + list11
print(list12)

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

print(sum_list([1, 2, -8]))

# Mean
n_num =[1, 2, 3, 4, 5]
n = len(n_num)

get_sum = sum(n_num)
mean = get_sum / n

print("Mean / Average is : " + str(mean))

# Median
n_num.sort()

if n % 2 == 0:
    median = (n_num[n//2] + n_num[n//2 - 1 ]) / 2
else:
    median = n_num[n//2]

print("Median is : " + str(median))