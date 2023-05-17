import simple_draw as sd

class Snowflake:
    def create(self):
        self.x = sd.random_number(0, sd.resolution[0])  # Random starting X coordinate
        self.y = sd.resolution[1]  # Starting Y coordinate (at the bottom of the screen)
        self.length = sd.random_number(10, 40)  # Length of the snowflake
        self.factor_a = sd.random_number(1, 10) / 10  # Horizontal amplitude factor
        self.factor_b = sd.random_number(1, 10) / 10  # Vertical amplitude factor
        self.factor_c = sd.random_number(10, 60)  # Speed factor

    def clear_previous_picture(self):
        sd.start_drawing()
        point = sd.get_point(self.x, self.y)
        sd.snowflake_center(point, self.length, sd.background_color)
        sd.finish_drawing()

    def move(self):
        self.x += sd.random_number(-2, 2)  # Add some horizontal variation
        self.y -= self.factor_c  # Move the snowflake upwards

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.start_drawing()
        sd.snowflake_center(point, self.length, sd.COLOR_WHITE)
        sd.finish_drawing()

    def can_fall(self):
        return self.y > 0  # Check if the snowflake is still within the screen bounds

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
