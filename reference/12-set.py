a = frozenset([1, 2, 3])
print(a)

#a.add(4)

b = {1, 2, 3}
b.add(4)
print(b)


s1 = {10, 20, 30, 40}
s2 = {20, 50}

s3 = s1 - s2
print(s3)

s4 = s1.difference(s2)
print(s4)