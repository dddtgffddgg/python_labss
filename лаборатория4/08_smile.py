#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
sd.resolution = (1200, 600)
sd.background_color = sd.COLOR_DARK_BLUE


for x in range(10):
    point = sd.random_point()
    sd.circle(center_position= point, radius = 85, width = 3)
    sd.circle(center_position= sd.Point(point.x - 45, point.y + 45), radius = 15, color = sd.COLOR_CYAN, width = 2) #глаз_1
    sd.circle(center_position= sd.Point(point.x + 45, point.y + 45), radius = 15, color = sd.COLOR_CYAN, width = 2) #глаз_2
    sd.line(start_point=sd.Point(point.x - 35, point.y - 30), end_point=sd.Point(point.x + 60, point.y - 45), color=sd.COLOR_RED, width=3) # рот


sd.pause()
