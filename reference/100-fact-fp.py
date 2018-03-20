def loop_fact(n):
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f

def fp_fact(n):
    if n <= 1:
        return 1
    else:
        return n * fp_fact(n - 1)


print(loop_fact(7))
print(fp_fact(7))
