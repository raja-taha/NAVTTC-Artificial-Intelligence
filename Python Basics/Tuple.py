tuple1 = (10, 10, 55.55, 0, 'apple', 'cherry')
print(tuple1)

# tuple1[2] = 3

print(tuple1.index(10))

indices = [i for i, x in enumerate(tuple1) if x == 10]
print(indices)

tuple2 = (1, 2, 3, 4)
tuple3 = (5, 6, 7, 8)
tuple4 = tuple2 + tuple3
print(tuple4)

tuple5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
print(tuple5[:])
print(tuple5[:4])
print(tuple5[4:])
print(tuple5[4::2])
print(tuple5[::-1])
