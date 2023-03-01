t = ('a', 'b', 'c', 'd', 'e')
print(t)

tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
tuple3 = ('a', 'b', 'c', 'd', 'e')

print(len(tuple1))
print(max(tuple1))
print(min(tuple2))

list = [1,2,3,4,5]
print(tuple(list))
print(list)

print(tuple1 + tuple2)

colors = "red", "green", "blue"
rev = colors[::-1]
colors = rev
print(colors)