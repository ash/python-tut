max = None
for i in range(1, 11):
    n = int(input('Value ' + str(i) + ': '))
    if max == None:
        max = n
    elif n > max:
        max = n

print('Maximum is ' + str(max))
