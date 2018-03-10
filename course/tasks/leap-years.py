year = int(input('Enter year: '))

if year % 4:
    print('Common')
elif year % 100:
    print('Leap')
elif year % 400:
    print('Common')
else:
    print('Leap')
