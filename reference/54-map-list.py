def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = map(lambda f: f(r), funcs)
    print(list(value))
