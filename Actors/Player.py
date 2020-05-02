from Actors.Actor import *

class Player(Actor):
    def __init__(self):
        row = 1
        col = 1

        super().__init__(row, col, arcade.color.TEAL)

        self.max_hp = 60
        self.curr_hp = self.max_hp
        self.attack = 20
        self.defense = 8
    def __str__(self):
        return "brave and noble player"
