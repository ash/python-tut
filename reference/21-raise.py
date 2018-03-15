def f():
    print(1)
    raise IndexError('hello')
    print(2)

print('before')
f()
print('after')