with open('out.txt', 'w') as f:
    f.write('Hello\n')
    f.write('World\n')

with open('out2.txt', 'a') as f:
    f.writelines(['a\n', 'b\n', 'c\n'])
