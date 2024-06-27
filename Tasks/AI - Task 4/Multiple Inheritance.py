class FlyingAnimal:
    def fly(self):
        print("Flying")

class WalkingAnimal:
    def walk(self):
        print("Walking")

class Bat(FlyingAnimal, WalkingAnimal):
    pass

# Create an instance of the Bat class
bat = Bat()

# Demonstrate multiple inheritance
bat.fly()
bat.walk()
