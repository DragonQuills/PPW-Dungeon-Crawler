from definitions import *

class Actor(arcade.Sprite):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self._color = color
        self.facing = DOWN

    def get_x_y(self):
        x = (MARGIN + WIDTH) * self.col + MARGIN + WIDTH // 2
        y = (MARGIN + HEIGHT) * self.row + MARGIN + HEIGHT // 2
        return [x, y]

    def draw(self):
        x, y = self.get_x_y()
        icon = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, self.color)
        icon.draw()
        face = arcade.create_rectangle_filled(x+self.facing[1]*27, y+self.facing[0]*27, 10, 10, arcade.color.AFRICAN_VIOLET)
        face.draw()

    def move(self, direction):
        self.row += direction[0]
        self.col += direction[1]

    def change_facing(self, direction):
        self.facing = direction
