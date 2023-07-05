from pynput.keyboard import Controller as kc
from pynput.mouse import Controller as mc
from pynput.mouse import Button
from pynput import mouse
from tkinter import Tk
from time import sleep


root = Tk()
k = kc()
m = mc()
x = 0
y = 0
d = 200
midx = 957
midy = 566

while True:
        x = root.winfo_pointerx()
        y = root.winfo_pointery()
        if x < 50 or y < 50:
            continue
        #print(x, y)
        if y < midy - d:
            k.press("w")
        else:
            k.release("w")
        if y > midy +d:
            k.press("s")
        else:
            k.release("s")
        if x < midx - d:
            k.press("a")
        else:
            k.release("a")
        if x > midx + d:
            k.press("d")
        else:
            k.release("d")
        sleep(0.1)
