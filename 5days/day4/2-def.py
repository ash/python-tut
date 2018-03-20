def f(x):
    print('f(%i)' % x)

class C:
    def f(self, x):
        print('C.f(self, %i)' % x)

f(5)
c = C()
c.f(5)

C.f(c, 5)
