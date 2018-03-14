f = open('2.txt')
s = f.read()
f.close()

n = {}
for c in s:    
    if c == '\n':
        continue

    if n.get(c) != None:
        n[c] += 1
    else:
        n[c] = 1

print(n)
