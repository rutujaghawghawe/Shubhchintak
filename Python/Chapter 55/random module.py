import random

laughs = ["Hi", "Ho", "He"]
random.shuffle(laughs)
print(laughs)
print(random.choice(laughs))
print(random.sample(laughs, 2))

print(random.randint(1, 8))
print(random.randrange(20, 50))