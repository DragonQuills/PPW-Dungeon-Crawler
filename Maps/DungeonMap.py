import arcade

FLOOR = arcade.color.ASH_GREY
WALL = arcade.color.BLACK

class DungeonMap():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = []
        for row in range(self.rows):
            self.grid.append([])

            for col in range(self.cols):
                self.grid[row].append(WALL) #start off with every square a wall

        #make the inside floor tiles
        for row in range(1, self.rows-1):
            for col in range(1, self.cols-1):
                self.grid[row][col] = FLOOR
