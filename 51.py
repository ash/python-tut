def f(x):
    x = 5
    print("inside f(x): " + str(x))

a = 10
f(a) # passing by value
print(a) # 10
