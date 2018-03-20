import math
#from math import sqrt
import time

t0 = time.time();
for i in range(10_000_000):
    math.sqrt(i)
print(time.time() - t0)
