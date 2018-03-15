class B1:
    def m(self):
        print('B1.m')

class B2:
    def m(self):
        print('B2.m')

class C(B1, B2):
    pass

c = C()
c.m()
