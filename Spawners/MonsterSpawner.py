from Actors.Monster import *
from Behaviors.MonsterAI import Position, MonsterAI
from random import randint, choice

class MonsterSpawner:
    def get_monster(self, monster_name, dungeon_map):
        monster = None
        if monster_name == "skull":
            monster = SkullMonster(0, 0, dungeon_map)
        elif monster_name == "lamp":
            monster = LampMonster(0, 0, dungeon_map)
        elif monster_name == "fish":
            monster = FishMonster(0, 0, dungeon_map)
        else:
            return None

        #slight stat randomization
        monster.attack += randint(-1, 1)
        monster.defense += randint(-1, 1)

        return monster


    def find_location_for_monster(self, monster, dungeon_map, player):
        valid_locations = []
        for row in range(0, ROW_COUNT):
            for col in range(0, COLUMN_COUNT):
                #quicker check first
                if(dungeon_map.grid[row][col] == FLOOR and len(monster.ai.solve(monster, player)) >= 10):
                    valid_locations.append(Position(row, col))
        position = choice(valid_locations)
        monster.row = position.row
        monster.col = position.col
        return monster
