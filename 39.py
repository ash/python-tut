# ranges

print('=====1=====')
for x in range(0, 10): # 10 excluded
    print(x)

print('=====2=====')
for x in range(0, 10, 2):
    print(x)

print('=====3=====')
for x in range(10, 0, -1):
    print(x)

array = range(1, 5)
print(type(array))
print(array) # range
print(len(array)) # 4

print(list(array)) # list
print(len(array)) # 4


