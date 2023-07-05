from tkinter import *

root = Tk()

def hello():
    print("hello!")

menu = Menu(root, tearoff=0)
menu.add_command(label="Undo", command=hello)
menu.add_command(label="Redo", command=hello)


def popup(event):
    menu.post(event.x_root, event.y_root)

# attach popup to canvas
root.bind("<Button-3>", popup)
root.mainloop()
