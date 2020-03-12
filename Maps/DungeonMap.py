from definitions import *

class DungeonMap():
    def __init__(self):
        #create the array of what the tule types are
        self.grid = []
        self.shape_list = None
        for row in range(ROW_COUNT):
            self.grid.append([])

            for col in range(COLUMN_COUNT):
                self.grid[row].append(WALL) #start off with every square a wall

        #make the inside floor tiles
        for row in range(1, ROW_COUNT-1):
            for col in range(1, COLUMN_COUNT-1):
                self.grid[row][col] = FLOOR

    def update_dungeon(self, actors):
        # update the grid to track the positions of the actors
        for actor in actors:
            self.grid[actor.row][actor.col] = ACTOR


    def get_tile_type(self, x, y):
        # Code from https://arcade.academy/examples/array_backed_grid_buffered.html#array-backed-grid-buffered
        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        if (row < ROW_COUNT and column < COLUMN_COUNT) and (row >= 0 and column >= 0):
            return self.grid[row][column]
        else:
            return WALL


    def draw(self):
        self.shape_list = arcade.ShapeElementList()
        for row in range(ROW_COUNT):
            for col in range(COLUMN_COUNT):
                x = (MARGIN + WIDTH) * col + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                if self.grid[row][col] != ACTOR:
                    current_rect = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, self.grid[row][col])
                else:
                    current_rect = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, FLOOR)

                self.shape_list.append(current_rect)
        self.shape_list.draw()
