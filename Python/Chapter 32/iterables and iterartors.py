s = {1, 2, 3} 
i = iter(s) 
a = next(i) 
b = next(i)
c = next(i)
print(a,b,c)

l1 = list(s)
l2 = [a * 2 for a in s if a > 2]
print(l2)