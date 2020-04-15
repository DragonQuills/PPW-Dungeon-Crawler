# Dungeon Delve
A dungeon crawler built in Python Arcade. My final project for CSCI 3010, Programming Project Workshop at CU Boulder.

[![Build Status](https://travis-ci.com/DragonQuills/PPW-Dungeon-Crawler.svg?branch=master)](https://travis-ci.com/DragonQuills/PPW-Dungeon-Crawler)

## Installation
First, download this project. Then, from the command line in the PPW-Dungeon-Crawler folder, run

    $ python3 arcade_main.py

## How To Play
After booting up the program (using the command listed above) use the arrow keys to move the player. Grey tiles represent the floor and black represent walls. The player is teal, the monsters are orange and white. The purple square represents the direction the player or a monster is facing. The monsters will follow the player around the room. The text box at the bottom currently only outputs the player's position, but will later be used to display damage from attacks.

## System Requirements
Dungeon Delve will run on a Linux or Mac machine.

### Dependencies
Dungeon Delve is built for Python 3.6+. Arcade only supports Python 3.6+ so this will not run in anything below that! This means that you'll need to install Python if you don't already have it.

Dungeon Delve also relies on [Python Arcade](https://arcade.academy/) which can be installed with

    $ python3 -m pip install arcade

I used [pytest](https://docs.pytest.org/en/latest/) to do testing, which can be installed with

    $ python3 -m pip install -U pytest
