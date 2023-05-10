from PIL import Image, ImageDraw
import math

def draw_rainbow():
    print("Отрисовываем радугу")

    # Определяем размеры изображения
    width = 400
    height = 300

    # Определяем центр изображения
    center_x = width / 2
    center_y = height / 2

    # Определяем радиус окружности
    radius = min(width, height) * 0.4

    # Определяем цвета радуги
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    # Определяем угол, на который нужно повернуться для начала отрисовки радуги
    start_angle = math.pi / 6

    # Создаем изображение
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Отрисовываем радугу
    for i in range(len(colors)):
        color = colors[i]
        angle = start_angle + i * math.pi / 3
        x = center_x + math.cos(angle) * radius
        y = center_y - math.sin(angle) * radius
        draw.arc((x - radius, y - radius, x + radius, y + radius), start=math.degrees(angle) + 180, end=math.degrees(angle) + 360, fill=color)

    # Отображаем изображение
    image.show()
