Kayden Adams <br>
Homework 3

1. What I Planned To Do <br>
Directly pulled from my last checkpoint:<br>
In short, during my next sprint I will complete MonsterSpawner, attack functionality, and a basic UI to show damage being dealt and the Player's current health and exp.<br>


2. What I Actually Accomplished <br>
As I mentioned in my HW3 checkpoint, there were a lot of "little" things that I needed to complete in preparation for the MonsterSpawner and attack functionality. Those things all got done, and turned out to not be so little. <br>
- <b>The Monsters and Player can now change directions:</b> Included in this is that holding shift+arrow key changes the player's direction without them moving at all. A new method, determine_direction was added to let monsters face the player more easily.This is needed for attacking to be able to happen.
- <b>Turn-based functionality:</b> This was actually way harder than I thought it would be and I had to do a lot of research. Arcade is really meant for real-time games, which I didn't realize when I started using it, and getting certain parts of the game to "wait" without stopping essential stuff like the graphics rendering or the game reading input was harder than I thought. And there was a huge issue with the monsters not being able to "see" the player and so not moving at all. But now there are dedicated player and monster turns, and the player can't interrupt. There's also a small delay between the player moving and each of the monsters moving, so that everything doesn't all move at once. This not only looks and feels a lot better, but it's essential setup for the player and monsters being able to attack.
- <b>Following Arcade Best-Practices and Optimizations: </b>
After I tried increasing the size of the dungeon and adding another actor, things seriously slowed down. The frame rate was lagging horrendously. So I did some research and realized that I was doing some very inefficient things that I fixed. I was recreating the entire dungeon every time I drew it, which was a terrible idea since drawing happens about 60 times a second. I also was iterating over every single square in the dungeon to remove the actors previous location, which is very silly so now I just pass in the previous location and clear those squares. Finally, I moved the player-movement into the update function, which is where Arcade wants code around movement to be located.
- <b> Comments and Cleaner Code: </b> Sreesha noted that I hadn't really commented my code at all, and I realized that was completely true and went through and fixed it. Significantly more of my classes, methods, and confusing parts of my code have comments now to explain their purpose or how they work. I also cleaned up the code by moving things around, abstracting repeated code to functions, and deleting old print statements or unneeded imports and variables.
- <b> Text-UI: </b> I created a text-box at the bottom of the screen that can be used to display information to the player, like when they dealt or took damage. I also made the UI a Singleton, which I think makes perfect sense for a UI since the player and main runner and monsters all should be sending messages to the same object. Currently the UI is just printing the player's position to show that it works.

3. What I Had Planned For The Next Deadline <br>
My original plan to get done by the final deadline was largely getting sprites, animations, and the UI done. I also wanted to add sounds and music. My goal now is to have a playable framework for a game. I think for the attacking, instead of worrying about scaling and formulas, I'm just going to stick in flat numbers and ignore leveling up. I will still create a monster factory to spawn in monsters. And the most important part, being able to attack and kill monsters or die and restart, will also work. I don't think I'm going to have time to make different dungeon floors so I'm just going to have one room as sort of a proof of concept.

In short, I will complete MonsterSpawner so it can spawn monsters, have one room for the player to run around in, and have the ability to attack and kill (or be killed by) monsters.

4. Gif of Game Running
