# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр 01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см /results/exercise_02_global_color.jpg

# TODO здесь ваш код
all_colors = {'1' : sd.COLOR_RED, '2' : sd.COLOR_ORANGE, '3' : sd.COLOR_YELLOW, '4' : sd.COLOR_GREEN,
                  '5' : sd.COLOR_CYAN, '6' : sd.COLOR_BLUE, '7' : sd.COLOR_PURPLE}
colors = {1 : "красный", 2 : "оранжевый", 3 : "желтый", 4 : "зеленый",
                  5 : "сине-зеленый", 6 : "голубой", 7 : "фиолетовый"}
for key, value in colors.items():
    print("{0}: {1}".format(key,value))
color = input ("Введите желаемый цвет > ")

if color in all_colors:
    point1 = sd.Point(100, 100)
    for i in range(30, 390, 120):
        v1 = sd.get_vector(point1, angle = i, length = 125, width=3)
        v1.draw(all_colors[color])
        point1 = v1.end_point

    point2 = sd.Point(400, 100)
    for i in range(30, 390, 90):
        v2 = sd.get_vector(point2, angle = i, length = 125, width=3)
        v2.draw(all_colors[color])
        point2 = v2.end_point

    point3 = sd.Point(125, 375)
    for i in range(30, 390, 72):
        v3 = sd.get_vector(point3, angle = i, length = 100, width=3)
        v3.draw(all_colors[color])
        point3 = v3.end_point

    point4 = sd.Point(400, 375)
    for i in range(30, 390, 60):
        v4 = sd.get_vector(point4, angle = i, length = 100, width=3)
        v4.draw(all_colors[color])
        point4 = v4.end_point
    sd.pause()
else:
    print('Вы ввели некоректный номер!')
