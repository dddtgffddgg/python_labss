#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1000, 1000)
# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код


for i in range (1, 11):
    d = sd.random_point()
    sd.circle(center_position = d,radius=90)
    sd.circle(center_position = sd.Point(d.x - 43, d.y + 25),radius=15)
    sd.circle(center_position = sd.Point(d.x + 43, d.y + 25),radius=15)
    point_list1 = [sd.Point(d.x - 63, d.y), sd.Point(d.x - 20, d.y - 45), sd.Point(d.x + 20, d.y - 45), sd.Point(d.x + 63, d.y )]
    sd.circle(center_position = sd.Point(d.x + 43, d.y + 25),radius=15)
    point_list2 = [sd.Point(d.x + 25, d.y - 40), sd.Point(d.x + 55, d.y - 50), sd.Point(d.x + 58, d.y - 47), sd.Point(d.x + 50, d.y - 15)]
   


sd.pause()