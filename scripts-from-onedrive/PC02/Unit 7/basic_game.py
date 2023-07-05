from tkinter import *
from random import choice


class Game:
    def __init__(self):
        self.letters = ["f", "y", "u", "q", "i", "a", "t", "z", "p", "b"]
        self.tk = Tk()
        self.tk.minsize(300, 200)
        self.rand_letter = StringVar()
        self.score = IntVar()
        self.score.set(0)
        self.rand_letter.set(choice(self.letters))
        self.tk.bind("<KeyPress>", self.check_press)
        Label(textvariable=self.rand_letter).pack()
        Label(textvariable=self.score).pack()

    def check_press(self, event):
        if event.keysym == self.rand_letter.get():
            self.rand_letter.set(choice(self.letters))
            self.score.set(self.score.get() + 1)
        else:
            self.rand_letter.set(choice(self.letters))
            self.score.set(self.score.get() - 1)


    def start(self):
        self.tk.mainloop()
        
        
g = Game()
g.start()