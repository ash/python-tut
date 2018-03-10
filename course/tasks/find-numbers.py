import re

str = input('Your string: ')
nums = re.findall(r'\d+', str)

for x in nums:
    print(x)