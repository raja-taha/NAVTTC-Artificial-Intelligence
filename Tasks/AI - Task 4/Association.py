class Car:
    def __init__(self, model):
        self.model = model

class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car  # Association with Car

    def drive(self):
        print(f"{self.name} is driving a {self.car.model}")

# Create an instance of Car
car = Car("Toyota")

# Create an instance of Driver
driver = Driver("Alice", car)

# Demonstrate association
driver.drive()
