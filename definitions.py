import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 64
HEIGHT = 64

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 1

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Dungeon Delve"

#Colors for the dungeon tiles
FLOOR = arcade.color.ASH_GREY
WALL = arcade.color.BLACK
ACTOR = arcade.color.PINK

UP = [1, 0]
DOWN = [-1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]
NULL = [0, 0]
