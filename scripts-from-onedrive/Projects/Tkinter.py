from tkinter import *
from pyautogui import click

window = Tk()
window.geometry("200x100+200+200")

window2 = Tk()
window2.geometry("200x100+1000+200")


def b_click():
    click(1104, 249, duration=0.5)


def b_click2():
    click(304, 249, duration=0.5)


Button(window, text='Click me', command=b_click).pack()
Button(window2, text='Click me', command=b_click2).pack()
window.mainloop()
