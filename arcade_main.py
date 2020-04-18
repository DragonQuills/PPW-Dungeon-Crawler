"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

import copy

from definitions import *

from Maps.DungeonMap import DungeonMap
from Actors.Player import Player
from Actors.Monster import *
from UI.MessageLogger import MessageLogger
from Spawners.MonsterSpawner import MonsterSpawner

"""
Detects if the direction the player is trying to move to is valid
"""
def player_collision(player, direction, map):
    return(map.get_tile_type(player.row+direction[0], player.col+direction[1]) != FLOOR)



class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        """
        Initializes things like the window size and background color
        and declares all class variables
        """
        super().__init__(width, height, title)

        arcade.set_background_color(BACKGROUND_COLOR)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.map = None

        self.player = None
        self.monsters_list = None
        # Used to track the positions of all actors for collision detection.
        self.actors_list = None

        self.is_players_turn = None

        # Used to make the player move during the update step, which is best practice
        self.key_pressed = None
        self.key_modifiers = None

        # Used to make the monsters move after a slight delay and 1 by 1 instead
        # of them all swarming the player at once
        self.monster_move_timer = None
        self.monster_turn = None

        #UI stuff
        self.text_box = None
        self.message_logger = None

        #used to spawn monsters
        self.spawner = None

        # Increments when the player takes a turn
        # Used to decide when to spawn in monsters
        # If I have time, also will spawn in heal tiles
        # and will provide the player a bonus at end of the game
        # based on how long they survived for
        self.turn_count = None


    def setup(self):
        """
        Initializes all class attributes
        """
        self.map = DungeonMap()

        self.player = Player()

        self.monsters_list = []
        self.monsters_list.append(LampMonster(4, 4, self.map))
        self.monsters_list.append(SkullMonster(5, 6, self.map))

        self.actors_list = []
        self.actors_list.append(self.player)
        self.actors_list.extend(self.monsters_list)

        self.map.update_dungeon([], self.actors_list)
        self.map.recreate_shapes()

        self.is_players_turn = True

        self.monster_move_timer = 0
        self.monster_turn = 0

        # The textbox uses a graphic that's included with Arcade
        self.text_box = arcade.Sprite(":resources:gui_themes/Fantasy/TextBox/Brown.png", scale = 1, center_x = SCREEN_WIDTH/2, center_y = TEXT_BOX_HEIGHT/2)
        self.text_box.width = SCREEN_WIDTH + MARGIN
        self.text_box.height = TEXT_BOX_HEIGHT + MARGIN
        self.message_logger = MessageLogger.instance()

        self.spawner = MonsterSpawner()

        self.turn_count = 0

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
        for monster in self.monsters_list:
            monster.draw()

        self.text_box.draw()
        # All the variables plus global variables should make it easier
        # to adjust this if I make the screen larger or smaller
        self.message_logger.draw(self.text_box.width/10, self.text_box.height - self.text_box.height/4, TEXT_SIZE)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        #this is needed by the map to replace the actor tiles with floor tiles
        old_actors = copy.deepcopy(self.actors_list)

        # if it is the player's turn and they pressed a valid key
        if self.is_players_turn and self.key_pressed != None:
            #do the player's action
            if self.key_pressed != arcade.key.SPACE:
                self.player_move(self.key_pressed, self.key_modifiers)
            else:
                attack_location = self.player.get_square_in_direction(self.player.facing)
                defender = self.get_actor_at_position(attack_location[0], attack_location[1])

                self.attack(self.player, defender)

            self.key_pressed = None

            # updating the dungeon so collisions can be detected when the monsters move
            self.map.update_dungeon(old_actors, self.actors_list)

            #this is just to show that the messager is working
            # message = "You moved to square (" + str(self.player.row) + ", " + str(self.player.col) + ")"
            # self.message_logger.push_message(message)

        old_actors = copy.deepcopy(self.actors_list)

        if not self.is_players_turn:
            # The move timer slows the monsters down so they don't all move at once
            self.monster_move_timer += 1

            if self.monster_move_timer > 7 - len(self.monsters_list * 2):
                # if there are still monsters who haven't taken their turn
                if self.monster_turn < len(self.monsters_list):
                    self.monsters_list[self.monster_turn].move(self.player, self.map)
                    self.map.update_dungeon(old_actors, self.actors_list)
                    self.monster_turn += 1
                    self.monster_move_timer = 0
                else:
                    self.monster_turn = 0
                    self.is_players_turn = True
            else:
                return;

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.is_players_turn:
            if key == arcade.key.UP or key == arcade.key.W:
                self.key_pressed = UP
                self.key_modifiers = modifiers
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.key_pressed = DOWN
                self.key_modifiers = modifiers
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.key_pressed = LEFT
                self.key_modifiers = modifiers
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.key_pressed = RIGHT
                self.key_modifiers = modifiers
            elif key == arcade.key.SPACE:
                self.key_pressed = arcade.key.SPACE
                self.key_modifiers = modifiers
            else:
                self.key_pressed = None
                self.key_modifiers = None

    '''
    Moves and/or changes the direction of the player based on the key pressed
    '''
    def player_move(self, direction, key_modifiers):
        # we should always change the direction if the player hit an arrow key
        self.player.change_facing(direction)

        # If the player hit shift+arrow, they should change directions but not move
        # and the player's turn shouldn't end
        if(not player_collision(self.player, direction, self.map) and key_modifiers != arcade.key.MOD_SHIFT):
            self.player.move(direction)
            self.player_end_of_turn()

    '''
    Uses the MonsterSpawner to spawn in a new monster
    '''
    def spawn_monster(self):
        monster = self.spawner.get_monster("random", self.map)
        monster = self.spawner.find_location_for_monster(monster, self.map, self.player)
        self.monsters_list.append(monster)
        self.actors_list.append(monster)

    '''
    Given a specific position, find the actor there
    Used for attacking.
    '''
    def get_actor_at_position(self, row, col):
        # check if there even is an actor there
        if self.map.grid[row][col] != ACTOR:
            return self.map.grid[row][col]
        for actor in self.actors_list:
            if actor.row == row and actor.col == col:
                return actor

    def attack(self, attacker, defender):
        # Attacked an invalid position, like a wall or the floor
        if defender == FLOOR:
            message = "You swing your sword at the air."
        elif defender == WALL:
            message = "Your sword clangs against the stone wall."
        # Attacked a monster
        else:
            damage = self.player.determine_damage(defender)
            defender.curr_hp -= damage
            message = "You attack the " + str(defender) + " for " + str(damage) + " damage."
            # self.message_logger.push_message(message)
            if defender.is_dead():
                self.message_logger.push_message(message)
                self.monsters_list.remove(defender)
                self.actors_list.remove(defender)
                message = "The " + str(defender) + " dies."


        self.message_logger.push_message(message)
        self.player_end_of_turn()

    def player_end_of_turn(self):
        self.is_players_turn = False
        self.turn_count += 1
        # If the correct number of tursn have passed
        # and we are under the cap for max monsters
        if self.turn_count % TURNS_BETWEEN_MONSTER_SPAWN == 0 and len(self.monsters_list) < MAX_MONSTERS:
            self.spawn_monster()
        self.monster_move_timer = 0



def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
