import math
import time

t0 = time.time();
f = math.sqrt
for i in range(10_000_000):
    f(i)
print(time.time() - t0)
