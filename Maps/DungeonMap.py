from definitions import *

FLOOR = arcade.color.ASH_GREY
WALL = arcade.color.BLACK

class DungeonMap():
    def __init__(self):
        #create the array of what the tule types are
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])

            for col in range(COLUMN_COUNT):
                self.grid[row].append(WALL) #start off with every square a wall

        #make the inside floor tiles
        for row in range(1, ROW_COUNT-1):
            for col in range(1, COLUMN_COUNT-1):
                self.grid[row][col] = FLOOR

        # now make the actual grid that will be displayed
        self.shape_list = arcade.ShapeElementList()
        for row in range(ROW_COUNT):
            for col in range(COLUMN_COUNT):
                x = (MARGIN + WIDTH) * col + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                current_rect = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, self.grid[row][col])
                self.shape_list.append(current_rect)

    def draw(self):
        self.shape_list.draw()
