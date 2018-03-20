class S:
    def __init__(self):
        self.objects = []

    def append(self, o):
        self.objects.append(o)

    def __contains__(self, o):
        return o in self.objects or o[::-1] in self.objects

data = list()
data.append('alpha')
data.append('beta')
data.append('gamma')

print('beta' in data)
print('ateb' in data)

s = S()
s.append('alpha')
s.append('beta')
s.append('gamma')

print('beta' in s)
print('xxx' in s)
print('ateb' in s)
