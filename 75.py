class Critter:
    counter = 0

    def __init__(self, given_name):
        self.name = given_name
        print("Creating a Critter object")
        Critter.counter += 1        

    def talk(self):        
        print("Hello, I am a critter #" + str(Critter.counter) + 
              ", my name is " + self.name)

    def __str__(self):
        return "This is a __str__ method for " + self.name

crit = Critter('Alpha')
crit.talk()
Critter.talk(crit)
crit.talk()

crit2 = Critter('Beta')
crit2.talk()

print(crit)
