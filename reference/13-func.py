def f():
    '''This is a function. Its name is "f".
    It takes no arguments'''
    return 10

f()
#print(help(f))


def g(x, y):
    print('x=' + str(x))
    print('y=' + str(y))

g('a', 'b')
g(x='a', y='b')
g(y='a', x='b')


def h(x=42):
    print(x)

h(10)
h()


def n(m):
    print(type(m))
    print(m[1])
    m[0] = 7

lst = [1,2,3]
n(lst)
print(lst)

lst2 = [4,5,6]
n(lst2[:])
print(lst2)


def func(x):
    x = 2 * x

val = 10
func(val)
print(val)


def arb(*x):
    print(type(x))
    print(x)

arb(1, 2, 3)


def arbkw(**x):
    print(type(x))
    print(x)

arbkw(a=1, b=2)
