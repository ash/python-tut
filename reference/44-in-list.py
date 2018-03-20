import random
import time


bigdata = [random.randint(0,1_000_000) for _ in range(1_000_000)]
#print(bigdata)
print(len(bigdata))

cmp_value = 55_555

print('Using "in":')
start = time.time()
print(cmp_value in bigdata)
end = time.time()
print(end-start)

print('Using loop:')
start = time.time()
cmp = False
for i in bigdata:
    if i == cmp_value:
        cmp = True
        break
print(cmp)
end = time.time()
print(end-start)


