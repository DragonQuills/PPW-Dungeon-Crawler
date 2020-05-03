"""
This information is used throughout the application
and every class needs access to arcade at a minimum
o it's all in this file instead of me having to
seperately import or define thes things is multiple
places.
"""

import arcade

# Set how many rows and columns we will have
ROW_COUNT = 15
COLUMN_COUNT = 15

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 48
HEIGHT = 48

# The height of the text box at the bottom of the screen
TEXT_BOX_HEIGHT = 128

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 1

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + TEXT_BOX_HEIGHT
SCREEN_TITLE = "Dungeon Delve"

#Colors for the dungeon tiles
FLOOR = arcade.color.ASH_GREY
WALL = arcade.color.BLACK
ACTOR = arcade.color.PINK

BACKGROUND_COLOR = arcade.color.DARK_BROWN

# UI definitions
TEXT_SIZE = 17
MAX_MESSAGES_ON_SCREEN = 6

#Movement definitions
UP = [1, 0]
DOWN = [-1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]
NULL = [0, 0]

# Sort of a difficulty level - lower turns b/w mean monsters spawn more often
# while higher max monsters lets more monsters be on screen at once.
# TODO: Spawn_distance is how close to the player the monster can be at minimum
# MONSTERS_AT_START is how many mosntres spawn at the very begining of the game
TURNS_BETWEEN_MONSTER_SPAWN = 10
MAX_MONSTERS = 5
SPAWN_DISTANCE_FROM_PLAYER = 10
MONSTERS_AT_START = 3
