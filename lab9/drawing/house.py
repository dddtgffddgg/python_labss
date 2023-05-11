import simple_draw as sd


def draw_house(height, width, start, brick_color, roof_color):
    widths = width + start
    sd.rectangle(left_bottom=sd.Point(start - 50, 150), right_top=sd.Point(widths + 50, height),
                 color=brick_color)
    for g in range(height, 150, -50):
        if g % 100 == 50:
            for i in range(start, widths, 100):
                sd.rectangle(left_bottom=sd.Point(i, g - 50), right_top=sd.Point(i + 100, g),
                             width=1, color=brick_color)
        else:
            for i in range(start - 50, widths, 100):
                sd.rectangle(left_bottom=sd.Point(i, g - 50), right_top=sd.Point(i + 100, g),
                             width=1, color=brick_color)
    sd.rectangle(left_bottom=sd.Point(start - 50, 150), right_top=sd.Point(widths + 50, height),
                 width=1, color=brick_color)
    point_list = [sd.Point(start - 80, height), sd.Point(start + width // 2, height + 200),
                  sd.Point(widths + 80, height)]
    sd.polygon(point_list, width=0, color=roof_color)


# Пример использования функции
house_height = 400
house_width = 400
house_start = 560
brick_color = (178, 34, 34)  # Красный цвет для кирпичей
roof_color = (139, 69, 19)  # Коричневый цвет для крыши
draw_house(house_height + 150, house_width, house_start, brick_color, roof_color)

sd.pause()
