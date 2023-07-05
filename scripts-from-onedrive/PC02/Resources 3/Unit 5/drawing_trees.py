"""THIS DRAWING CODE ONLY WORKS PROPERLY FOR BINARY TREES (TREES WITH 2 CHILDREN AT MOST)"""
""" ADD THESE INSTANCE FUNCTION TO THE TREE CLASS """
def get_children(self):
    return self.__children

def get_value(self):
    return self.__value


# Gets the depth of the tree
def return_tree_depth(current: Tree, depth: int) -> int:
    if len(current.get_children()) == 0:
        return depth
    greatest_depth = depth
    for child in current.get_children():
        new_depth = return_tree_depth(child, depth + 1)
        if new_depth > greatest_depth:
            greatest_depth = new_depth
    return greatest_depth


# Setup the window to show the Tree
canvas_size = 800  # Keep the canvas as a square
import tkinter
window = tkinter.Tk()
window.title("Drawing Trees")
canvas = tkinter.Canvas(window, width=canvas_size, height=canvas_size, bg="#FFFFFF")

# Split the canvas into a NxN grid ready for the nodes
max_levels = return_tree_depth(root, 1)
cols = max_levels ** 2
rows = max_levels ** 2
square_size = canvas_size / cols
coord_grid = []
for current_row in range(rows):
    coord_row = []
    for current_col in range(cols):
        start_x = current_col * square_size
        start_y = current_row * square_size
        end_x = start_x + square_size
        end_y = start_y + square_size
        coord_row.append((start_x, start_y, end_x, end_y))
    coord_grid.append(coord_row)

# Iteratively go through the Tree and connect nodes with coordinates from the grid
visited = []
pairs = []
found = [(root, 0, 0, len(coord_grid) - 1, None, None)]
while len(found) > 0:
    current, level, lower_width, upper_width, parent_coord_x, parent_coord_y = found.pop(0)
    visited.append(current)
    # Get the correct coordinate grid (the middle of the allowed left/right on the current level)
    grid_row = int((level / max_levels) * rows)
    grid_col = int((lower_width + upper_width) // 2)
    packet = (current.get_value(), coord_grid[grid_row][grid_col], (parent_coord_x, parent_coord_y))
    pairs.append(packet)
    # Check if we have any children and update their bounds
    max_width = upper_width
    upper_width = grid_col - 1
    parent_coord_x = coord_grid[grid_row][grid_col][0]
    parent_coord_y = coord_grid[grid_row][grid_col][1]
    for child in current.get_children():
        found.append((child, level + 1, lower_width, upper_width, parent_coord_x, parent_coord_y))
        lower_width = grid_col + 1
        upper_width = max_width
print(pairs)

# Draw all the lines and nodes in the pairs list
for current_pair in pairs:
    value, coordinates, parent_coordinates = current_pair
    if parent_coordinates[0] is not None:
        canvas.create_line(coordinates[0] + (square_size / 2), coordinates[1] + (square_size / 2),
                           parent_coordinates[0] + (square_size / 2), parent_coordinates[1] + (square_size / 2))
for current_pair in pairs:
    value, coordinates, parent_coordinates = current_pair
    canvas.create_oval(coordinates, fill="#FF5555")
    canvas.create_text(coordinates[0] + (square_size / 2), coordinates[1] + (square_size / 2), text=str(value), font=("Consolas", 16))

# Pack the canvas and show the window
canvas.pack()
window.mainloop()
