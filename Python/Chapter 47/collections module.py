import collections

counts = collections.Counter([1,2,3])
print(counts)

print(collections.Counter('Happy Birthday'))

print(collections.Counter('I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-Iam'.split()))

d = collections.OrderedDict([('foo', 5), ('bar', 6), ('baz', 7)])
d['foobar'] = 8
print(d)

s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]
dd = collections.defaultdict(list)
for k, v in s:
    dd[k].append(v)
print(dd)

Human = collections.namedtuple('Person', 'age, height, name')
dave = Human(30, 178, 'Dave')
print(dave)
print(dave.age)

dict1 = {'apple': 1, 'banana': 2}
dict2 = {'coconut': 1, 'date': 1, 'apple': 3}
combined_dict = collections.ChainMap(dict1, dict2)
reverse_ordered_dict = collections.ChainMap(dict2, dict1)

for k, v in combined_dict.items():
    print(k, v)
    
for k, v in reverse_ordered_dict.items():
    print(k, v)    