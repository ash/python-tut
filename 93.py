# exctact data with re
# capturing

import re

e = 'write to JOHN@example.com please'

r = re.search(
    '([0-9_.a-z-]+)@([0-9_.a-z-]+\.[a-z]{2,})',
    e, flags = re.I) # case-insensitive
if r:
    print('E-mail OK')
else:
    print('Wrong e-mail')

print(r[0]) # john@example.com
print(r[1]) # JOHN
print(r[2]) # example.com
