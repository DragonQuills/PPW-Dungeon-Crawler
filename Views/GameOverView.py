from definitions import arcade, SCREEN_WIDTH, SCREEN_HEIGHT
from Views.GameView import GameView

'''
Code taken from https://arcade.academy/examples/view_instructions_and_game_over.html#view-instructions-and-game-over
'''
class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)

        # arcade.draw_text(f"Time taken: {time_taken_formatted}",
        #                  WIDTH/2,
        #                  200,
        #                  arcade.color.GRAY,
        #                  font_size=15,
        #                  anchor_x="center")

        # output_total = f"Total Score: {self.window.total_score}"
        # arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
