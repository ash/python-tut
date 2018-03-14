a = {}
print(a)

b = {'a': 1, 'b': 'c'}
print(b)

c = dict(k1='v1', k2=[1, 2, 3])
print(c)

d = dict([[1, 2], ['a', 'b'], ['c', 5]])
print(d)

e = {'a': 'alpha', 'b': 'beta', 'c': 'gamma', 'd': 'delta'}
print(e)
e.pop('b')
print(e)

e.popitem()
print(e)

print(e.setdefault('Q', '123'))
print(e)


f = {1: 2, 3: 4}
g = {1: 5, 7: 8}
f.update(g)
print(f)

print(1 in f)
print(1 in f.keys())
print(8 in f.values())
print((1, 5) in f.items())