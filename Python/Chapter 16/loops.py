i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1

for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)

for i in range(1, 5):
    if (i == 2):
        print(i)
    print(i)
print(5)

for x in ['one', 'two', 'three', 'four']:
    print(x)

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')