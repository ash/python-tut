def f(x):
    return x ** 2

data = [1, 3, 5, 7]
map_obj = map(f, data)
result = list(map_obj)
print(result)
