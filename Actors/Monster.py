from definitions import *

class Monster(arcade.Sprite):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        icon = arcade.create_rectangle_filled(self.x, self.y, WIDTH, HEIGHT, self.color)
        icon.draw()

    def move(self, direction):
        self.x += direction[0]
        self.y += direction[1]
