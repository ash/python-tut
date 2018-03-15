class Person:
    '''Represents a person'''

    def __init__(self, name, age = 19):
        self.name = name
        self.age = age
    
    def say(self):
        print('My name is %s, I am %i years old.' % (self.name, self.age))
    
p1 = Person('John', 20)
p2 = Person('Jessica')
p1.say()
p2.say()

print(p1)
print(p1.name)

p2.age += 1
p2.say()


print(help(Person))
print(p1.__dict__)
