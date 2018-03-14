import re

f = open('3.txt')
s = f.read()
f.close()

print(re.findall(r'[^A-Z]([A-Z]{3}[a-z][A-Z]{3})[^A-Z]', s))