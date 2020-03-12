from Actors.Actor import *

class Monster(Actor):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

class SkullMonster(Monster):
    def __init__(self, row, col):
        super().__init__(row, col, arcade.color.BONE)

class LampMonster(Monster):
    def __init__(self, row, col):
        super().__init__(row, col, arcade.color.ALLOY_ORANGE)

class FishMonster(Monster):
    def __init__(self, row, col):
        super().__init__(row, col, arcade.color.AIR_SUPERIORITY_BLUE)
