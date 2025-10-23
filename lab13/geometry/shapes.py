from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.base + 2 * math.sqrt((self.base / 2) ** 2 + self.height ** 2)

    def __str__(self):
        return f"Triangle ({self.name}): base={self.base}, height={self.height}"

    def __repr__(self):
        return f"Triangle({self.name})"
    
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle ({self.name}): length={self.length}, width={self.width}"

    def __repr__(self):
        return f"Rectangle({self.name})"
    
class Trapezoid(Shape):
    def __init__(self, name, top_base, bottom_base, height):
        super().__init__(name)
        self.top_base = top_base
        self.bottom_base = bottom_base
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.top_base + self.bottom_base) * self.height

    def calculate_perimeter(self):
        return self.top_base + self.bottom_base + 2 * math.sqrt((self.top_base - self.bottom_base) ** 2 + self.height ** 2)

    def __str__(self):
        return f"Trapezoid ({self.name}): top_base={self.top_base}, bottom_base={self.bottom_base}, height={self.height}"

    def __repr__(self):
        return f"Trapezoid({self.name})"
    
class InscribedCircle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"InscribedCircle ({self.name}): radius={self.radius}"

    def __repr__(self):
        return f"InscribedCircle({self.name})"
    
class CircumscribedCircle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"CircumscribedCircle ({self.name}): radius={self.radius}"

    def __repr__(self):
        return f"CircumscribedCircle({self.name})"
