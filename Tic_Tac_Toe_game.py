import tkinter as tk
from tkinter import messagebox

def check_winner():
    """Check if there is a winner."""
    # Check rows and columns
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]  # Row match
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]  # Column match

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    return None

def is_full():
    """Check if the board is full."""
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

def handle_click(row, col):
    """Handle button clicks."""
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        winner = check_winner()

        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            label_status.config(text=f"Player {current_player}'s turn")

def reset_board():
    """Reset the board for a new game."""
    global current_player
    for row in buttons:
        for button in row:
            button["text"] = ""
    current_player = "X"
    label_status.config(text="Player X's turn")

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the board
buttons = [[None for _ in range(3)] for _ in range(3)]
current_player = "X"

# Add buttons to the grid
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                           command=lambda r=i, c=j: handle_click(r, c))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Add a status label
label_status = tk.Label(root, text="Player X's turn", font=("Arial", 16))
label_status.grid(row=3, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()
