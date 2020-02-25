import arcade

FLOOR = arcade.color.ASH_GREY
WALL = arcade.color.BLACK


class DungeonMap:
    def __init__(self, rows, cols):
        self.grid = []
        for row in range(0, rows):
            self.grid.append([])

            for col in range(0, cols):
                self.grid[row].append(WALL) #start off with every square a wall

        #make the inside floor
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                self.grid[row][col] = FLOOR
