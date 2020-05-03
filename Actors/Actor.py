'''
Actor is the parent class for anything that moves around the board
such as monsters of the player. It handles the logic for
movement, drawing, changing direction, and calculating damage,
among other things.
'''

from definitions import *
from random import randint

class Actor(arcade.Sprite):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self._color = color
        self.facing = DOWN

        # Attack attributes
        self.max_hp = None
        self.curr_hp = None
        self.attack = None
        self.defense = None

    '''
    This converts the actor's current row and column to an x and y that arcade uses to draw the actor
    '''
    def get_x_y(self):
        x = (MARGIN + WIDTH) * self.col + MARGIN + WIDTH // 2
        y = (MARGIN + HEIGHT) * self.row + MARGIN + HEIGHT // 2 + TEXT_BOX_HEIGHT
        return [x, y]

    def draw(self, x = -1, y = -1):
        # During gameplay, x and y should never be set.
        # The only time they are passed in as arguments
        # is on the instruction screen where the actor needs
        # to be drawn in a specific location
        if(x == -1 and y == -1):
            x, y = self.get_x_y()

        # draw the main body of the actor
        icon = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, self.color)
        icon.draw()
        # draw a mini square to show which direction the actor is facing
        face = arcade.create_rectangle_filled(x+self.facing[1]*(WIDTH/2 - 5), y+self.facing[0]*(WIDTH/2 - 5), 10, 10, arcade.color.AFRICAN_VIOLET)
        face.draw()

    def move(self, direction):
        self.row += direction[0]
        self.col += direction[1]

    def change_facing(self, direction):
        self.facing = direction

    '''
    Given a row and column, determines if that space is next to the actor,
    and if so returns the direction the square is.
    '''
    def determine_direction(self, row, col):
        temp_row = row - self.row
        temp_col = col - self.col
        if [temp_row, temp_col] in [UP, DOWN, LEFT, RIGHT]:
            return [temp_row, temp_col]
        else:
            return NULL

    '''
    Calculates damage this actor does to another actor
    Does not change the stats of this or the other actor.
    '''
    def determine_damage(self, other_actor):
        #slight stat randomization
        return (self.attack - other_actor.defense) + randint(-2, 2)

    '''
    Given a direction (up, down, left, right), returns the row and col
    of the square next to the actor in that direction
    '''
    def get_square_in_direction(self, direction):
        row = self.row + direction[0]
        col = self.col + direction[1]
        return [row, col]

    def is_dead(self):
        return self.curr_hp <= 0
