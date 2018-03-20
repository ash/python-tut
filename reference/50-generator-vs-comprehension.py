def f(x):
    print("f(%i)" % x)
    return x**2

l = [f(x) for x in range(10)]
print(l[0])
print(l[1])
print(l[2])


g = (f(x) for x in range(10))
print(next(g))
print(next(g))
print(next(g))
