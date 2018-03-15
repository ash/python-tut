def f(x):
    def helper(x):
        return -x
    return 3 * helper(x)

print(f(5))
#print(helper(5))
# method resolution order, MRO

class B1:
    def whoami(self):
        print('B1')

class B2:
    def whoami(self):
        print('B2')

#class C(B2, B1):
class C(B1, B2):
    pass

b1 = B1()
b2 = B2()
b1.whoami()
b2.whoami()

c = C()
c.whoami()