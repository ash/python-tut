n = int(input('Enter number: '))

if n < 0:
    print('Negative number')
elif n > 0:
    print('Positive number')
else:
    print('Zero')

n = abs(n)
if n < 10:
    print('One-digit number')
elif n < 100:
    print('Two-digit number')
else:
    print('Three digits or more')
