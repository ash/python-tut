def factorial(n):
    f = 1
    for x in range(1, n + 1): # 1, 2, 3, 4, 5
        f *= x
        # f *= 1
        # f *= 2
        # f *= 3
        # f *= 4
        # f *= 5
    return f 

print(factorial(-5))
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(5))
