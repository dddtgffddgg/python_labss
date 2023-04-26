# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код
figures = {1 : "треугольник", 2 : "квадрат", 3 : "пятиугольник", 4 : "шестиугольник"}
for key, value in figures.items():
    print("{0}: {1}".format(key,value))

point = sd.Point(275, 250)

all_figures = {'1' : 120, '2' : 90, '3' : 72, '4' : 60}

figure = input ("Введите желаемый цвет > ")
if figure in all_figures:
    for i in range(30, 390, all_figures[figure]):
        v1 = sd.get_vector(point, angle = i, length = 125, width=3)
        v1.draw()
        point = v1.end_point
    sd.pause()
else:
    print('Вы ввели некоректный номер!')
