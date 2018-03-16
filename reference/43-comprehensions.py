mylist = [x**2 for x in range(10)]
mylist2 = [x**2 for x in range(10) if x % 2]

print(mylist)
print(mylist2)

myset = {x ** 3 for x in range(5)}
myset2 = {x ** 3 for x in range(5) if x > 0}

print(myset)
print(myset2)

mydict = {"4th power of %i" % x : x ** 4 for x in range(5)}
print(mydict)
