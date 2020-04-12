from Actors.Actor import *
from Behaviors.MonsterAI import MonsterAI

class Monster(Actor):
    def __init__(self, row, col, color, dungeon_map):
        super().__init__(row, col, color)
        # the AI needs to know the layout of the dungeon to navigate
        self.ai = MonsterAI(dungeon_map)

    # overwritten to use the AI to determine the move to make
    def move(self, player, dungeon_map):
        next_move = self.ai.next_move(self, player)
        self.facing = self.determine_direction(next_move.row, next_move.col)

        #Checking for collisions with other monsters
        if dungeon_map.grid[next_move.row][next_move.col] == FLOOR:
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
