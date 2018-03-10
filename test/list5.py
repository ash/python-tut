colours = ['red', 'green', 'blue']
colours.insert(1, 'yellow')
print(colours) # ['red', 'yellow', 'green', 'blue']

del colours[1]
print(colours)

last_elem = colours.pop()
print(colours)
print(last_elem)


colours = ['red', 'green', 'blue']
x = colours.pop(1);
print(x)
print(colours)
