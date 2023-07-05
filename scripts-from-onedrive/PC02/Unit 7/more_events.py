from tkinter import *


class ColourIncrementWindow:
    def __init__(self):
        self.tk = Tk()
        self.tk.config(bg="#b1b1b1")
        self.tk.minsize(300, 200)
        self.tk.bind("<Button-1>", self.decrease)
        self.tk.bind("<Button-3>", self.decrease)
        self.tk.bind("<Motion>", self.position)
        self.tk.bind("<KeyPress>", self.keys)

        self.r_colour = 100
        self.g_colour = 100
        self.b_colour = 100
        
        self.pos = StringVar()
        self.pos_label = Label(textvariable=self.pos).pack()

    def start(self):
        self.tk.mainloop()
    
    def change(self, col):
        if col == "r":
            self.r_colour += 10
        elif col == "g":
            self.g_colour += 10
        else:
            self.g_colour += 10
        self.tk.config(bg="#{:02x}{:02x}{:02x}".format(self.r_colour, self.g_colour, self.b_colour))
    
    def decrease(self, event):
        self.r_colour -= 10
        self.g_colour -= 10
        self.g_colour -= 10
        self.tk.config(bg="#{:02x}{:02x}{:02x}".format(self.r_colour, self.g_colour, self.b_colour))
    
    def increase(self, event):
        self.r_colour += 10
        self.g_colour += 10
        self.g_colour += 10
        self.tk.config(bg="#{:02x}{:02x}{:02x}".format(self.r_colour, self.g_colour, self.b_colour))

    def position(self, event):
        self.pos.set("{},{}".format(event.x, event.y))

    def keys(self, event):
        if event.keysym == "r":
            self.tk.config(bg="red")
        elif event.keysym == "g":
            self.tk.config(bg="#00ff00")
        elif event.keysym == "b":
            self.tk.config(bg="blue")

    
    
window = ColourIncrementWindow()
window.start()