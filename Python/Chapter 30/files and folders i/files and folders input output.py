with open('shoppinglist.txt', 'w') as fileobj:
    fileobj.write('tomato\npasta\ngarlic')

with open('shoppinglist.txt', 'r') as fp:
    for line in fp:
        print(line)

with open("shoppinglist.txt", "r") as fp:
    lines = fp.readlines()
for i in range(len(lines)):
    print("Line " + str(i) + ": " + line) 

with open('shoppinglist.txt') as in_file:
    content = in_file.read()
print(content)           

with open('myfile.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    f.write("Line 4\n")

with open('my_file.txt', 'w', encoding='utf-8') as f:
    f.write('utf-8 text')   

with open('fred.txt', 'w') as outfile:
    s = "I'm Not Dead Yet!"
    print(s) 
    print(s, file = outfile)     