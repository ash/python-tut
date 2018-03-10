import re

str = input('Your string: ')

str = re.sub(r'\[.*?\]', '', str)
print(str)
