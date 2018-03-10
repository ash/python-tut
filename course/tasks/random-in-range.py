import random

a = float(input('Begin: '))
b = float(input('End: '))

#r = random.random() * (b - a) + a
r = random.uniform(a, b)

#r = random.randrange(a, b)
print(r)
