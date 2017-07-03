# dicts

# dictionary, hash, associative array, map

d = {"name": "John", "last name": "Johnson"}
#    ^ key   ^value   ^ key        ^ value
print(d)

# a = {"0": "John", "1": "Johnson"}
# a = ['John', 'Johnson']
# a[0] # name
print(d["name"])
print(d["last name"])

d["name"] = 'Jonny'
print(d["name"])

del(d["name"])
print(d)

d["second name"] = 'Frank'
print(d)
