x = float(input('x: '))
y = float(input('y: '))

if x > 0:
    if y > 0:
        print('I')
    elif y < 0:
        print('II')
    else:
        print('Axis X')
elif x < 0:
    if y > 0:
        print('IV')
    elif y < 0:
        print('III')
    else:
        print('Axis -X')
else:
    if y > 0:
        print('Axis Y')
    elif y < 0:
        pint('Axis -Y')
    else:
        print('(0, 0)')
    