from definitions import arcade, SCREEN_WIDTH, SCREEN_HEIGHT
from Views.GameView import GameView

'''
Code taken from https://arcade.academy/examples/view_instructions_and_game_over.html#view-instructions-and-game-over
A screen that shows after player death. It allows the player
to restart the game by clicking.
'''
class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.turns_survived = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", SCREEN_WIDTH/2, SCREEN_HEIGHT - 1.5*SCREEN_HEIGHT/10, arcade.color.WHITE, 54, anchor_x="center")
        arcade.draw_text("Click to restart", SCREEN_WIDTH/2, SCREEN_HEIGHT - 2.5*SCREEN_HEIGHT/10, arcade.color.WHITE, 24, anchor_x="center")

        arcade.draw_text("You survived " + str(self.turns_survived) + " turns!",
                         SCREEN_WIDTH/2,
                         SCREEN_HEIGHT - 4*SCREEN_HEIGHT/10,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
