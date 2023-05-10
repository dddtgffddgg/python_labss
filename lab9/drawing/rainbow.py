import simple_draw as sd

def draw_rainbow():
    print("Отрисовываем радугу")

    # Определяем размеры экрана
    width = 800
    height = 600

    # Определяем центр экрана
    center_x = width // 2
    center_y = height // 2

    # Определяем радиус окружности
    radius = min(width, height) * 0.4

    # Определяем цвета радуги
    colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

    # Определяем угол, на который нужно повернуться для начала отрисовки радуги
    start_angle = 30

    # Отрисовываем радугу
    for i in range(len(colors)):
        color = colors[i]
        angle = start_angle + i * 60
        point = sd.get_point(center_x, center_y)
        sd.circle(center_position=point, radius=radius, color=color, width=20, start_angle=angle, end_angle=angle+60)

    # Ожидание закрытия окна
    sd.pause()
