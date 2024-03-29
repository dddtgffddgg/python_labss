#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
sd.background_color = sd.COLOR_CYAN
point = sd.get_point(500, 400) 
radius = 50
for i in range(3):
    radius += 10 
    sd.circle(center_position = point, radius = radius, width = 5, color = sd.COLOR_GREEN)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет"
def bubbles(point, step, color):
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(center_position = point, radius = radius, color = color, width = 2)

point = sd.get_point(300, 300)
bubbles(point=point, step=10, color = sd.COLOR_ORANGE)

# Нарисовать 10 пузырьков в ряд
for x in range(100, 700, 1000):
    point = sd.get_point(x, 500)
    bubbles(point = point, step = 10, color = sd.COLOR_PURPLE)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubbles(point = point, step = 10, color = sd.COLOR_ORANGE)

sd.resolution = (1200, 900)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for x in range(100):
    point = sd.random_point()
    bubbles(point=point, step = 5, color = sd.COLOR_BLUE)

sd.resolution = (1200, 900)

sd.pause()
