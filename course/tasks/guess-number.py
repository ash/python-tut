n = int(input('Enter you secret number: '))

g = int(input('Your guess: '))
while n != g:
    if n < g:
        print('Your number is too big')
    elif n > g:
        print('Your number is too small')
    
    g = int(input('Your guess: '))

print('Yes! This was ' + str(n))
