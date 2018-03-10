odd = []
even = []
for i in range(1, 11):
    n = int(input('Number %i: ' % i))
    if n % 2:
        odd.append(n)
    else:
        even.append(n)

all = odd
all.extend(even)
print(all)
