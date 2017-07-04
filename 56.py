def sum_of_all(*list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

a = [3, 4, 5]
print(sum_of_all(*a))

