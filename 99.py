print(4 is 4)
print(4 == 4)

print(4 is 5)
print(4 == 5)

x = 4
y = 4
print(x == y) # True
print(x is y) # True

a = []
b = []
print(a == b) # True
print(a is b) # False

c = a
print(a is c) # True

c.append(42)
print(a)


def f(a): # by reference
    a[0] = 5

v = [1, 2, 3]
f(v)
print(v)

def g(x): # by value
    x = 5

z = 3
g(z)
print(z)
