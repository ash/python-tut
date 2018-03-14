a = [10, 2, 3, 5, 7, 1, 4]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

b = [10, 2, 3, 5, 7, 1, 4]
print(sorted(b))
print(b)

c = ['alpha', 'Beta', 'Gamma', 'delta']
c.sort()
print(c)

c.sort(key=str.lower)
print(c)

