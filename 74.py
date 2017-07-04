class Critter(object):
    counter = 0

    def __init__(self):
        print("Creating a Critter object")
        Critter.counter += 1        

    def talk(self):        
        print("Hello, I am a critter #" + str(Critter.counter))

crit = Critter()
crit.talk()
crit.talk()

crit2 = Critter()
crit2.talk()
