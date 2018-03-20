def f(x):
    return x % 2

data = list(range(10))
map_obj = filter(f, data)
result = list(map_obj)
print(result)
