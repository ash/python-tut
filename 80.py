# iterable

for i in [1, 2, 3, 4]:
    print(i)

for i in range(10):
    print(i)

for ch in "string":
    print(ch)

for line in open("79.py"):
    print(line, end='')

print("====Using iterator===")

my_iterator = iter([1, 2, 3, 4])
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

my_iterator2 = iter([7, 8, 9])
print(len(list(my_iterator2)))
# print(next(my_iterator2)) # StopIteration exception

my_iterator3 = iter([10, 11, 12])
data = list(my_iterator3)
print(data)
