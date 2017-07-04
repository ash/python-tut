# search tables
# pre-calculated data

fact = [0] * 100

def factorial(n):
    if n <= 1:
        return 1
    f = fact[n - 1] * n
    return f

for i in range(100):
    fact[i] = factorial(i)

print(fact[5])
