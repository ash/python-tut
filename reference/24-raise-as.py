def f():
    print(1)
    raise IndexError('hello')
    print(2)

try:
    print('before')
    f()
    print('after')
except IndexError as ie:
    print(ie.__class__)
