from definitions import *

class DungeonMap():
    # Dungeon layout is currently hard-coded, I hope to fix this later
    def __init__(self):
        #create the array of what the tile types are
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

    def update_dungeon(self, old_actors, new_actors):
        # remove previous positions of actors
        if old_actors != []: #if we aren't just initializing the list for the first time
            for actor in old_actors:
                self.grid[actor.row][actor.col] = FLOOR
        # update the grid to track the positions of the actors
        for actor in new_actors:
            self.grid[actor.row][actor.col] = ACTOR


    def get_tile_type(self, row, col):
        # if in bounds
        if (row < ROW_COUNT and col < COLUMN_COUNT) and (row >= 0 and col >= 0):
            return self.grid[row][col]
        else: #outside of valid bounds is considered a wall.
            return WALL


    def draw(self):
        # creating the shapes first then drawing them in a batch is more efficent
        self.shape_list = arcade.ShapeElementList()
        for row in range(ROW_COUNT):
            for col in range(COLUMN_COUNT):
                # convert row and column to x and y for drawing
                x = (MARGIN + WIDTH) * col + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                current_rect = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, self.grid[row][col])

                self.shape_list.append(current_rect)
        self.shape_list.draw()
