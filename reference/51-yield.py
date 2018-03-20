def f():
    for i in range(10):
        print("returning %i**2" % i)
        yield i ** 2


g1 = f()
g2 = f()
print(next(g1))
print(next(g1))
print(next(g1))

print(next(g2))
print(next(g2))

print(next(g1))
