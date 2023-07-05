from tkinter import *
from tkinter.colorchooser import askcolor


class DrawingWindow:
    def __init__(self):
        self.__tk = Tk()
        self.__canvas = Canvas(width=500, height=500, bg="#ffffff")
        self.__canvas.pack()
        self.__canvas.create_line(100, 100, 400, 100)
        self.__canvas.create_line(100, 100, 100, 400)
        self.__canvas.create_line(100, 400, 400, 400)
        self.__canvas.create_line(400, 400, 400, 100)

        self.__col1 = askcolor()[1]
        self.__col2 = askcolor()[1]
        self.__col3 = askcolor()[1]
        self.__col4 = askcolor()[1]

        self.__canvas.create_rectangle(50, 50, 150, 150, fill=self.__col1)
        self.__canvas.create_rectangle(350, 350, 450, 450, fill=self.__col2)
        self.__canvas.create_rectangle(50, 350, 150, 450, fill=self.__col2)
        self.__canvas.create_rectangle(350, 50, 450, 150, fill=self.__col2)

        #self.__col1 = int("ffffff", 16) - int(self.__col1[1:], 16)
        self.__canvas.create_rectangle(50, 50, 150, 150, fill=self.__col1)
        self.__canvas.create_rectangle(350, 350, 450, 450, fill=self.__col2)
        self.__canvas.create_rectangle(50, 350, 150, 450, fill=self.__col2)
        self.__canvas.create_rectangle(350, 50, 450, 150, fill=self.__col2)

    def start(self):
        self.__tk.mainloop()


window = DrawingWindow()
window.start()