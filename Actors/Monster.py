from Actors.Actor import *
from Behaviors.MonsterAI import MonsterAI

class Monster(Actor):
    def __init__(self, row, col, color, dungeon_map):
        super().__init__(row, col, color)
        self.ai = MonsterAI(dungeon_map)

    def move(self, player):
        next_move = self.ai.next_move(self, player)
        self.facing = self.determine_direction(next_move.row, next_move.col)
        self.row = next_move.row
        self.col = next_move.col

class SkullMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.BONE, dungeon_map)

class LampMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.ALLOY_ORANGE, dungeon_map)

class FishMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.AIR_SUPERIORITY_BLUE, dungeon_map)
