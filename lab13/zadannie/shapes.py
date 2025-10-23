from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self):
        self.managed = True

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"This is a {type(self).__name__}."

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"This is a {type(self).__name__} with base {self.base} and height {self.height}."

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"This is a {type(self).__name__} with width {self.width} and height {self.height}."

class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"This is a {type(self).__name__} with base1 {self.base1}, base2 {self.base2}, and height {self.height}."

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def __str__(self):
        return f"This is a {type(self).__name__} with radius {self.radius}."
