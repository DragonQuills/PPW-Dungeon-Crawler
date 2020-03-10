from definitions import *

class Player(arcade.Sprite):
    def __init__(self):
        self.x = (MARGIN + HEIGHT)+ MARGIN + HEIGHT // 2
        self.y = (MARGIN + HEIGHT)+ MARGIN + HEIGHT // 2

    def draw(self):
        icon = arcade.create_rectangle_filled(self.x, self.y, WIDTH, HEIGHT, arcade.color.TEAL)
        icon.draw()

    def move(self, direction):
        self.x += direction[0]
        self.y += direction[1]
