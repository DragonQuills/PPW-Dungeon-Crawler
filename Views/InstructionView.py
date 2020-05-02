from definitions import arcade, SCREEN_WIDTH, SCREEN_HEIGHT
from Views.GameView import GameView
from Actors.Player import Player
from Actors.Monster import *

'''
Code taken from https://arcade.academy/examples/view_instructions_and_game_over.html#view-instructions-and-game-over
A start screen that shows instructions on how to play the game.
'''
class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AUROMETALSAURUS)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH/2, SCREEN_HEIGHT - 1.5*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        arcade.draw_text("You look like this: ", SCREEN_WIDTH/20, SCREEN_HEIGHT- 2.5*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=12, anchor_x="left")
        arcade.draw_text("The monsters look like this: ", SCREEN_WIDTH/20, SCREEN_HEIGHT- 3.5*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=12, anchor_x="left")

        arcade.draw_text("The game is turn based. You take your turn by attacking or moving.",
                         SCREEN_WIDTH/20, SCREEN_HEIGHT- 4.5*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=12, anchor_x="left")
        arcade.draw_text("Changing direction won't advance your turn, but attacking always will.",
                         SCREEN_WIDTH/20, SCREEN_HEIGHT- 5*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=12, anchor_x="left")
        arcade.draw_text("Use the arrow keys to move.",
                         SCREEN_WIDTH/20, SCREEN_HEIGHT- 5.5*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=12, anchor_x="left")
        arcade.draw_text("Shift+arrow key will change the direction you're facing without moving you.",
                         SCREEN_WIDTH/20, SCREEN_HEIGHT- 6*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=12, anchor_x="left")
        arcade.draw_text("Space will attack in whatever direction you're facing.",
                         SCREEN_WIDTH/20, SCREEN_HEIGHT- 6.5*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=12, anchor_x="left")

        arcade.draw_text("Survive as many turns as you can!", SCREEN_WIDTH/2, SCREEN_HEIGHT- 8.2*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT- 9*SCREEN_HEIGHT/10,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
