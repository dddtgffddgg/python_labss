import math

def calculate_area(base, height, side_a, side_b, result_label):
    try:
        base = float(base)
        height = float(height)
        side_a = float(side_a)
        side_b = float(side_b)

        triangle_area = 0.5 * base * height
        rectangle_area = base * height
        trapezoid_area = 0.5 * (side_a + side_b) * height

        triangle_inscribed_radius = triangle_area / (base + height + math.sqrt(base**2 + height**2))
        triangle_circumscribed_radius = (base * height) / (math.sqrt(base**2 + height**2))
        rectangle_inscribed_radius = min(base, height) / 2
        rectangle_circumscribed_radius = math.sqrt(base**2 + height**2) / 2
        trapezoid_inscribed_radius = trapezoid_area / (side_a + side_b)
        trapezoid_circumscribed_radius = (side_a + side_b) / 4

        result_message = f"Треугольник: {triangle_area}\n" \
                         f"Прямоугольник: {rectangle_area}\n" \
                         f"Трапеция: {trapezoid_area}\n" \
                         f"Радиус вписанной окружности треугольника: {triangle_inscribed_radius}\n" \
                         f"Радиус описанной окружности треугольника: {triangle_circumscribed_radius}\n" \
                         f"Радиус вписанной окружности прямоугольника: {rectangle_inscribed_radius}\n" \
                         f"Радиус описанной окружности прямоугольника: {rectangle_circumscribed_radius}\n" \
                         f"Радиус вписанной окружности трапеции: {trapezoid_inscribed_radius}\n" \
                         f"Радиус описанной окружности трапеции: {trapezoid_circumscribed_radius}"

        result_label.config(text=result_message)

    except ValueError:
        result_label.config(text="Пожалуйста, введите числовые значения для параметров.")
