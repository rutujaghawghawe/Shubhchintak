thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist)

print(len(thislist))

print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

thislist.insert(2, "guava")
print(thislist)

thislist.append("papaya")
print(thislist)

thislist.remove("watermelon")
print(thislist)

thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist.sort()
print(thislist)

thislist.reverse()
print(thislist)