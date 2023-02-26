print({1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})) 
print({1, 2, 3, 4, 5} & {3, 4, 5, 6})

print({1, 2, 3, 4, 5}.union({3, 4, 5, 6})) 
print({1, 2, 3, 4, 5} & {3, 4, 5, 6})

print({1, 2, 3, 4, 5}.difference({3, 4, 5, 6})) 
print({1, 2, 3, 4, 5} & {3, 4, 5, 6})

print({1, 2, 3, 4, 5}.symmetric_difference({3, 4, 5, 6})) 
print({1, 2, 3, 4, 5} & {3, 4, 5, 6})

s = {1,2,3}
s.add(4)
print(s)
s.discard(3)
print(s)

restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)
print(list(unique_restaurants))
