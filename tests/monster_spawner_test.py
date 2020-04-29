from Actors.Monster import FishMonster
from Actors.Player import Player
from Spawners.MonsterSpawner import MonsterSpawner
from Maps.DungeonMap import DungeonMap
from definitions import FLOOR, SPAWN_DISTANCE_FROM_PLAYER

def test_spawner_get_monster():
    spawner = MonsterSpawner()
    dungeon = DungeonMap()

    fish = spawner.get_monster("fish", dungeon)

    assert( isinstance(fish, FishMonster) )
    assert( 11 <= fish.attack <= 13)
    assert( 9 <= fish.defense <= 11)

# Testing to make sure the monster is now spawning too close to the player or inside of a wall
def test_find_location_for_monster():
    spawner = MonsterSpawner()
    player = Player()
    dungeon = DungeonMap()
    dungeon.update_dungeon([player], [player])

    fish = spawner.get_monster("fish", dungeon)

    fish = spawner.find_location_for_monster(fish, dungeon, player)

    # making sure they aren't in a wall or on a different actor
    assert(dungeon.grid[fish.row][fish.col] == FLOOR)

    # using the monster AI to tell how far we are from the player
    assert( len(fish.ai.solve(fish, player)) >= SPAWN_DISTANCE_FROM_PLAYER )
