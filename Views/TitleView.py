from definitions import arcade, SCREEN_WIDTH, SCREEN_HEIGHT
from Views.InstructionView import InstructionView

'''
Code taken from https://arcade.academy/examples/view_instructions_and_game_over.html#view-instructions-and-game-over
The opening screen with the title of the game
'''
class TitleView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Dungeon Delve", SCREEN_WIDTH/2, SCREEN_HEIGHT - 4*SCREEN_HEIGHT/10,
                         arcade.color.DARK_GOLDENROD, font_size=70, anchor_x="center")

        arcade.draw_text("Made by Kayden Adams", SCREEN_WIDTH/2, SCREEN_HEIGHT - 5*SCREEN_HEIGHT/10,
                         arcade.color.OLD_SILVER, font_size=30, anchor_x="center")

        arcade.draw_text("Click anywhere to start.", SCREEN_WIDTH/2, SCREEN_HEIGHT - 9*SCREEN_HEIGHT/10,
                         arcade.color.OLD_SILVER, font_size=20, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instruction_view = InstructionView()
        self.window.show_view(instruction_view)
