# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def create_snowflake():
    length = sd.random_number(10, 100)
    x = sd.random_number(100, 1100)
    y = sd.random_number(650, 750)
    return {'length': length, 'x': x, 'y': y}

snowflakes = []
while True:
    if len(snowflakes) < N:
        snowflakes.append(create_snowflake())

    sd.start_drawing()
    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point, color=sd.background_color, length=snowflake['length'])
        snowflake['x'] += sd.random_number(-10, 10)
        snowflake['y'] -= sd.random_number(5, 20)
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=snowflake['length'])
        if snowflake['y'] < 15:
            snowflakes.remove(snowflake)
    
    sd.finish_drawing()
    sd.sleep(0.1)

    if sd.user_want_exit():
        break

sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
