from Maps.DungeonMap import *
from Actors.Actor import Actor

def test_map_instantiation():
    map = DungeonMap();
    grid = map.grid

    #test outside is walls
    for i in range(COLUMN_COUNT):
        assert(grid[0][i] == WALL) #top row
        assert(grid[ROW_COUNT-1][i] == WALL) #bottom row

    for i in range(ROW_COUNT):
        assert(grid[i][0] == WALL) #left col
        assert(grid[i][COLUMN_COUNT-1] == WALL) #right col

    #test inside is floors
    for i in range(1, ROW_COUNT-1):
        for j in range(1, COLUMN_COUNT-1):
            assert(grid[i][j] == FLOOR)

def test_get_tile_type():
    map = DungeonMap()

    assert(map.get_tile_type(0, 0) == WALL) # works with walls
    assert(map.get_tile_type(1, 1) == FLOOR) # works with floor

    assert(map.get_tile_type(ROW_COUNT + 1, COLUMN_COUNT + 1) == WALL) #no error and returns wall if off screen to upper right
    assert(map.get_tile_type(-(ROW_COUNT + 1), -(COLUMN_COUNT + 1)) == WALL) #no error and returns wall if off screen to lower left

def test_update_dungeon():
    map = DungeonMap()
    player = Actor(1, 1, arcade.color.BLUE)

    map.update_dungeon([player])

    assert(map.grid[1][1] == ACTOR) #works with a single actor

    player2 = Actor(2, 2, arcade.color.BLUE)
    map.update_dungeon([player, player2])
    assert(map.grid[1][1] == ACTOR) #works with a multiple actors
    assert(map.grid[2][2] == ACTOR) #works with a multiple actor

    map.update_dungeon([player])
    assert(map.grid[1][1] == ACTOR) #works with a multiple actors
    assert(map.grid[2][2] != ACTOR) #resets tiles after an actor moves off of them
