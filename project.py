# NQueen Problem Solver
# Navigate to line 68 to change the n value; n = ?
import tkinter as tk

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col, gui_board, labels, window):
    """Use backtracking to solve the N Queen problem."""
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            labels[i][col].config(text='Q', bg='red')  # Display queen
            window.update_idletasks()
            if solve_nq_util(board, col + 1, gui_board, labels, window):
                return True
            board[i][col] = 0
            labels[i][col].config(text='', bg='white')  # Remove queen
            window.update_idletasks()

    return False

def solve_n_queens(n):
    """Main function to solve the N Queen problem."""
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Setting up the GUI
    window = tk.Tk()
    window.title("N Queens Solver")
    gui_board = [[None for _ in range(n)] for _ in range(n)]
    labels = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            gui_board[i][j] = tk.Frame(window, width=50, height=50, borderwidth=1, relief='solid')
            gui_board[i][j].grid(row=i, column=j)
            gui_board[i][j].pack_propagate(False)
            labels[i][j] = tk.Label(gui_board[i][j], font=('Arial', 22), text='')
            labels[i][j].pack(expand=True, fill=tk.BOTH)

    if not solve_nq_util(board, 0, gui_board, labels, window):
        print("Solution does not exist")
        label = tk.Label(window, text="No solution exists!", font=('Arial', 14))
        label.pack()

    window.mainloop()

# Change the value of n to the number of queens
n = 4
solve_n_queens(n)
