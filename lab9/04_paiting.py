#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать (или при необходимости написать) функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)



# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.


import simple_draw as sd
from drawing import rainbow, house, tree, smile

sd.resolution = (1920, 1080)

sd.ellipse(sd.Point(-180, -250), sd.Point(2100, 250), color=sd.COLOR_GREEN)

rainbow_start = sd.Point(760, -150)
rainbow_rad = 1300
rainbow_width = 15
rainbow.draw_rainbow(rainbow_start, rainbow_rad, rainbow_width)

tree_leaves_color = sd.COLOR_YELLOW
tree_color = (101, 67, 33)
tree_start = sd.Point(1400, 150)
tree.draw_tree(tree_start, tree_leaves_color, tree_color)

house_height = 400
house_width = 400
house_start = 560
house_lines_color = sd.COLOR_DARK_GREEN
house_color = (136,69,53)
house.draw_house(house_height+100, house_width, house_start, house_lines_color, house_color)


smile_x = tree_start.x + 250  # Положение смайлика по оси X
smile_y = tree_start.y + 200  # Положение смайлика по оси Y
smile_radius = 100

# Нарисуем смайлик
smile.draw_smile(x=smile_x, y=smile_y, radius=smile_radius)

# Нарисуем рот
sd.circle(center_position=sd.Point(smile_x, smile_y - smile_radius // 2), radius=smile_radius // 2,
          color=sd.COLOR_DARK_RED, width=10)

# Нарисуем глаза
eye_radius = 15
eye_y = smile_y + smile_radius // 4  # Положение глаз по оси Y
sd.circle(center_position=sd.Point(smile_x - smile_radius // 3, eye_y), radius=eye_radius, color=sd.COLOR_BLACK, width=0)
sd.circle(center_position=sd.Point(smile_x + smile_radius // 3, eye_y), radius=eye_radius, color=sd.COLOR_BLACK, width=0)



sd.pause()
