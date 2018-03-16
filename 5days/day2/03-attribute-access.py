# This program demonstrates how you can access data attributes using
# methods: get_age and inc_age. You still cannot hide the implementation
# attributes from the user of the class, but if you use methods to 
# manipulate data, you can restrict the operations that you can do with them.
class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        
    def show(self):
        print('My name is %s, I am %i years old.' % (self.name, self.age))

    def get_age(self):
        return self.age
    
    def inc_age(self):
        self.age += 1

p = Person('John', 60)
print(p.get_age())
#p.set_age(18)
p.inc_age()
print(p.get_age())


