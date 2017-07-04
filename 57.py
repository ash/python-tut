num = 1
def func():
    num = 1
    # global num
    num = num + 3
    print(num)

func()
print(num)
