# sorting lists

a = [3, 2, 5, 7, 4, 1]

b = sorted(a)
print(b) # another list, which is sorted
print(a) # original list did not change

a.sort()
print(a) # orignal array is modified
