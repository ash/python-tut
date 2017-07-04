class Animal:
    def __init__(self, newname):
        self.myname = newname

    def name(self):
        print('My name is ' + self.myname)

    def __str__(self):
        return 'You know, my name is ' + self.myname


a = Animal('Ani')
b = Animal('Many')
b.name()
#b.sleep()

class Dog(Animal):
    def bark(self):
        print('aw-aw')

dog = Dog('Doggy')
dog.name()
dog.bark()
# # Dog.bark(dog)
#print(dog)

class Cat(Animal):
    def miau(self):
        print('miau')

    def name(self):
        print("I AM A CAT")

cat = Cat('Kitty')
cat.name()

zoo = []
zoo.append(dog)
zoo.append(cat)

print("ZOO inhabitants:")
for a in zoo:
    a.name() # polymorphic behaviour

# # a.sleep()
# # a.jump()
# #print(a)
