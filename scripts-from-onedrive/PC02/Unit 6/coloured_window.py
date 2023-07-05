from tkinter import *


class ColourWindow:
    def __init__(self, colour: str):
        self.__colour = colour
        self.window = Tk()
        self.window.title("Colours")
        self.window.minsize(400, 300)
        self.window.config(bg=self.__colour)
        self.window.bind("<Return>", lambda e: self.set_colour())
        # Labels
        self.label = Label(text=colour, bg="black", fg="white")
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)
        # Entries
        self.entry = Entry()
        self.entry.insert(0, "#")
        self.entry.place(relx=0.5, rely=0.6, anchor=CENTER)
        # Button
        self.button = Button(text="Set colour", command=self.set_colour)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)
        
    def get_colour(self):
        return self.__colour
    
    def start(self):
        self.window.mainloop()
       
    def set_colour(self):
        if self.entry.get() != "":
            try:
                self.window.config(bg=self.entry.get())
                self.label.config(text=self.entry.get())
            except Exception as error:
                self.label.config(text=error)
                pass
        self.entry.delete(1, "end")
       
window = ColourWindow("#3d7e9a")
window.start()
