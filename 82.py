# lambda

# function with a name
def func(x):
    return x ** 2

f = lambda x: x ** 2

print(func(3)) # 9

print(type(f)) # <class 'function'>
print(f(3)) # 9


staff = [
    {"name" : "John",   "age" : 20},
    {"name" : "Thomas", "age" : 40},
    {"name" : "Karl",   "age" : 19},
    {"name" : "Johan",  "age" : 55}
]

# Johan (55)
# John (20)
# Karl (19)
# Thomas (40)

def ff(x):
    return x["name"]

#r = sorted(staff, key = lambda x: x["name"])
r = sorted(staff, key = ff)
print(r)

# {"name" : "John",   "age" : 20} < {"name" : "Thomas", "age" : 40} = ? 
# x = {"name" : "John",   "age" : 20} ==> x["name"] ==> "John"
# x = {"name" : "Thomas", "age" : 40} ==> x["name"] ==> "Thomas" 
# "John" < "Thomas"

for p in r:
    print(p["name"] + ' (' + str(p["age"]) + ')')


# also see map and filter
