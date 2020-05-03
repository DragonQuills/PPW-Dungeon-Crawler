"""
Main runner file.
Used to create a window and begining the game.
The code to run the game is in Views/GameView.py
"""

from definitions import arcade, SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT

from Views.TitleView import TitleView

def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    title_view = TitleView()
    window.show_view(title_view)
    arcade.run()


if __name__ == "__main__":
    main()
