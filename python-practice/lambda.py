from functools import reduce


def squared(num): return num * num
# lambda squared = lambda num: num * num


print(squared(5))


def addtwo(x): return x + 3
# lambda addtwo = lambda x: x + 3


print(addtwo(5))


def sum(x, y): return x + y
# sum = lambda x, y: x + y


print(sum(6, 3))
print((lambda x, y: x + y)(0, 9))

#############################


def funcBuilder(x):
    return lambda y: x + y


add2 = funcBuilder(2)
add9 = funcBuilder(9)

print(add2(3))
print(add9(8))
print(funcBuilder(3)(5))

#########################

nums = [2, 3, 6, 9, 12, 13]
squared_nums = map(lambda x: x * x, nums)
print(list(squared_nums))

###############################

odd_nums = filter(lambda x: x % 2 != 0, nums)
print(list(odd_nums))

#############################


sum_all = reduce(lambda acc, curr: acc + curr, nums)
print(sum_all)

########################

lambda acc, curr: acc + len(curr)

names = ['Alice', 'Bob', 'Charlie', 'David']
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
#########################

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Sorted by second element of each tuple

#########################

points = [(1, 2), (3, 1), (0, 0), (2, 2)]
points.sort(key=lambda point: point[0]**2 + point[1]**2)
print(points)  # Sorted by distance from origin
