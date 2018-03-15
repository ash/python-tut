f = open('data.txt', 'r')
print('pos', f.tell())
f.seek(5)
print('pos', f.tell())
data = f.read(1)
print(data)

print('isatty', f.isatty())
print('fileno', f.fileno())
f.close()

print(f.encoding)