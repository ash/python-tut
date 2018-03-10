n = int(input('Your number between 100 and 999: '))

s = n // 100
n = n % 100

s = s + n // 10
n = n % 10

s = s + n

print('Sum of digits = ' + str(s))
