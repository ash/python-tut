class MyE(Exception):
    pass


try:
    raise MyE
except MyE:
    print('MyE found')