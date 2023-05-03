import simple_draw as sd
import random

def snowflake(center, length):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=center, angle=0, length=length, width=1)
    v1.draw()
    v2 = sd.get_vector(start_point=center, angle=120, length=length, width=1)
    v2.draw()
    v3 = sd.get_vector(start_point=center, angle=240, length=length, width=1)
    v3.draw()
    next_length = length * 0.75
    snowflake(center=v1.end_point, length=next_length)
    snowflake(center=v2.end_point, length=next_length)
    snowflake(center=v3.end_point, length=next_length)

sd.resolution = (800, 800)
sd.background_color = sd.COLOR_BLACK

for _ in range(10):
    point = sd.get_point(random.randint(0, 800), random.randint(0, 800))
    snowflake(center=point, length=100)

sd.pause()
