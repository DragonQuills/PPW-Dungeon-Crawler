from definitions import *

class Actor(arcade.Sprite):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self._color = color

    def get_x_y(self):
        x = (MARGIN + WIDTH) * self.col + MARGIN + WIDTH // 2
        y = (MARGIN + HEIGHT) * self.row + MARGIN + HEIGHT // 2
        return [x, y]

    def draw(self):
        x, y = self.get_x_y()
        icon = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, self.color)
        icon.draw()

    def move(self, direction):
        self.row += direction[0]
        self.col += direction[1]
