# Grid_life
Grid life game
to run grid.runner([[],[].......])

which is a game applying some rules into a grid which containe only 1's and 0's
Rules


The whole world is a 2D board of cells
A generation moves from one to the next when the following rules
are applies simultaneously to all cells
1. If a live cell has less than 2 live neighbours, it dies due to
loneliness.
2. If a live cell has 2 or 3 live neighbours, it stays alive.
3. If a live cell has more than 3 live neighbours, it dies.
4. If a dead cell has exactly 3 live neighbours, it becomes alive.3
