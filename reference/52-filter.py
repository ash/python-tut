def f(x):
    return x % 2

data = list(range(10))
f_obj = filter(f, data)
result = list(f_obj)
print(result)
