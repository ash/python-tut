#a = [1, 11, 21, 1211, 111221, 

n = '1211'
for i in range(30):
    c = 0
    while c < len(n):
        curr = n[c]
        print('curr=' + str(curr))
        while c < len(n) and n[c] == curr:
            c += 1
        c += 1
    print(str(c) + curr)