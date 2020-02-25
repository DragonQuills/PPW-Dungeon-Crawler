from Maps.DungeonMap import *

import pytest

a = arcade.Window()
a.test()

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
