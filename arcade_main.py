"""
Main runner file.
Used to create a window and begining the game.
The code to run the game is in Views/GameView.py
"""

from definitions import arcade, SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT

from Views.InstructionView import InstructionView

def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # game_view = GameView()
    # game_view.setup()
    # window.show_view(game_view)
    instruction_view = InstructionView()
    window.show_view(instruction_view)
    arcade.run()


if __name__ == "__main__":
    main()
