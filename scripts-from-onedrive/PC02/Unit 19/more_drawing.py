from tkinter import *


class PieChartWindow:
    def __init__(self):
        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=500, height=500)
        self.canvas.pack()
        self.canvas.create_text(250, 50, text="Favourite animals", font=(input("Enter font: "), 20))
        self.arc1 = input("Enter angle: ")
        self.arc2 = input("Enter angle: ")
        self.arc3 = input("Enter angle: ")
        self.canvas.create_oval(200, 200, 300, 300, fill="#000000")
        self.canvas.create_arc(200, 200, 300, 300, fill="#ff0000", start=0, extent=int(self.arc1))
        self.canvas.create_arc(200, 200, 300, 300, fill="#00ff00", start=int(self.arc1), extent=int(self.arc2))
        self.canvas.create_arc(200, 200, 300, 300, fill="#0000ff", start=int(self.arc2)+int(self.arc1), extent=int(self.arc3))

    def start(self):
        self.tk.mainloop()


wind = PieChartWindow()
wind.start()