#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингридиентов - создать соответствующие функции в модуле my_burger
# my_burger.py

def add_bun():
    print("А теперь добавим булочки")

def add_patty():
    print("А теперь добавим котлеты")

def add_pickle():
    print("А теперь добавим огурчика")

def add_ketchup():
    print("А теперь добавим кетчупа")

def add_mustard():
    print("А теперь добавим горчицы")

def add_cheese():
    print("А теперь добавим сыра")

def add_tomato():
    print("А теперь добавим помидорку")

def add_special_sauce():
    print("А теперь добавим специальный соус")

def add_salat():
    print("А теперь добавим салата")            

# example.py

import my_burger
print("Для приготовления двойного чизбургера нужно:")

my_burger.add_bun()
my_burger.add_patty()
my_burger.add_cheese()
my_burger.add_patty()
my_burger.add_cheese()
my_burger.add_pickle()
my_burger.add_ketchup()
my_burger.add_mustard()
my_burger.add_bun()

print("Готово! Приятного аппетита!")

import my_burger
print("Для приготовления бургера Гранд Де Люкс нам нужно:")
my_burger.add_bun()
my_burger.add_ketchup()
my_burger.add_mustard()
my_burger.add_pickle()
my_burger.add_salat()
my_burger.add_tomato()
my_burger.add_cheese()
my_burger.add_patty()
my_burger.add_cheese()
my_burger.add_bun()
print("Готово! Приятного аппетита!")
