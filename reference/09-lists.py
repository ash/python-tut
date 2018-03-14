a = []
print(a)

b = [1, 2, [3, 4]]
print(b)

c = [1, 'one']
print(c)

d = list((1, 2, 3))
print(d)

d.append(4)
print(d)

e = [1, 2]
f = (3, 4)
e.append(f)
print(e)

e = [1, 2]
e.extend(f)
print(e)

e.reverse()
print(e)

print(e.index(2))


g = [1, 2, 3, 1, 4, 5]
g.remove(1)
print(g)

del g[2]
print(g)

h = [1, 2, 3, 4, 5, 6, 7]
print(h.pop())
print(h)
print(h.pop(2))
print(h)

print(3 in h)
print(8 not in h)

h.clear()
print(h)
