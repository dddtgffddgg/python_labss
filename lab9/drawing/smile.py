import simple_draw as sd


def draw_smile(x, y, radius):
    # Рисуем лицо смайлика
    sd.circle(center_position=sd.get_point(x, y), radius=radius, width=0)

    # Рисуем левый глаз
    left_eye_position = sd.get_point(x - radius // 2, y + radius // 2)
    sd.circle(center_position=left_eye_position, radius=radius // 10, width=0)

    # Рисуем правый глаз
    right_eye_position = sd.get_point(x + radius // 2, y + radius // 2)
    sd.circle(center_position=right_eye_position, radius=radius // 10, width=0)

    # Рисуем рот
    mouth_start_position = sd.get_point(x - radius // 2, y - radius // 2)
    mouth_end_position = sd.get_point(x + radius // 2, y - radius // 2)
    sd.line(start_point=mouth_start_position, end_point=mouth_end_position, width=radius // 10)
