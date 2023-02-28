from random import randrange

squares = [x * x for x in (1, 2, 3, 4)]
print(squares)

print([s.upper() for s in "Hello World"])

print([x if x in 'aeiou' else '*' for x in 'apple'])

print([sorted(x) for x in [[2, 1], [4, 3], [0, 1]]])

print([randrange(1, 7) for x in range(10)])

print([x if x % 2 == 0 else None for x in range(10)])

print([x if (x > 2 and x % 2 == 0) else '*' for x in range(10)])

print(dict((x, x * x) for x in (1, 2, 3, 4)))

data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element in each_list]
print(output)

print({x for x in range(1, 11) if x % 2 == 0})
