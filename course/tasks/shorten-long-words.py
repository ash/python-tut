import re

str = input('Your string: ')

str = re.sub(r'\b(\w{5})(\w+)\b', r'\1...', str)
print(str)

# Your string: helloworld hi there
# hello... hi there
