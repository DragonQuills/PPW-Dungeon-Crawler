from Actors.Actor import *
from Actors.Monster import *
from Actors.Player import Player
from definitions import UP, DOWN, LEFT, RIGHT

def test_determine_direction():
    actor = Actor(1, 1, arcade.color.PINK)

    #test all directions work
    assert(actor.determine_direction(0, 1) == DOWN)
    assert(actor.determine_direction(2, 1) == UP)
    assert(actor.determine_direction(1, 2) == RIGHT)
    assert(actor.determine_direction(1, 0) == LEFT)

    #test invalid direction is null
    assert(actor.determine_direction(0, 0) == NULL)
    assert(actor.determine_direction(1, 1) == NULL)

def test_determine_damage():
    dungeon_map = ""

    player = Player()
    skull = SkullMonster(0, 0, dungeon_map)

    # Should be 10 because player.attack - skull.defense is 10
    assert( 8 <= player.determine_damage(skull) <= 12)

def test_get_square_in_direction():
    actor = Actor(1, 1, arcade.color.PINK)

    assert(actor.get_square_in_direction(UP) == [2, 1] )
    assert(actor.get_square_in_direction(DOWN) == [0, 1] )
    assert(actor.get_square_in_direction(LEFT) == [1, 0] )
    assert(actor.get_square_in_direction(RIGHT) == [1, 2] )

    actor.row = 10
    actor.col = 8
    actor.change_facing(UP)

    assert(actor.get_square_in_direction(actor.facing) == [11, 8])
