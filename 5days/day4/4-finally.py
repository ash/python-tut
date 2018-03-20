try:
    #print(1/0)
    n = [1, 2, 3]
    print(n[100])
except ZeroDivisionError:
    print('Division by 0')
finally:
    print('Finally')

print('ok done')
