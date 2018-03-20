import time

s = 0

t0 = time.time()

def f():
    # global s
    s = 0
    # s = sum(range(10_000_000))
    for i in range(10_000_000):
        s += i
    return s

s = f()
print(s)

print(time.time() - t0)

# Also for classes