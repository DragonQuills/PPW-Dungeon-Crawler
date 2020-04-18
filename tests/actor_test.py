from Actors.Actor import *
from Actors.Monster import *
from Actors.Player import Player

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
    assert( player.determine_damage(skull) == 10)
