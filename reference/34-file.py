f = open('f.txt', 'w')
print('mode', f.mode)
print('closed?', f.closed)
f.close()
print('closed?', f.closed)
print('name', f.name)
