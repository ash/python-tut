a = []
a.append('alpha')
a.append('beta')
a.append('gamma')

print('beta' in a)
print('ateb' in a)
print('abet' in a)

class S:
    def __init__(self):
        self.s = []
    def append(self, v):
        self.s.append(v)
    def __contains__(self, o):
        return o in self.s or o[::-1] in self.s

s = S()
s.append('alpha')
s.append('beta')
s.append('gamma')

print('beta' in s)
print('ateb' in s)
