from tkinter import *
from tkinter.colorchooser import askcolor


class StickMan:
    def __init__(self):
        self.tk = Tk()
        self.canvas = Canvas(width=500, height=500, bg=askcolor()[1])
        self.canvas.pack()
        self.man_colour = askcolor()[1]
        self.canvas.create_oval(200, 100, 300, 200, width=5, outline=self.man_colour)
        self.canvas.create_line(250, 200, 250, 350, width=5, fill=self.man_colour)
        self.canvas.create_line(250, 350, 300, 450, width=5, fill=self.man_colour)
        self.canvas.create_line(250, 350, 200, 450, width=5, fill=self.man_colour)
        self.canvas.create_line(250, 225, 300, 325, width=5, fill=self.man_colour)
        self.canvas.create_line(250, 225, 200, 325, width=5, fill=self.man_colour)

    def start(self):
        self.tk.mainloop()


sm = StickMan()
sm.start()