from tkinter import *
from random import choice


class SimonSays:
    def __init__(self):
        self.tk = Tk()
        self.tk.geometry("170x145")
        self.ss = ["Simon says click on ", "Click on "]
        self.pos = ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5", "Button 6", "Button 7", "Button 8", "Button 9", "Button 10"]
        self.info = StringVar()
        self.info.set(choice(self.ss)+choice(self.pos))
        self.l = Label(self.tk, textvariable=self.info)
        self.l.grid(row=0, column=0, columnspan=4)
        self.score = IntVar()
        self.score.set(0)
        self.s = Label(self.tk, textvariable=self.score)
        self.s.grid(row=1, column=1)

        self.b1 = Button(self.tk, text="Button 1", command=lambda: self.rand_button("Button 1"))
        self.b1.grid(row=2, column=0)
        self.b2 = Button(self.tk, text="Button 2", command=lambda: self.rand_button("Button 2"))
        self.b2.grid(row=2, column=1)
        self.b3 = Button(self.tk, text="Button 3", command=lambda: self.rand_button("Button 3"))
        self.b3.grid(row=2, column=2)
        self.b4 = Button(self.tk, text="Button 4", command=lambda: self.rand_button("Button 4"))
        self.b4.grid(row=3, column=0)
        self.b5 = Button(self.tk, text="Button 5", command=lambda: self.rand_button("Button 5"))
        self.b5.grid(row=3, column=1)
        self.b6 = Button(self.tk, text="Button 6", command=lambda: self.rand_button("Button 6"))
        self.b6.grid(row=3, column=2)
        self.b7 = Button(self.tk, text="Button 7", command=lambda: self.rand_button("Button 7"))
        self.b7.grid(row=4, column=0)
        self.b8 = Button(self.tk, text="Button 8", command=lambda: self.rand_button("Button 8"))
        self.b8.grid(row=4, column=1)
        self.b9 = Button(self.tk, text="Button 9", command=lambda: self.rand_button("Button 9"))
        self.b9.grid(row=4, column=2)
        self.b10 = Button(self.tk, text="Button 10", command=lambda: self.rand_button("Button 10"))
        self.b10.grid(row=5, column=1)

    def start(self):
        self.tk.mainloop()

    def rand_button(self, num):
        if self.info.get().startswith("Si"):
            if self.info.get()[-8:] == num:
                self.info.set(choice(self.ss) + choice(self.pos))
                self.score.set(self.score.get()+1)
            else:
                self.end()
        else:
            if self.info.get()[-8:] != num:
                self.info.set(choice(self.ss) + choice(self.pos))
                self.score.set(self.score.get()+1)
            else:
                self.end()

    def end(self):
        self.b1.grid_forget()
        self.b2.grid_forget()
        self.b3.grid_forget()
        self.b4.grid_forget()
        self.b5.grid_forget()
        self.b6.grid_forget()
        self.b7.grid_forget()
        self.b8.grid_forget()
        self.b9.grid_forget()
        self.b10.grid_forget()
        self.l.grid_forget()
        self.s.grid_forget()
        Label(textvariable=self.score, font=(None, 30)).pack()


s = SimonSays()
s.start()
