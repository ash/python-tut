def sum_of_all(list):
    # range(4) => 0, 1, 2, 3
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

print(sum_of_all([1]))
print(sum_of_all([1, 2]))
print(sum_of_all([1, 2, 3]))
print(sum_of_all([1, 2, 3, 4]))

my_list = [2, 3, 5, 6, 8, 9]
print(sum_of_all(my_list))
