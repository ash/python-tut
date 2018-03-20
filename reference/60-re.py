import re

s = "Abcda"
r = re.match(r'abcd', s, re.IGNORECASE)
if r:
    print('Yes')


r = re.search(r'((c)(d))', s)
if r:
    print('Found')
    print(r.groups())
    print(r.group(3))
    print(r.start())
    print(r.end())
    print(r.span())    

r = re.findall(r'\w', s)
print(r)

r = re.finditer(r'[a-z]', s)
for x in r:
    print(x.group())


x = re.compile(r'''
    (.)(.)
''', re.VERBOSE)
r = x.findall(s)
print(r)

d = re.match(r'(?P<y>\d+)-(?P<m>\d+)-(?P<d>\d+)', '2018-03-20')
print(d.groupdict())

if re.match(r'(\d)-\1', '2-2'):
    print('2-2')    


n = re.split(r';', '1;3;5;7')
print(n)

r = re.sub(r'1', 'one', '123145')
print(r)

r = re.compile(r'(\d+)-(\d+)')
m = r.match('10-11')
x = m.expand(r'\2-\1')
print(x)