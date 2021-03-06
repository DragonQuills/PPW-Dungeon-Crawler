'''
Monster is the super-class that governs the behavior of monsters
using the AI. Individual monsters have different stats and colors.
'''

from Actors.Actor import *
from Behaviors.MonsterAI import MonsterAI

class Monster(Actor):
    def __init__(self, row, col, color, dungeon_map):
        super().__init__(row, col, color)
        # the AI needs to know the layout of the dungeon to navigate
        self.ai = MonsterAI(dungeon_map)

    '''
    Overwritten to use the AI to determine the move to make.
    Returns true if they AI spent their turn moving, false if not.
    If false, the AI might be able to attack (which will happen in the main runner)
    '''
    def move(self, player, dungeon_map):
        next_move = self.ai.next_move(self, player)

        # The AI says not to move, so just face the player
        if next_move.row == self.row and next_move.col == self.col:
            self.facing = self.determine_direction(player.row, player.col)
            return False
        # The AI says to move, so face the way we're moving
        else:
            self.facing = self.determine_direction(next_move.row, next_move.col)

        # Checking for collisions with other monsters
        if dungeon_map.grid[next_move.row][next_move.col] == FLOOR:
            self.row = next_move.row
            self.col = next_move.col
            return True
        return False

class SkullMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.BONE, dungeon_map)

        self.max_hp = 20
        self.curr_hp = self.max_hp
        self.attack = 15
        self.defense = 10

    def __str__(self):
        return "scary floating skull"

class LampMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.ALLOY_ORANGE, dungeon_map)
        self.max_hp = 15
        self.curr_hp = self.max_hp
        self.attack = 12
        self.defense = 15
    def __str__(self):
        return "giant robot lamp"

class FishMonster(Monster):
    def __init__(self, row, col, dungeon_map):
        super().__init__(row, col, arcade.color.AIR_SUPERIORITY_BLUE, dungeon_map)
        self.max_hp = 30
        self.curr_hp = self.max_hp
        self.attack = 12
        self.defense = 10
    def __str__(self):
        return "skeletal floating fish"
