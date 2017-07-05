# regular expressions
# regex / regexp
# re

import re

e = 'john@example.com'

# ^, $ = anchors
# [] = character class
# +, *, ?, {2,} = quantifiers
# \. = meta-character
# . = any character

# [a-z] = [abcde.....xyz]
# [0-9a-z] = [0123456789abcde.....xyz]
# [0-9a-z-] = [0123456789abcde.....xyz-]

r = re.search(
    '^[0-9_.a-z-]+@[0-9_.a-z-]+\.[a-z]{2,}$',
    e)
if r:
    print('E-mail OK')
else:
    print('Wrong e-mail')

# print(r[1])
# if r[1] == 'example.com':
#     print('Domain accepted')
# print(r)
# if r:
#     print(r.groups())


# flags = re.I