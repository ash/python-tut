import re

for i in range(32, 10_000):
    ch = chr(i)
    if re.match('\d', ch, re.ASCII):
        print(ch, end='')
print('')

for i in range(32, 10_000):
    ch = chr(i)
    if re.match('[$.0-9A-Za-z[]', ch, re.ASCII):
        print(ch, end='')
print('')

for i in range(32, 256):
    ch = chr(i)
    if re.match('[^a-zA-Z]', ch):
        print(ch, end='')
print('')
