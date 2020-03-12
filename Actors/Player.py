from Actors.Actor import *

class Player(Actor):
    def __init__(self):
        row = 1
        col = 1

        super().__init__(row, col, arcade.color.TEAL)
