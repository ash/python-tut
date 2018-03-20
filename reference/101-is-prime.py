def is_prime(n):
    def is_prime_helper(n, i):  
        if n <= 2:
            return True
        elif n % i == 0:
            return False
        elif i < n / 2:
            return is_prime_helper(n, i + 1)
        else:
            return True
    
    return is_prime_helper(n, 2)
    
for i in range(100):
    if is_prime(i):
        print(i)

# print(is_prime(8))