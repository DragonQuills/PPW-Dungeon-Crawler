import arcade



class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)

    def setup(self):
        arcade.set_background_color(arcade.color.AMETHYST)
        self.text_box = arcade.Sprite(":resources:gui_themes/Fantasy/TextBox/Brown.png", scale = 1.7, center_x = 400, center_y = 300)
        # self.text_box.height = 96
        # self.text_box.width = 800
    def on_draw(self):
        arcade.start_render()
        super().on_draw()
        self.text_box.draw()


def main():
    window = Window()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
