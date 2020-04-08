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

def player_collision(player, direction, map):
    return(map.get_tile_type(player.row+direction[0], player.col+direction[1]) != FLOOR)



class MyGame(arcade.Window):
    """
    Main application class.
player
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

    def setup(self):
        self.map = DungeonMap()
        self.player = Player()

        self.monsters_list = []
        self.monsters_list.append(LampMonster(4, 4, self.map))

        self.actors_list = []
        self.actors_list.append(self.player)
        self.actors_list.extend(self.monsters_list)

        self.map.update_dungeon(self.actors_list)
        # Create your sprites and sprite lists here

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
        self.actors_list = []
        self.actors_list.append(self.player)
        self.actors_list.extend(self.monsters_list)
        self.map.update_dungeon(self.actors_list)
        pass

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            player_turn(UP)
        elif key == arcade.key.DOWN:
            player_turn(DOWN)
        elif key == arcade.key.LEFT:
            player_turn(LEFT)
        elif key == arcade.key.RIGHT:
            player_turn(RIGHT)

    def player_turn(direction, key_modifiers):
        self.player.change_facing(direction)
        if(not player_collision(self.player, direction, self.map) and key_modifiers != arcade.key.MOD_SHIFT):
            self.player.move(direction)
            self.monsters_list[0].move(self.player)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
