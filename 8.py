# strings

s = "double quotes"
s = 'single quotes'

s = "O'Reilly"

s = 'O\'Reilly'
print(s)

# \n new line
print("a\nb")

# \t tab
print("a\tb")

m = "string that \
continues on another \
line"
print(m)

n = '''multi-line
string that can
continue on other lines'''
print(n)


# tabs
print("Name\tQuant\tPrice\tTotal")
print("Book\t1\t2.50\t2.50")
print("Orange\t10\t0.50\t5.00")

# see https://pyformat.info/
print('%10.2f %10.2f %10.2f' % (3.0, 4.5, 10.2))
print('%10.2f %10.2f %10.2f' % (1343.0, 4, 10.2))

print('%10.2f' % (10.1 + 10.2))
