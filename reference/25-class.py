import random

class X:
    '''An X's docstring'''
    a = 10
    
    def show(self):
        print("self.a=%f, X.a=%f" % (self.a, X.a))
    def set_new_a(self, new_a):
        X.a = new_a
    def randomise(self):
        self.a = random.random()
        #X.show(self)
        #self.show()

x1 = X()
x2 = X()
x1.show()
x2.show()
print(x1.__dict__)
print(x2.__dict__)

x1.set_new_a(300)
x1.randomise()
x2.randomise()

x1.show()
x2.show()

print(X.a)
y = X()
X.randomise(y)
X.show(y)

print(X.__doc__)
