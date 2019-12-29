# ai-tic-tac-toe

~~Each board position and picked square from the game is saved. When the game is over, these and the result of the game are used to update a saved dictionary of `weights` (a 0–100 value) representing each possible square to pick for each possible board position. Also updated in this dictionary is the number of times each of these possiblities was chosen. The current weight value and this number of observations is used to calculate the new weight when the next game completes.~~

On execution, the AI plays itself a set number of times, updating the `data` for both players after each game.

While looping through games, the final board position for each is displayed. Also displayed is the percentage of draws from the most recent 100 games. It is assumed that, as the AI learns, the percentage of draws should approach 100%.

There are 2,096 possible positions to evaluate.

## todo

- complete learning algorithm
- update/complete documentation
- save/load weights to/from file
- support human player
