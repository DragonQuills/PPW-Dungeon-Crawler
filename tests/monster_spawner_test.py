from Spawners.MonsterSpawner import MonsterSpawner
from Maps.DungeonMap import DungeonMap

def test_spawner_get_monster():
    spawner = MonsterSpawner()
    dungeon = DungeonMap()

    fish = spawner.get_monster("fish", dungeon)

    assert( 9 <= fish.attack <= 11)
    assert( 9 <= fish.defense <= 11)
