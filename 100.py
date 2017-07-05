# return vs yield

def f():
    for i in range(1, 5):
        print("value=" + str(i))
        return i

def g():
    for i in range(1, 5):
        print("value=" + str(i))
        yield i

f()
f()
f()

gen = g()
next(gen)
next(gen)
next(gen)
