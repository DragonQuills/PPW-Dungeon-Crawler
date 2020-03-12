from Actors.Actor import *
from Behaviors.MonsterAI import MonsterAI

class Monster(Actor):
    def __init__(self, row, col, color, dungeon_map):
        super().__init__(row, col, color)
        self.ai = MonsterAI(dungeon_map)

class SkullMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.BONE, dungeon_map)

class LampMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.ALLOY_ORANGE, dungeon_map)

class FishMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.AIR_SUPERIORITY_BLUE, dungeon_map)
