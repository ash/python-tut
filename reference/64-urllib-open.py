import urllib.request

with urllib.request.urlopen('http://www.google.com/') as f:
    html = f.read()
    print(html)

