from Actors.Actor import *

class Player(Actor):
    def __init__(self):
        x = (MARGIN + HEIGHT)+ MARGIN + HEIGHT // 2
        y = (MARGIN + HEIGHT)+ MARGIN + HEIGHT // 2

        super().__init__(x, y, arcade.color.TEAL)
