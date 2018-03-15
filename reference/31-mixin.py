class NoneAttr:
    def __getattr__(self, name):
        def f():
            print('Non existing method')    

        print('No such attribute %s' % name)
        return f

class X(NoneAttr):
    pass

x = X()
x.unknown_attribute
x.unknown_method()
