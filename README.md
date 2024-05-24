One day, after discovering the board game [Ricochet Robots](https://en.wikipedia.org/wiki/Ricochet_Robots), I realized the dynamics of the game would make for a fun coding challenge

## Running the code
Install pygame (version 2.5.2 with python 3.10 is a possibility, but most of the versions should be supported)\
run `python main.py`

## To play the game
You have 4 robots on the board, represented by the 4 colored squares.\
One square on the board has a colored circle on it. That is your **target** square. It is randomly generated.\
You can see there are walls on the board, shown by brown lines.\
\
Your **goal** is to move the robot whose color matches the circle **directly** on the target square.\
\
**To move a robot**, click on it and use the arrow keys (up, down, left right) to choose the directions you want it to move.\
When a robot moves, it will travel in the direction specified by the arrow **until it reaches an obstacle**. Obstacles can be a wall **or another robot** (that's where it gets interesting).\
Imagine that the robot is on slippery ice, and the only way it can stop is to hit an obstacle in its way (just like in those Pokemon games from my childhood).\
\
Once a target is reached, a new one will appear.\
\
Since a move is not reversible ((up, down) will not necessarily lead back to the starting point), there is an opportunity to **undo by pressing 'u'**.\
\
The initial game's aim is to try to find a solution which takes as few moves as possible. However this is more flexible and you can just play around with all the robots.
## Next steps for the project
One of the initial goals was to train a reinforcement learning algorithm to solve the puzzles as efficiently as possible. Back then I didn't understand RL much.
Now that I know about reinforcement learning methods, I plan making one to solve the game.
However maybe an algorithm like A* would be able to solve this. The problem is the state and action space might be a bit big.

I also want implement a counter visible on the screen that tells you how many moves you've taken for a specific task, and a score that tells you how many you've solved

I would also be interested in figuring out how to host this on a simple website instead, so that people can access it without having to run the code (similar online implementations of this game already exist)
