i = iter([1, 2, 3, 4])

try:
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
except(StopIteration):
    print("List is over")
finally:
    print("Finally")

print("Done")
