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

# example.py

import my_burger

print("Для приготовления двойного чизбургера нужно:")
def double_cheeseburger():
    my_burger.add_bun()
    my_burger.add_patty()
    my_burger.add_cheese()
    my_burger.add_patty()
    my_burger.add_cheese()
    my_burger.add_pickle()
    my_burger.add_ketchup()
    my_burger.add_mustard()
    my_burger.add_bun()
double_cheeseburger()    

print("Готово! Приятного аппетита!")

import my_burger
print("Для приготовления бургера Гранд Де Люкс нам нужно:")
def burger_Grand_De_Lyux():
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
Grand_De_Lyux        
print("Готово! Приятного аппетита!")
