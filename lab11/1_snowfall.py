import simple_draw as sd


class Snowflake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.length = 0
        self.factor_a = 0
        self.factor_b = 0
        self.factor_c = 0

    def create(self):
        self.x = sd.random_number(0, sd.resolution[0])  # Случайная начальная координата X
        self.y = sd.resolution[1]  # Начальная координата Y (внизу экрана)
        self.length = sd.random_number(10, 40)  # Длина снежинки
        self.factor_a = sd.random_number(1, 10) / 10  # Горизонтальный фактор амплитуды
        self.factor_b = sd.random_number(1, 10) / 10  # Вертикальный фактор амплитуды
        self.factor_c = sd.random_number(10, 60)  # Фактор скорости

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(point, self.length, sd.background_color)

    def move(self):
        self.x += sd.random_number(-2, 2)  # Добавляем некоторое горизонтальное отклонение
        self.y -= self.factor_c  # Перемещаем снежинку вверх

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(point, self.length, sd.COLOR_WHITE)

    def can_fall(self):
        return self.y > 0  # Проверяем, находится ли снежинка в пределах экрана


flake = Snowflake()

while True:
    flake.create()
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
