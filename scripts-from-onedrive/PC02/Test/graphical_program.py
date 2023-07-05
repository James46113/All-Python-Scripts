# Create a ButtonClicker class that contains the following instance variables
# - A window with the title "Button Clicker"
# - A label that shows "Click on Buttons to Enter Password"
# - 4 Buttons under the label, each shown horizontally from left to right, with text "Button 1" to "Button 4"
# =   Add the same click listener to each button that retrieves the button's text and adds it to a list
# =   It then checks the list against a hard coded list of 4 values: "Button 2", "Button 4", "Button 1", "Button 3"
# =   If they match, change the label to "Correct Password Entered"
# =   If they don't when the list has 4 elements, remove all the elements from the list so the user can try again
# Define the following functions too
# - A start function that runs the main loop of the window


# Instantiate a ButtonClicker and start it
from tkinter import *


class ButtonClicker:
    def __init__(self):
        self.l = []
        self.g = ["Button 2", "Button 4", "Button 1", "Button 3"]
        self.tk = Tk()
        self.tk.geometry("200x200+400+500")
        self.lab = StringVar()
        self.lab.set("Click on Buttons to Enter Password")
        self.label = Label(textvariable=self.lab)
        self.label.place(relx=0.5, y=20, anchor=CENTER)
        Button(text="Button1", command=lambda: self.add("Button 1")).pack(side=LEFT)
        Button(text="Button2", command=lambda: self.add("Button 2")).pack(side=LEFT)
        Button(text="Button3", command=lambda: self.add("Button 3")).pack(side=LEFT)
        Button(text="Button4", command=lambda: self.add("Button 4")).pack(side=LEFT)

    def add(self, button):
        self.l.append(button)
        if self.l == self.g:
            self.lab.set("Correct Password Entered")
        if len(self.l) == 4:
            self.l = []

    def start(self):
        self.tk.mainloop()


b = ButtonClicker()
b.start()
