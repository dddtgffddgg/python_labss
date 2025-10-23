from geometry.shapes import Triangle, Rectangle, Trapezoid, InscribedCircle, CircumscribedCircle

def calculate_triangle_area(base, height):
    triangle = Triangle("MyTriangle", base, height)
    return triangle.calculate_area()

def calculate_triangle_perimeter(base, height):
    triangle = Triangle("MyTriangle", base, height)
    return triangle.calculate_perimeter()

def calculate_rectangle_area(length, width):
    rectangle = Rectangle("MyRectangle", length, width)
    return rectangle.calculate_area()

def calculate_rectangle_perimeter(length, width):
    rectangle = Rectangle("MyRectangle", length, width)
    return rectangle.calculate_perimeter()

def calculate_trapezoid_area(top_base, bottom_base, height):
    trapezoid = Trapezoid("MyTrapezoid", top_base, bottom_base, height)
    return trapezoid.calculate_area()

def calculate_trapezoid_perimeter(top_base, bottom_base, height):
    trapezoid = Trapezoid("MyTrapezoid", top_base, bottom_base, height)
    return trapezoid.calculate_perimeter()

def calculate_inscribed_circle_area(radius):
    inscribed_circle = InscribedCircle("MyInscribedCircle", radius)
    return inscribed_circle.calculate_area()

def calculate_inscribed_circle_perimeter(radius):
    inscribed_circle = InscribedCircle("MyInscribedCircle", radius)
    return inscribed_circle.calculate_perimeter()

def calculate_circumscribed_circle_area(radius):
    circumscribed_circle = CircumscribedCircle("MyCircumscribedCircle", radius)
    return circumscribed_circle.calculate_area()

def calculate_circumscribed_circle_perimeter(radius):
    circumscribed_circle = CircumscribedCircle("MyCircumscribedCircle", radius)
    return circumscribed_circle.calculate_perimeter()

def calculate_inscribed_triangle_radius(base, height):
    triangle = Triangle("MyTriangle", base, height)
    return triangle.calculate_inscribed_circle_radius()

def calculate_circumscribed_triangle_radius(base, height):
    triangle = Triangle("MyTriangle", base, height)
    return triangle.calculate_circumscribed_circle_radius()

def calculate_inscribed_rectangle_radius(length, width):
    rectangle = Rectangle("MyRectangle", length, width)
    return rectangle.calculate_inscribed_circle_radius()

def calculate_circumscribed_rectangle_radius(length, width):
    rectangle = Rectangle("MyRectangle", length, width)
    return rectangle.calculate_circumscribed_circle_radius()

def calculate_inscribed_trapezoid_radius(top_base, bottom_base, height):
    trapezoid = Trapezoid("MyTrapezoid", top_base, bottom_base, height)
    return trapezoid.calculate_inscribed_circle_radius()

def calculate_circumscribed_trapezoid_radius(top_base, bottom_base, height):
    trapezoid = Trapezoid("MyTrapezoid", top_base, bottom_base, height)
    return trapezoid.calculate_circumscribed_circle_radius()
