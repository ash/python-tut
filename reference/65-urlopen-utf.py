import urllib.request

with urllib.request.urlopen('http://www.google.com/') as f:
    html = f.read().decode('UTF-8')
    print(html)

