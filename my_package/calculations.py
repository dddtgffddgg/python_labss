from triangle import calculate_triangle_area
from rectangle import calculate_rectangle_area
from trapezoid import calculate_trapezoid_area


def calculate_shapes_area(shape_type, parameters):
    if shape_type == "triangle":
        base, height = parameters
        return calculate_triangle_area(base, height)
    elif shape_type == "rectangle":
        length, width = parameters
        return calculate_rectangle_area(length, width)
    elif shape_type == "trapezoid":
        upper_base, lower_base, height = parameters
        return calculate_trapezoid_area(upper_base, lower_base, height)
    else:
        return None
