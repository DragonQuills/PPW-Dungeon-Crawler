Kayden Adams <br>
Homework 5

1. What I Planned To Do <br>
Directly pulled from my last checkpoint:<br>
In short, I will complete MonsterSpawner so it can spawn monsters, have one room for the player to run around in, and have the ability to attack and kill (or be killed by) monsters.<br>


2. What I Actually Accomplished <br>
This time around I accomplished more than I set out to do! The game is fully playable now!
- <b>MonsterSpawner is complete: </b> I've finished creating a MonsterSpawner that follows the Factory pattern. It's responsible for creating monsters and also randomizes their stats slightly. It has an additional method that then finds a free location for that monster to spawn in at. Monsters spawn after a certain number of turns taken by the Player. I also made it in a way that it would be easy to spawn monsters of different levels or with different stats, or even new types of monsters if I extended functionality. There's also a test file for MonsterSpawner testing its different methods.
- <b>Attacking: </b> The Player and Monsters can now attack and deal damage to each other. The player attacks when they hit space, and will attack the space they're facing They have differing stats that make some monsters deal and take damage differently. Damage is also slightly randomized to make the game more interesting. When an attack happens, the damage dealt is printed to the text box at the bottom of the screen. I also checked if they player attacked a wall or the air, and output that. Monsters will only attack the player if they didn't spend their turn moving and are next to the player.
- <b>Monster and Player Death: </b> Monsters and the Player can now die. For monsters, the UI outputs a message and the monsters are removed from the list that tracks them. For the Player, death triggers a game over screen. There's a max amount of monsters that can be on the screen at a time defined in the definitions file.
- <b> Game Over and Restart: </b> Once the Player dies, the game goes to a Game Over screen, when it shows the number of turns the Player survived and lets the Player click to restart the game. Separate screens are done through Arcade Views. The game can be restarted any time the player loses, so it's now able to be played repeatedly without closing and reopening the window.
- <b> Title and Instruction Screen: </b> There is now a Title screen with the name of the game and my name. There's also a thorough instructions screen with details on what the Monsters and Player look like, how to move, how turns advance, and how to attack. Both screens are click-to-advance. The text on these screens and the GameOver screen is positioned according to the size of the window they're in, so if the window is made larger, they should still fit reasonably well. 

3. What I Had Planned For The Next Deadline <br>
No longer applicable since this is the last deadline.

4. Video Presentation <br>
The presentation video is in this folder, titled PPW_Final_Project.mp4
