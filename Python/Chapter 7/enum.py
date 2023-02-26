from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3

print(Color.red) 
print(Color(2))
print(Color['red'])

print([c for c in Color])