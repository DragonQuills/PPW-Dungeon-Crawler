from Actors.Actor import *

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
