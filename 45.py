n = 0

def inc_n(x):
    global n
    n += x

print(n) # 0

inc_n(10)
print(n) # 10

inc_n(15)
print(n) # 25
