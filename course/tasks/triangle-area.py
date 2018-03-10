import math

a = float(input('Side 1: '))
b = float(input('Side 2: '))

c = math.sqrt(a ** 2 + b ** 2)

p = a + b + c
s = a * b / 2

print('Perimeter = ' + str(p))
print('Area = ' + str(s))
