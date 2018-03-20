def loop_sum(list):
    s = 0
    for x in list:
        s += x
    return s

def fp_sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

data = list(range(100))
print(loop_sum(data))
print(fp_sum(data))
