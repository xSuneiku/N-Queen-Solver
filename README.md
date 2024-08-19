##What is the N-Queen Problem?
The problem involves placing N queens on an N×N chessboard such that no two queens can attack each other.
This following example is a solution for a 4 queen problem.

The output is in the form of a matrix where the "Q" are the spots where queen are and the "." are empty space.
. . Q .
Q . . .
. . . Q
. Q . .

##How Backtracking Algorithm Works in the Code:
1. is_safe Function:
-This function checks if placing a queen on a particular spot on the board is safe. It does this by ensuring that no other queens are in the same row, the same column, or on the diagonals that intersect with that spot.

2. solve_nq_util Function:-This function is the core of the backtracking process. It tries to place a queen in each row one by one.
-If placing a queen in a particular row and column is safe, it proceeds to place the next queen in the next column.
-If placing the next queen fails (no safe spot in the next column), it backtracks by removing the last placed queen and tries the next possible row.
-The function returns True when all queens are placed successfully, or False when a solution doesn't exist for the given configuration.

3. solve_n_queens Function:
-This function sets up the board and the GUI, and initiates the solving process starting from the first column.

##HOW TO WORK THE PROGRAM
** Navigate to line 68 to change the n value; n = ? **
