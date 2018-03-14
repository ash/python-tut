import re
import zipfile

z = zipfile.ZipFile('channel.zip')

nothing = 90052

comments = ''

for i in range(100_000):
    filename = '%i.txt' % nothing    
    comments += z.getinfo(filename).comment.decode('utf-8')

    f = open('channel/' + filename)
    content = f.read()
    print(content)
    r = re.search(r'Next nothing is (\d+)', content)
    if r != None:
        n = r.group(1)
        nothing = int(n)
    else:
        break


print(comments)
