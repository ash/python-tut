import re

str = input('Your string: ')
n = int(input('N of the word to print (starting with 0): '))

words = re.findall(r'\b(\w+)\b', str)
print(words[n])
