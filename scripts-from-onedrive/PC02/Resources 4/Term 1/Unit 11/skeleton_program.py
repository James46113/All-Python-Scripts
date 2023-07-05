import tkinter


# Global variables (so all functions can access them)
# Also set up all the UI elements here
current_player = 0
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
window = tkinter.Tk()
window.title("Noughts and Crosses")

# Loop through the 3x3 grid row by row and create Frames for each row
for current_row in range(3):
    row = tkinter.Frame(window)
    row.pack()

    # Within each row, loop through the 3 spaces and create buttons for them
    for current_col in range(3):
        button = tkinter.Button(row)

        # Configure and pack the buttons so they run the 'select_button' function
        # (will need to include self. before select_button when changing to OOP)
        button.config(text=" ", command=lambda clicked_button=button, clicked_row=current_row, clicked_col=current_col: select_button(clicked_button, clicked_row, clicked_col))
        button.pack(side=tkinter.LEFT)


# Function for when a button is clicked in the window
# It sets that button to the correct symbol and moves the player on to the next one
# current_player is currently global, would need to change if going to an OOP design
def select_button(button_clicked, row, column):
    global current_player
    symbol = "X" if current_player == 0 else "O"
    grid[row][column] = symbol
    button_clicked.config(text="{}".format(symbol))
    current_player = (current_player + 1) % 2


def start():
    window.mainloop()


start()
