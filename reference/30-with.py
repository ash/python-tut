class W:
    def __init__(self):
        pass
    def __enter__(self):
        print('__enter__')
    def __exit__(self, a1, a2, a3):
        print('__exit__')
    def info(self):
        print('W.info()')

w = W()
with w:
    w.info()
print('ok done')
