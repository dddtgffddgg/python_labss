#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center_position = sd.get_point(300, 300)  # центр пузырька
radius = 50  # радиус первой окружности
step = 5  # шаг

for _ in range(3):
    radius += step
    sd.circle(center_position, radius=radius, width=2)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def draw_bubble(center_position, step, color):
    radius = 50  # радиус первой окружности
    for _ in range(3):
        radius += step
        sd.circle(center_position, radius=radius, color=color, width=2)

# Нарисовать 10 пузырьков в ряд
def draw_bubble(center_position, step, color):
    radius = 50  # радиус первой окружности
    for _ in range(3):
        radius += step
        sd.circle(center_position, radius=radius, color=color, width=2)

sd.resolution = (1200, 600)

x_start = 100  # начальная координата x
y = 300  # координата y
step = 60  # шаг между пузырьками
color = sd.COLOR_ORANGE  # цвет пузырьков

for i in range(10):
    x = x_start + i * step
    center_position = sd.get_point(x, y)
    draw_bubble(center_position, step=5, color=color)

# Нарисовать три ряда по 10 пузырьков
def draw_bubble(center_position, step, color):
    radius = 50  # радиус первой окружности
    for _ in range(3):
        radius += step
        sd.circle(center_position, radius=radius, color=color, width=2)

sd.resolution = (1200, 900)

x_start = 100  # начальная координата x
y_start = 100  # начальная координата y
step = 60  # шаг между пузырьками
color1 = sd.COLOR_ORANGE  # цвет первого ряда пузырьков
color2 = sd.COLOR_BLUE  # цвет второго ряда пузырьков
color3 = sd.COLOR_GREEN  # цвет третьего ряда пузырьков

for row in range(3):  # внешний цикл по рядам
    y = y_start + row * 200
    for i in range(10):  # внутренний цикл по пузырькам в ряду
        x = x_start + i * step
        center_position = sd.get_point(x, y)
        if row == 0:
            color = color1
        elif row == 1:
            color = color2
        else:
            color = color3
        draw_bubble(center_position, step=5, color=color)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
import random

def draw_bubble(center_position, step, color):
    radius = 50  # радиус первой окружности
    for _ in range(3):
        radius += step
        sd.circle(center_position, radius=radius, color=color, width=2)

sd.resolution = (1200, 900)

for _ in range(100):
    x = random.randint(0, sd.resolution[0])
    y = random.randint(0, sd.resolution[1])
    center_position = sd.get_point(x, y)
    color = sd.random_color()
    draw_bubble(center_position, step=5, color=color)

sd.pause()
