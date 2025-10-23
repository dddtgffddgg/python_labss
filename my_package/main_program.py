import appJar
from calculations import calculate_shapes_area
from report import create_report

# Rest of the code remains the same...

# calculations.py
from triangle import calculate_triangle_area
from rectangle import calculate_rectangle_area
from trapezoid import calculate_trapezoid_area

# Rest of the code remains the same...

# report.py
from docx import Document

# Rest of the code remains the same...

# triangle.py
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# rectangle.py
def calculate_rectangle_area(length, width):
    return length * width

# trapezoid.py
def calculate_trapezoid_area(upper_base, lower_base, height):
    return 0.5 * (upper_base + lower_base) * height
