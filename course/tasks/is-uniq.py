array_variable = []
for i in range(1, 11):
    array_variable.append(int(input('Value ' + str(i) + ': ')))

set_variable = set(array_variable)
if len(set_variable) == len(array_variable):
    print('Only unique')
else:
    print('Not unique')