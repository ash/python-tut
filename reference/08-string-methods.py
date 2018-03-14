print('abc def'.capitalize())

print('Straße'.casefold())
print('strasse'.casefold())

print('abc'.center(10))
print('abc'.center(10, '*'))

print('abcdeabcabc'.count('a'))
print('abcdeabcabc'.count('a', 3))
print('abcdeabcabc'.count('a', 4, 8))

print('Zürich'.encode(encoding='utf-8'))
print('Zürich'.encode(encoding='latin-1'))

print('abc'.endswith('c'))
print('abc'.endswith('c', 1))
print('abc'.endswith('b', 0, 2))

print('abc'.endswith(('b', 'c')))
print('abc'.endswith(('b', 'd')))

print('1\t2'.expandtabs(4))
print('1\t2'.expandtabs(8))

print('abcde'.index('c'))
#print('abcde'.index('f'))

print('½'.isalpha())
print('½'.isnumeric())

print(':'.join(['a','b','c']))

print('AbC'.swapcase())

print('abc'.maketrans('abcdef', 'xyz123'))

print('abcdef'.partition('c'))

print('abcabc'.replace('a', 'x'))
print('abcabc'.replace('a', 'x', 1))


print('one two three'.split())
print('one,two,three'.split(','))
print('one,two,three'.split(',', maxsplit=1))

print('abc'.zfill(5))