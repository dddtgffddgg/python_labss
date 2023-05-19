# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс catа. У catа eat аттрибуты - satiety и home (в catором он живет).
# cat живет с humanом в homeе.
# Для catа home характеризируется - миской для еды и грязью.
# Изначально в homeе нет еды для catа и нет грязи.

# Доработать класс humanа, добавив методы
#   подобрать catа - у catа появляется home.
#   купить catу еды - кошачья еда в homeе увеличивается на 50, money уменьшаются на 50.
#   убраться в homeе - степень грязи в homeе уменьшается на 100, satiety у humanа уменьшается на 20.
# Увеличить кол-во зарабатываемых humanом денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# cat может eat, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда cat спит - satiety уменьшается на 10
# Когда cat ест - satiety увеличивается на 20, кошачья еда в homeе уменьшается на 10.
# Когда cat дерет обои - satiety уменьшается на 10, степень грязи в homeе увеличивается на 5
# Если степень сытости < 0, cat умирает.
# Так же надо реализовать метод "действуй" для catа, в catором он принимает решение
# что будет делать сегодня

# humanу и catу надо вместе прожить 365 дней.

# TODO здесь ваш код
class Human:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.satiety = 50
        self.home = None

    def __str__(self):
        return self.name

    def zabral_cat(self, cat):
        cat.home = self.home

    def buy_cats_food(self):
        if self.money >= 50:
            self.money -= 50
            self.home.cats_food += 50
            print(f"{self.name} купил еду для кота.")
        else:
            print(f"{self.name} не имеет достаточно денег, чтобы купить еду для кота.")

    def clean_in_home(self):
        self.home.dirty -= 100
        self.satiety -= 20
        print(f"{self.name} убрался в доме.")

    def zarabotal_money(self):
        self.money += 150
        print(f"{self.name} заработал 150 денег.")


class Cat:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.home = None

    def __str__(self):
        return self.name

    def eat(self):
        if self.home.cats_food >= 10:
            self.satiety += 20
            self.home.cats_food -= 10
            print(f"{self.name} поел.")
        else:
            print(f"{self.name} не может поесть, так как нет еды.")

    def sleep(self):
        self.satiety -= 10
        print(f"{self.name} поспал.")

    def wallpaper(self):
        self.satiety -= 10
        self.home.dirty += 5
        print(f"{self.name} дерет обои.")

    def deloet_chtoto(self):
        if self.satiety <= 0:
            print(f"{self.name} умер.")
            return

        if self.satiety < 20:
            self.eat()
        elif self.home.dirty > 100:
            self.wallpaper()
        else:
            self.sleep()

class home:
    def __init__(self):
        self.cats_food = 0
        self.dirty = 0

human = Human("Женя")
cat = Cat("Басик")
home = home()

human.money = 200
human.home = home
cat.home = home

for день in range(1, 366):
    print(f">>>>> День {день} <<<<<")
    human.zarabotal_money()
    human.zabral_cat(cat)
    human.buy_cats_food()
    human.clean_in_home()
    cat.deloet_chtoto()
    print(f"Уровень грязи в доме: {home.dirty}")
    print(f"Кошачья еда в доме: {home.cats_food}")
    print(f"Сытость {human}: {human.satiety}")
    print(f"Сытость {cat}: {cat.satiety}")
    print("")

    if human.satiety <= 0:
        print(f"{human} умер от голода.")
        break

    if cat.satiety <= 0:
        print(f"{cat} умер от голода.")
        break




# Усложненное задание (делать по желанию)
# Создать несколько (2-3) catов и подселить их в home к humanу.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество catов, catорое может прокормить human...)
