# generators

def f():
    for i in range(2, 100):
        # print(i)
        # return i
        yield i

g = f() # generator object

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
