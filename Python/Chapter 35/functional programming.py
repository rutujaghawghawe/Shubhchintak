import functools

s=lambda x:x*x
print(s(2))

name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(list(name_lengths))

total = functools.reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total)

arr=[1,2,3,4,5,6]
print([i for i in filter(lambda x:x>4,arr)])