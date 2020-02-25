from Maps.DungeonMap import *

def test_map_instantiation():
    map = DungeonMap(6, 6);
    grid = map.grid

    #test outside is walls
    for i in range(0, 6):
        assert(grid[0][i] == WALL) #top row
        assert(grid[5][i] == WALL) #bottom row
        assert(grid[i][0] == WALL) #top row
        assert(grid[i][5] == WALL) #bottom row
    #test inside is floors
    for i in range(1, 5):
        for j in range(1, 5):
            assert(grid[i][j] == FLOOR)
