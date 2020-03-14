# Dungeon Delve
A dungeon crawler built in Python Arcade. My final project for CSCI 3010, Programming Project Workshop at CU Boulder.

[![Build Status](https://travis-ci.com/DragonQuills/PPW-Dungeon-Crawler.svg?branch=master)](https://travis-ci.com/DragonQuills/PPW-Dungeon-Crawler)

## Installation
First, download this project. Then, from the command line in the PPW-Dungeon-Crawler folder, run

    $ python3 arcade_main.py

## How To Play
After booting up the program (using the command listed above) use the arrow keys to move the player. Grey tiles represent the floor and black represent walls. The player is teal, the monster is orange. The monster will follow the player and quite likely trap them, currently resulting in a restart because there is no attack functionality and the dungeon is a very small room.

### Dependencies
Dungeon Delve is build for Python 3.6+. Arcade only supports Python 3.6+ so this will not run in anything below that!

Dungeon Delve relies on [Python Arcade](https://arcade.academy/) which can be installed with

    $ python3 -m pip install arcade

I used [pytest](https://docs.pytest.org/en/latest/) to do testing, which can be installed with

    $ python3 -m pip install -U pytest
