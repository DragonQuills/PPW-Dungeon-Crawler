"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

import time
import copy

from definitions import *

from Maps.DungeonMap import DungeonMap
from Actors.Player import Player
from Actors.Monster import *
from UI.MessageLogger import MessageLogger

"""
Detects if the direction the player is trying to move to is valid
"""
def player_collision(player, direction, map):
    return(map.get_tile_type(player.row+direction[0], player.col+direction[1]) != FLOOR)



class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        """
        Initializes things like the window size and background color
        and declares all class variables
        """
        super().__init__(width, height, title)

        arcade.set_background_color(BACKGROUND_COLOR)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.map = None

        self.player = None
        self.monsters_list = None
        # Used to track the positions of all actors for collision detection.
        self.actors_list = None

        self.is_players_turn = None

        # Used to make the player move during the update step, which is best practice
        self.key_pressed = None
        self.key_modifiers = None

        # Used to make the monsters move after a slight delay and 1 by 1 instead
        # of them all swarming the player at once
        self.monster_move_timer = None
        self.monster_turn = None

        #UI stuff
        self.text_box = None
        self.message_logger = None


    def setup(self):
        """
        Initializes all class attributes
        """
        self.map = DungeonMap()
        self.player = Player()

        self.monsters_list = []
        self.monsters_list.append(LampMonster(4, 4, self.map))
        self.monsters_list.append(SkullMonster(5, 6, self.map))

        self.actors_list = []
        self.actors_list.append(self.player)
        self.actors_list.extend(self.monsters_list)

        self.map.update_dungeon([], self.actors_list)
        self.map.recreate_shapes()

        self.is_players_turn = True

        self.monster_move_timer = 0
        self.monster_turn = 0

        self.text_box = arcade.Sprite(":resources:gui_themes/Fantasy/TextBox/Brown.png", scale = 1, center_x = SCREEN_WIDTH/2, center_y = TEXT_BOX_HEIGHT/2)
        self.text_box.width = SCREEN_WIDTH + MARGIN
        self.text_box.height = TEXT_BOX_HEIGHT + MARGIN
        self.message_logger = MessageLogger.instance()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.map.draw()
        self.player.draw()
        for monster in self.monsters_list:
            monster.draw()

        self.text_box.draw()
        self.message_logger.draw(self.text_box.width/10, self.text_box.height - self.text_box.height/4, TEXT_SIZE)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        old_actors = copy.deepcopy(self.actors_list)

        if self.is_players_turn and self.key_pressed != None:
            self.player_turn(self.key_pressed, self.key_modifiers)
            self.key_pressed = None
            self.map.update_dungeon(old_actors, self.actors_list)
            self.map.recreate_shapes()

        old_actors = copy.deepcopy(self.actors_list)

        if not self.is_players_turn:
            self.monster_move_timer += 1

            if self.monster_move_timer > 5:
                if self.monster_turn < len(self.monsters_list):
                    self.monsters_list[self.monster_turn].move(self.player, self.map)
                    self.map.update_dungeon(old_actors, self.actors_list)
                    self.map.recreate_shapes()
                    self.monster_turn += 1
                    self.monster_move_timer = 0
                else:
                    self.monster_turn = 0
                    self.is_players_turn = True
            else:
                return;

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.is_players_turn:
            if key == arcade.key.UP or key == arcade.key.W:
                self.key_pressed = UP
                self.key_modifiers = modifiers
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.key_pressed = DOWN
                self.key_modifiers = modifiers
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.key_pressed = LEFT
                self.key_modifiers = modifiers
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.key_pressed = RIGHT
                self.key_modifiers = modifiers
            else:
                self.key_pressed = None
                self.key_modifiers = None

    # moves and/or changes the direction of the player based on the key pressed
    def player_turn(self, direction, key_modifiers):
        # we should always change the direction if the player hit an arrow key
        self.player.change_facing(direction)

        # if the player hit shift+arrow, they should change directions but not move
        # and the player's turn shouldn't end
        if(not player_collision(self.player, direction, self.map) and key_modifiers != arcade.key.MOD_SHIFT):
            self.player.move(direction)
            self.is_players_turn = False
            self.monster_move_timer = 0


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
