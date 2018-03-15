
class LoggableData:
    def __init__(self, data):
        self.data = data

    def __set__(self, instance, datatype):
        print('__set__')
        self.data = instance

    def __get__(self, instance, datatype):
        print('__get__')
        return self.data

class X:
    n = LoggableData(10)

    def __init__(self, value):
        self.n = LoggableData(value)

    # def set_value(self, value):
    #     print('Value was set to %i' % self.value.data)
    #     self.value = value
        
    # def get_value(self):
    #     print('Somebody used the value of %i' % self.value.data)
    #     return self.value


x = X(5)
# x.set_value(6)
# print(x.get_value())

x.value = LoggableData(7)
x.n = 11
print(x.value.data)

