print("This string will be displayed in the output")
print("You can print \n escape characters too.")

with open('shoppinglist.txt', 'w') as fileobj:
    fileobj.write('tomato\npasta\ngarlic')

with open('shoppinglist.txt', 'r') as fp:
    for line in fp:
        print(line)