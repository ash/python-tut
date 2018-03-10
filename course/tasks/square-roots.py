import math

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

a2 = 2 * a
d = b ** 2 - 2 * a2 * c;

if d > 0:
    ds = math.sqrt(d)
    x1 = (ds - b) / a2
    x2 = - (ds + b) / a2
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))
elif d == 0:
    x = -b / a2
    print('x = ' + str(x))
else:
    print('No roots')