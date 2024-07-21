class Animal:
    def sound(self):
        print("Some generic animal sound")

class Mammal(Animal):
    def sound(self):
        print("Some generic mammal sound")

class Dog(Mammal):
    def sound(self):
        print("Bark")

# Create an instance of the Dog class
dog = Dog()

# Demonstrate multilevel inheritance
dog.sound()

# Demonstrate calling the sound method from each level
animal = Animal()
mammal = Mammal()

animal.sound()
mammal.sound()
dog.sound()
