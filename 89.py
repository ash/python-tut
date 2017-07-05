# nonlocal

# x = 10
# def f():
#     global x
#     x += 1
#     print(x)


x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x) # 2

outer()
print("global:", x)
