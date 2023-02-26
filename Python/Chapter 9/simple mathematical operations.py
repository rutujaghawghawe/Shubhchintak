import operator 
import math

a, b, c = 3, 2, 10

print(a+b)
print(operator.add(a, b))

print(a-b)
print(operator.sub(a, b))

print(a*b)
print(operator.mul(a, b))

print(a/b)
print(operator.__truediv__(a, b))
print(operator.floordiv(a, b))

print(c%a)
print(operator.mod(c, a))

print(a**b)
print(operator.pow(a,b))
print(pow(a,b,a))

