sentence = input('Your string: ')

words = sentence.split()
unique = set(words)
print(str(len(unique)) + ' unique words')

# Your string: hello here hello there
# 3 unique words
