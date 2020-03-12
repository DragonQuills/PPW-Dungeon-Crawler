from Actors.Actor import *

class Monster(Actor):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

class SkullMonster(Monster):
    def __init__(self, x, y):
        super().__init__(x, y, arcade.color.BONE)

class LampMonster(Monster):
    def __init__(self, x, y):
        super().__init__(x, y, arcade.color.ALLOY_ORANGE)

class FishMonster(Monster):
    def __init__(self, x, y):
        super().__init__(x, y, arcade.color.AIR_SUPERIORITY_BLUE)
