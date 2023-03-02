foo = 1
bar = 'bar'
baz = 3.14

print('{0}, {1}, {2}, and {1}'.format(foo, bar, baz))

print("X value is: {x_val}. Y value is: {y_val}.".format(x_val=2, y_val=3))

my_dict = {'key': 6, 'other_key': 7}
print("My other key is: {0[other_key]}".format(my_dict))

my_list = ['zero', 'one', 'two']
print("2nd element is: {0[2]}".format(my_list))

t = (12, 45, 22222, 103, 6)
print('{0} {2} {1} {2} {3} {2} {4} {2}'.format(*t))

print('{0:.3f}'.format(42.12345))

print('{first} {last}'.format(first='Hodor', last='Hodor!'))