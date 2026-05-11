# CSCI 724 Final Project — A COMPARATIVE ANALYSIS OF PATHFINDING ALGORITHMS IN GAMES

## How to Run the Project
1. Open the project in your editor of choice
2. Start the `main.py` file by:
   1. Using the terminal command `python -m main`
   2. Using the start/execute button in your editor
3. After collecting all the necessary data in the `\data` directory, create the data charts by executing the
`analyze_results.py` file.
   1. This is done similarly to the `main.py` file by executing `python -m analyze_results` or by using the start button

## When Running the Game...
When you run the game, there will be a start screen that presents different "modes" that an be selected. There are the 
four pathfinding algorithms we implemented, a mode for human input, and another option that executes them all 
sequentially by starting with human input. Each mode is repeated a certain amount of times until the max amount of 
trials are executed. Once a mode has exhausted all its trials, the next mode will start.

## What is the Project About?
Our work was inspired by an article titled "A Systematic Review and Analysis of Intelligence-Based Pathfinding 
Algorithms in the Field of Video Games" by Lawande et al. While being inspired by the authors' experiments, 
our work was executed differently. Lawande et al. analyzed different metrics to evaluate how pathfinding algorithms 
performed in varying sizes of grid-based maps. There were no obstacles in these maps, and the goal was strictly to get 
from the starting point to the goal.

For our work, we decided to conduct a similar experiment, but in the context of the classic game Snake. By using this 
game, the goals and game environment slightly change. First, our game map was consistent the entire time while collecting 
metrics; the grid size never changed. Next, the authors concluded their research by stating how conducting 
experiments with dynamic objects (moving obstacles) would be a great next step. Given the nature of Snake, we 
were able to cover this as well, since the snake's body would count as a moving obstacle, changing positions for 
wherever the snake was previously.

## How were Experiments Conducted?
We used four pathfinding algorithms (A*, BFS, GBFS, and Dijkstra's) and human input as a control. We executed each of 
these different modes at least three times and stored our metrics in JSON files. We then took the average of each 
game's ending results to evaluate which algorithm performed best. 

To ensure the game environment was consistent, we made sure to use the same seeds for each mode's executions. 
For example, if we were to execute each mode three times, three seeds would be generated, and those same three seeds 
would be used for the rest of the modes.