pi = 0

sign = 1
denom = -1
for i in range(1,100):
    sign *= -1
    denom += 2  # vs. 2 * i - 1
    pi += sign / denom
print(-4*pi)