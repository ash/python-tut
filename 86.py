# exception

n = 4
z = 0

try:
    #r = n / z
    open('non-existing.txt')
except(ZeroDivisionError):
    print("Division by zero happened")
except(IOError):
    print("I/O error occured")
except:
    print("Something else happened")

print("Done")
