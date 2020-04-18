from Actors.Monster import *
from random import randint

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
