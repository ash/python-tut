# Catch an exception if there is no file on disk.
try:
    with open('non-existing.txt') as f:
    data = f.read()
    print(data)
# But maybe don't try catching _all_ the errors. Just stick to those you can handle.
except FileNotFoundError:
    print('not found')

print('ok done')
