list1 = [[10, 20, 30]] * 3
list2 = [[10, 20, 30] for _ in range(3)]

print(list1)
print(list2)

list1[1][1] = 99
list2[1][1] = 99

print(list1)
print(list2)
