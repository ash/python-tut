import requests

r = requests.get('http://www.nasdaq.com')
print(r.status_code)
print(r.content)


# GET
# POST
