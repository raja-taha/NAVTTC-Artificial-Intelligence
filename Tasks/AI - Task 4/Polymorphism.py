import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Demonstrate polymorphism
shapes = [circle, rectangle]
for shape in shapes:
    print(f"The area is: {shape.area()}")
