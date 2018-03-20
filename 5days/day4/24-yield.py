def counter():
    for i in range(1000):
        yield i

g = counter()
print(next(g))
print(next(g))
print(next(g))

g2 = counter()
print(next(g2))
print(next(g2))
print(next(g2))

print(next(g))
print(next(g))

print(next(g2))
