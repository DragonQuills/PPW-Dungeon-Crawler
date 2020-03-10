from Maps.DungeonMap import *

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
    map = DungeonMap();

    assert(map.get_tile_type(33, 33) == WALL) # works when given the center of the square
    assert(map.get_tile_type(34, 34) == WALL) #works when given something off center
    assert(map.get_tile_type(98, 98) == FLOOR) # works when given the center of the square
    assert(map.get_tile_type(99, 99) == FLOOR) #works when given something off center

    assert(map.get_tile_type(1000000, 1000000) == WALL) #no error and returns wall if off screen to upper right
    assert(map.get_tile_type(-1000000, -1000000) == WALL) #no error and returns wall if off screen to lower left
