import cmath

z = 2+3j

print(cmath.phase(z))
print(cmath.polar(z))
print(cmath.rect(2, cmath.pi/2))

print(cmath.exp(z))
print(cmath.log(z))
print(cmath.sqrt(z))

print(cmath.sin(z))
print(cmath.asin(z))
print(cmath.sinh(z))
print(cmath.tanh(z))
print(cmath.acosh(z))
print(cmath.cosh(z)**2 - cmath.sin(z)**2)
print(cmath.cosh((0+1j)*z) - cmath.cos(z))
