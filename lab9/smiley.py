def draw_smiley():
    import math

    # Определяем размеры изображения
    width = 400
    height = 300

    # Создаем изображение
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Определяем центр смайлика
    center_x = width / 2
    center_y = height / 2

    # Определяем радиус смайлика
    radius = min(width, height) * 0.4

    # Определяем цвета
    yellow = (255, 255, 0)
    black = (0, 0, 0)

    # Отрисовываем круг
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=yellow, outline=black)

    # Определяем координаты глаз и рта
    eye_radius = radius * 0.15
    mouth_angle = math.pi / 6
    mouth_length = radius * 0.3
    left_eye_x = center_x - radius / 3
    right_eye_x = center_x + radius / 3
    eye_y = center_y - radius / 4

    # Отрисовываем глаза
    draw.ellipse((left_eye_x - eye_radius, eye_y - eye_radius, left_eye_x + eye_radius, eye_y + eye_radius), fill=black)
    draw.ellipse((right_eye_x - eye_radius, eye_y - eye_radius, right_eye_x + eye_radius, eye_y + eye_radius), fill=black)

    # Отрисовываем рот
    mouth_x1 = center_x + math.cos(mouth_angle) * mouth_length
    mouth_y1 = center_y + math.sin(mouth_angle) * mouth_length
    mouth_x2 = center_x - math.cos(mouth_angle) * mouth_length
    mouth_y2 = center_y + math.sin(mouth_angle) * mouth_length
    draw.line((mouth_x1, mouth_y1, mouth_x2, mouth_y2), fill=black, width=5)

    # Отображаем изображение
    image.show()
