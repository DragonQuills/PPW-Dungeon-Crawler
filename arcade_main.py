"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

from definitions import *

from Maps.DungeonMap import DungeonMap
from Actors.Player import Player
from Actors.Monster import *

# detects if the direction the player is trying to move to is valid
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
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.map = None

        self.player = None
        self.monsters_list = None
        self.actors_list = None

        self.is_players_turn = None

    def setup(self):
        # initializes all class attributes
        self.map = DungeonMap()
        self.player = Player()

        self.monsters_list = []
        self.monsters_list.append(LampMonster(4, 4, self.map))

        self.actors_list = []
        self.actors_list.append(self.player)
        self.actors_list.extend(self.monsters_list)

        self.map.update_dungeon(self.actors_list)

        self.is_players_turn = True

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
        self.monsters_list[0].draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if not self.is_players_turn:
            print("Player is at ", self.player.row, self.player.col)
            self.monsters_list[0].move(self.player)
            self.is_players_turn = True

        self.map.update_dungeon(self.actors_list)



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.is_players_turn:
            if key == arcade.key.UP:
                self.player_turn(UP, modifiers)
            elif key == arcade.key.DOWN:
                self.player_turn(DOWN, modifiers)
            elif key == arcade.key.LEFT:
                self.player_turn(LEFT, modifiers)
            elif key == arcade.key.RIGHT:
                self.player_turn(RIGHT, modifiers)

    # moves and/or changes the direction of the player based on the key pressed
    def player_turn(self, direction, key_modifiers):
        # we should always change the direction if the player hit an arrow key
        self.player.change_facing(direction)
        '''
        if the player hit shift+arrow, they should change directions but not move
        and the player's turn shouldn't end
        '''
        if(not player_collision(self.player, direction, self.map) and key_modifiers != arcade.key.MOD_SHIFT):
            self.player.move(direction)
            self.is_players_turn = False


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
