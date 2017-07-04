def sum_of_all(*list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

print(sum_of_all(1))
print(sum_of_all(1, 2))
print(sum_of_all(1, 2, 3))
print(sum_of_all(1, 2, 3, 4))
