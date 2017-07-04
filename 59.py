# n! = 1 * 2 * 3 * ... (n - 1) * n
# n! = (n - 1)! * n

def factorial(n):
    print("calling a function with argument " + str(n))
    if n <= 1:
        return 1
    f = factorial(n - 1) * n
    return f

print(factorial(5))
