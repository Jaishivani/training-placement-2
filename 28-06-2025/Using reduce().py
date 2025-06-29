from functools import reduce

li = [1, 3, 4, 5, 7]
li = reduce(lambda x, y: [6] + x + y, [[], li])
print(li)
