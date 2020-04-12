import arcade


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600)
        self.text = ""
        self.center_x = self.width / 2
        self.center_y = self.height / 2

    def setup(self):
        arcade.set_background_color(arcade.color.AMETHYST)
        self.text_box = arcade.Sprite(":resources:gui_themes/Fantasy/TextBox/LightBrown.png")

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
