class Ape:
    def __init__(self, age):
        self.age = age
    def say(self):
        print('oo-oo')

class Person(Ape):
    '''A person'''

    def __init__(self, name, age):
        super().__init__(age)
        self.name = name        
    
    def say(self):
        print('My name is %s, I am %i years old.' % (self.name, self.age))

a1 = Ape(10)
a1.say()

p1 = Person('John', 20)
p2 = Person('Jessica', 19)
p1.say()
p2.say()

print(p1)
print(p1.name)
print(p1.__dict__)

p2.age += 1
p2.say()
