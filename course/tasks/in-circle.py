x = float(input('x: '))
y = float(input('y: '))
r = float(input('r: '))

if x ** 2 + y ** 2 <= r ** 2:
    print('Belongs')
else:
    print('Outside')


print('Yes' if x ** 2 + y ** 2 <= r ** 2 else 'No')

result = ('-', '+')[x ** 2 + y ** 2 <= r ** 2]
print(result)