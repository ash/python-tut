# if

threshold = 100

x = int(input("What is your number? "))

print(x > threshold)

if x > threshold:
    print('Too big number')
# else:
#     print('OK, good')


r = x > threshold
print(type(r))
if r:
    print("also big")

print('Your value was ' + str(x))
