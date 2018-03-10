max = int(input('Maximum: '))
p = int(input('Power: '))

n = 1
while n ** p <= max:
    print(n)
    n = n + 1
