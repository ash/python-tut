# 10 unique random ints between 0 and 20, variant 1 - using single loop

import random

seen = []

while len(seen) != 10:
    r = random.randint(0, 20)
    if r in seen:
        continue
    seen.append(r)
    print(r)
