from tkinter import Tk
from random import choice
from time import sleep
tk = Tk()
#tk.attributes('-fullscreen', True)
pos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
while True:
    failed = True
    colour = "#"
    while failed:
        failed = False
        for x in range(6): colour += choice(pos)
        tk.config(bg=colour)
    sleep(0.001)
    tk.update()
