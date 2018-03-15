sign = 1
pi = 0
for i in range(1, 10_000_000, 2):
    pi += sign * 1/i
    sign *= -1
print(4 * pi)
