# 10 unique random ints between 0 and 20

import random

seen = dict()

for i in range(10):
    r = random.randint(0, 20)
    while r in seen:
        r = random.randint(0, 20)
    seen[r] = 1
    print(r)
