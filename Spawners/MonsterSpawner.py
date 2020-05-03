'''
Uses the factory pattern to create monsters with randomized stats,
and can then place them on the grid.
'''

from Actors.Monster import *
from Behaviors.MonsterAI import Position, MonsterAI
from random import randint, choice

class MonsterSpawner:
    '''
    Gets a monster with slightly randomized stats.
    If an invalid name is given, returns a monster at random.
    '''
    def get_monster(self, monster_name, dungeon_map):
        monster = None
        if monster_name == "skull":
            monster = SkullMonster(0, 0, dungeon_map)
        elif monster_name == "lamp":
            monster = LampMonster(0, 0, dungeon_map)
        elif monster_name == "fish":
            monster = FishMonster(0, 0, dungeon_map)
        else:
            rand = randint(0, 2)
            if rand == 0:
                monster = SkullMonster(0, 0, dungeon_map)
            elif rand == 2:
                monster = LampMonster(0, 0, dungeon_map)
            else:
                monster = FishMonster(0, 0, dungeon_map)



        #slight stat randomization
        monster.attack += randint(-1, 1)
        monster.defense += randint(-1, 1)

        return monster

    '''
    Uses the dungeon map and the position of the player to find a place
    for the monster to spawn in.
    The monster should always spawn on a floor
    TODO: spawn at least 10 tiles away from the player
    '''
    def find_location_for_monster(self, monster, dungeon_map, player):
        valid_locations = []
        for row in range(0, ROW_COUNT):
            for col in range(0, COLUMN_COUNT):
                # Make sure the tile is a floor and not too close to the player
                # checking player distance isn't working yet, it is a TODO
                if(dungeon_map.grid[row][col] == FLOOR and len(monster.ai.solve(monster, player)) >= SPAWN_DISTANCE_FROM_PLAYER):
                    valid_locations.append(Position(row, col))
        position = choice(valid_locations)
        monster.row = position.row
        monster.col = position.col
        return monster
