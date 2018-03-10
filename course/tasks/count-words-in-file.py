filename = input('File name: ')

content = ''
for line in open(filename):
    content += line

#print(content.split())
words_count = len(content.split())
print('%d words in the file' % words_count)