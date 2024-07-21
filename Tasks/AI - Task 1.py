# Question 1
# number1 = 42
# number2 = 10
# text1 = "Hello, world!"
# text2 = "Muhammad Taha"
# floating_point1 = 3.14
# floating_point2 = 4.98
# boolean1 = True
# boolean2 = False
# list_of_numbers = [1, 2, 3, 4, 5]
# dictionary = {"name": "Alice", "age": 30}
#
# print("Number:", number1)
# print("Number:", number2)
# print("Text:", text1)
# print("Text:", text2)
# print("Floating point:", floating_point1)
# print("Floating point:", floating_point2)
# print("Boolean:", boolean1)
# print("Boolean:", boolean2)
# print("List of numbers:", list_of_numbers)
# print("Dictionary:", dictionary)
#
# class = 15
# print(class)

# Question 2
# import keyword
# print(keyword.kwlist)

# Question 3
# int1 = 10
# int2 = 20
# int3 = 30
# int4 = 40
# int5 = 50
# print("Integer values are: {}, {}, {}, {}, {}".format(int1, int2, int3, int4, int5))
#
# city = "Islamabad"
# temperature = 22.02
# print("The Temperature in {} today is {} degrees outside!".format(city, temperature))

# Question 4
# This is a single-line comment
# It explains that the following line of code prints a message

"""
This is a multi-line comment.
It can span multiple lines.
It is typically used to provide detailed explanations or documentation.
The following lines of code assign values to variables.
"""

# Question 5
# a = 10
# b = 10
# c = 10
#
# print(id(a))
# print(id(b))
# print(id(c))

# Question 6
# a = 25
# b = 15.4
# c = "Taha"
# d = True
# e = 1+7j
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# Question 7
# a = 33.33
# b = 1+2j
#
# print(isinstance(a, float))
# print(isinstance(b, complex))

# Question 8
# str1 = "Python lab conduction"
# print(f"Memory address of {str1[0]} is {id(str1[0])}")
# print(f"Memory address of {str1[1]} is {id(str1[1])}")
# print(f"Memory address of {str1[2]} is {id(str1[2])}")
# print(f"Memory address of {str1[3]} is {id(str1[3])}")
# print(f"Memory address of {str1[4]} is {id(str1[4])}")
# print(f"Memory address of {str1[5]} is {id(str1[5])}")
# print(f"Memory address of {str1[6]} is {id(str1[6])}")
# print(f"Memory address of {str1[7]} is {id(str1[7])}")
# print(f"Memory address of {str1[8]} is {id(str1[8])}")
# print(f"Memory address of {str1[9]} is {id(str1[9])}")
# print(f"Memory address of {str1[10]} is {id(str1[10])}")
# print(f"Memory address of {str1[11]} is {id(str1[11])}")
# print(f"Memory address of {str1[12]} is {id(str1[12])}")
# print(f"Memory address of {str1[13]} is {id(str1[13])}")
# print(f"Memory address of {str1[14]} is {id(str1[14])}")
# print(f"Memory address of {str1[15]} is {id(str1[15])}")
# print(f"Memory address of {str1[16]} is {id(str1[16])}")
# print(f"Memory address of {str1[17]} is {id(str1[17])}")
# print(f"Memory address of {str1[18]} is {id(str1[18])}")
# print(f"Memory address of {str1[19]} is {id(str1[19])}")
# print(f"Memory address of {str1[20]} is {id(str1[20])}")

# Question 9
# L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# print(L[:])
# print(L[5:])
# print(L[:5])
# print(L[:-2])
# print(L[-7:-2])

# Question 10
# def addTwo (num1, num2):
#     addition = num1 + num2
#     subtraction = num1 - num2
#     multiplication = num1 * num2
#     division = num1 / num2
#     modulus = num1 % num2
#
#     print(f"Addition of {num1} and {num2} is: {addition}")
#     print(f"Subtraction of {num1} from {num2} is: {subtraction}")
#     print(f"Multiplication of {num1} and {num2} is: {multiplication}")
#     print(f"Division of {num1} by {num2} is: {division}")
#     print(f"Modulus of {num1} and {num2} is: {modulus}")
#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# addTwo(num1, num2)

# Question 11 (a)
# def interchange_first_last(list):
#     first = list[0]
#     last = list[-1]
#
#     list[0] = last
#     list[-1] = first
#
#     return list
#
# list1 = [1, 2, 3, 4, 5]
# print("Original list:", list1)
# print("List after interchanging first and last elements:", interchange_first_last(list1))

# Question 11 (b)
# list2 = [1, 2, 3, 4, 5]
# print("Sum of all elements in the list:", sum(list2))

# Question 11 (c)
# def calculate_mean(lst):
#     return sum(lst) / len(lst)
#
# def calculate_median(lst):
#     sorted_list = sorted(lst)
#     n = len(sorted_list)
#     mid = n // 2
#
#     if n % 2 == 0:
#         median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
#     else:
#         median = sorted_list[mid]
#
#     return median
#
# list3 = [1, 2, 3, 4, 5]
# print("Mean of the list:", calculate_mean(list3))
# print("Median of the list:", calculate_median(list3))

# Question 12
# list4 = [1, 2, 3, 4, 5]
# sqrList4 = [x**2 for x in list4]
# print(sqrList4)

# Question 13
# list5 = [1, 2, 3, 4, 5]
# sqrList5 = [x**3 for x in list5]
# print(sqrList5)

# Question 14
# list6 = [23, 45, 12, 68, 41, 10]
# element = 68
# found = element in list6
#
# if found:
#     print(element, " is found at index: ", list6.index(element))
# else:
#     print(element, " is not found")