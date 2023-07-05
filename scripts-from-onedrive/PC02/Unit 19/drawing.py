from tkinter import *
from threading import Thread
from tkinter.colorchooser import askcolor


class Draw:
    def __init__(self):
        self.tk = Tk()

        self.line = Button(text="Line", command=self.start_line_thread)
        self.line.place(x=30, y=20, anchor=CENTER)

        self.line_colour_button = Button(text="Line colour", command=self.change_line_colour)
        self.line_colour_button.place(x=100, y=20, anchor=CENTER)

        self.line_thickness = Entry(width=5)
        self.line_thickness.place(x=170, y=20, anchor=CENTER)
        self.line_thickness.insert(0, "2")
        self.line_thickness.bind("<KeyPress>", self.change_width)

        self.canvas = Canvas(width=500, height=500, bg="#ffffff")
        self.canvas.pack(pady=50)

        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.first = None
        self.second = None
        self.line_width = 2

        self.line_colour = "#000000"

        self.tk.bind("<Button-1>", self.click)

    def start(self):
        self.tk.mainloop()

    def change_width(self, event):
        self.line_width = int(self.line_thickness.get())
        print(self.line_width)

    def start_line(self):
        self.first = False
        self.second = False
        while not self.first or not self.second:
            pass
        print("made line")
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.line_colour, width=self.line_width)
        self.canvas.update()
        self.first = None
        self.second = None

    def change_line_colour(self):
        self.line_colour = askcolor()[1]

    def start_line_thread(self):
        t = Thread(target=self.start_line)
        t.start()
        print("started")

    def click(self, event):
        if not self.first:
            self.x1 = event.x
            self.y1 = event.y
            print("1s set")
            self.first = True

        else:
            self.x2 = event.x
            self.y2 = event.y
            print("2s set")
            self.second = True


draw = Draw()
draw.start()
