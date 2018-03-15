# lists vs tuples vs sets

l = [1, 2, 3]
t = (1, 2, 3)
s = {1, 2, 3}

l[1] = 7
l.append(8)
l.append(8)
print(l)

print(t[1])
#t[1] = 7
#t.append(8)
print(t)

#print(s[1])
s.add(4)
s.add(4)
print(s)