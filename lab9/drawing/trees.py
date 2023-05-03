# -*- coding: utf-8 -*-

import simple_draw as sd
import random

def draw_tree():
    sd.resolution = (1200, 600)
    point_0 = sd.get_point(600, 0)
    v0 = sd.get_vector(point_0, angle=90, length=50)
    v0.draw()

    def branch(point, angle, length):
        if length < 5:
            return
        v1 = sd.get_vector(start_point=point, angle=angle, length=length)
        v1.draw()
        v2 = sd.get_vector(start_point=point, angle=angle, length=length)
        v2.draw()
        next_point1 = v1.end_point
        next_point2 = v2.end_point
        next_length = length * random.uniform(0.60, 0.90)
        branch(point=next_point1, angle=angle-random.uniform(18, 42), length=next_length)
        branch(point=next_point2, angle=angle+random.uniform(18, 42), length=next_length)

    branch(point=v0.end_point,angle=90, length=100)
    sd.pause()
////здесь должна скачать pip install Pillow
