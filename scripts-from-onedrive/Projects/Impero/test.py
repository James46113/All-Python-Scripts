from tkinter import Tk


def ev(event):
    print(event.keysym)


root = Tk()
root.bind("<Key>", ev)
root.mainloop()