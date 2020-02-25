"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
# import sys
# sys.path.insert(1, '/Actors')
# sys.path.insert(1, '/Behaviors')
# sys.path.insert(1, '/Maps')
# sys.path.insert(1, '/Spawners')

from definitions import *

from Maps.DungeonMap import DungeonMap


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

        self.map = DungeonMap()

        self.player_x = (MARGIN + HEIGHT)+ MARGIN + HEIGHT // 2
        self.player_y = (MARGIN + HEIGHT)+ MARGIN + HEIGHT // 2
        self.player = arcade.create_rectangle_filled(self.player_x, self.player_y, WIDTH, HEIGHT, arcade.color.TEAL)

    def setup(self):
        # Create your sprites and sprite lists here
        pass

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

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player = arcade.create_rectangle_filled(self.player_x, self.player_y, WIDTH, HEIGHT, arcade.color.TEAL)
        pass

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_y += (MARGIN+HEIGHT)
        elif key == arcade.key.DOWN:
            self.player_y -= (MARGIN+HEIGHT)
        elif key == arcade.key.LEFT:
            self.player_x -= (MARGIN+HEIGHT)
        elif key == arcade.key.RIGHT:
            self.player_x += (MARGIN+HEIGHT)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
