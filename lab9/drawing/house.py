import simple_draw as sd


def draw_brick_house_with_window(start_point, width, height, window_size):
    # отрисовка основной стены дома
    left_bottom = start_point
    right_top = sd.get_point(start_point.x + width, start_point.y + height)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_ORANGE, width=0)

    # отрисовка окна
    window_left_bottom = sd.get_point(start_point.x + width / 3, start_point.y + height / 3)
    window_right_top = sd.get_point(window_left_bottom.x + window_size, window_left_bottom.y + window_size)
    sd.rectangle(left_bottom=window_left_bottom, right_top=window_right_top, color=sd.COLOR_WHITE, width=0)
    sd.rectangle(left_bottom=window_left_bottom, right_top=window_right_top, color=sd.COLOR_BLACK, width=2)

    # отрисовка смайлика в окне
    smile_center = sd.get_point(window_left_bottom.x + window_size / 2, window_left_bottom.y + window_size / 2)
    sd.circle(center_position=smile_center, radius=window_size / 4, color=sd.COLOR_YELLOW, width=0)
    sd.circle(center_position=smile_center, radius=window_size / 4, color=sd.COLOR_BLACK, width=2)
    left_eye_center = sd.get_point(window_left_bottom.x + window_size / 3, window_left_bottom.y + window_size / 1.7)
    right_eye_center = sd.get_point(window_left_bottom.x + window_size / 1.5, window_left_bottom.y + window_size / 1.7)
    sd.circle(center_position=left_eye_center, radius=window_size / 12, color=sd.COLOR_BLACK, width=0)
    sd.circle(center_position=right_eye_center, radius=window_size / 12, color=sd.COLOR_BLACK, width=0)
    mouth_start = sd.get_point(window_left_bottom.x + window_size / 3, window_left_bottom.y + window_size / 3)
    mouth_end = sd.get_point(window_left_bottom.x + window_size / 1.5, window_left_bottom.y + window_size / 3)
    sd.line(start_point=mouth_start, end_point=mouth_end, color=sd.COLOR_BLACK, width=2)
