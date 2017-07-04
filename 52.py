def f(x):
    x[0] = 5
    print("inside f(x): " + str(x[0])) # 5

a = [2, 4, 6, 8, 10]
f(a) # passing by reference
print(a) # [5, 4, 6, 8, 10]
