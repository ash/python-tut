import urllib.request
import re

nothing = '12345'

for i in range(450):
    url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing)
    content = url.read()
    print(i, content)

    parsed = re.search(r'the next nothing is (\d+)', str(content))
    nothing = parsed.group(1)

    if nothing == '16044':
        nothing = str(int(nothing) / 2)
