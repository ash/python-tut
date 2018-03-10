import re

str = input('Your string: ')
new_str = re.sub(r'\s+', '*', str)
print(new_str)
