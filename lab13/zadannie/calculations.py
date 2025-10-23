from shapes import Triangle, Rectangle, Trapezoid, Circle
from report_generation import generate_report

def calculate_triangle_area(base, height):
    triangle = Triangle(base, height)
    area = triangle.area()
    generate_report({'Triangle': area})
    return area

def calculate_rectangle_area(width, height):
    rectangle = Rectangle(width, height)
    area = rectangle.area()
    generate_report({'Rectangle': area})
    return area

def calculate_trapezoid_area(base1, base2, height):
    trapezoid = Trapezoid(base1, base2, height)
    area = trapezoid.area()
    generate_report({'Trapezoid': area})
    return area

def calculate_circle_area(radius):
    circle = Circle(radius)
    area = circle.area()
    generate_report({'Circle': area})
    return area

