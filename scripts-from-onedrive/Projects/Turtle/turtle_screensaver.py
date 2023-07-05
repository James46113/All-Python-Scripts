from turtle import RawTurtle, bgcolor, listen, onscreenclick, colormode, TurtleScreen, clear, reset, bye
from tkinter import *
from datetime import datetime
import pyautogui
from random import random

pyautogui.FAILSAFE = False
tk = Tk()
tk.withdraw()
tk.config(cursor=None)
tk.attributes('-fullscreen', True)
tk.attributes('-topmost', True)
canvas = Canvas(master=tk, width=1700, height=1000, bd=0, bg="black")
turtle_screen = TurtleScreen(canvas)
turtle_screen.bgcolor("black")
canvas.pack()


def stop(x, y):
    global go
    go = False
    print(r, g, b)


size, angle = 200, 90.911  # Also: 90.991 or 98 are good values

while True:
    go_again = True
    not_pressed = True
    while go_again:
        go_again = False
        now = datetime.now()
        start_time = int(now.strftime("%H%M%S"))
        time_elapsed = 0
        mouse_x = tk.winfo_pointerx()
        mouse_y = tk.winfo_pointery()
        while time_elapsed < 60:
            print(time_elapsed)
            print(time_elapsed)
            now = datetime.now()
            time_elapsed = int(now.strftime("%H%M%S")) - start_time
            if mouse_x != tk.winfo_pointerx() and mouse_y != tk.winfo_pointery():
                go_again = True
                break

    pyautogui.move(1700, 500)
    tk.deiconify()
    tk.focus_set()

    angle = random()*90
    tim = RawTurtle(turtle_screen)
    tim.hideturtle()
    tim.speed(0)
    bgcolor('black')
    tim.penup()
    tim.pendown()
    listen()
    onscreenclick(stop, 1)

    go = True
    x = 1
    r, g, b = 50, 0, 0
    stage = 1
    over = 0
    mouse_x = tk.winfo_pointerx()
    mouse_y = tk.winfo_pointery()

    while mouse_x == tk.winfo_pointerx() and mouse_y == tk.winfo_pointery() and go:
        if stage == 1:
            r += 2
        elif stage == 2:
            g += 2
        elif stage == 3:
            r -= 2
        elif stage == 4:
            b += 2
        elif stage == 5:
            g -= 2
        elif stage == 6:
            r += 2
        elif stage == 7:
            b -= 2
        elif stage == 8:
            over += 1

        if r == 254 and stage == 1:
            stage += 1
        elif g == 254 and stage == 2:
            stage += 1
        elif r == 0 and stage == 3:
            stage += 1
        elif b == 254 and stage == 4:
            stage += 1
        elif g == 0 and stage == 5:
            stage += 1
        elif r == 254 and stage == 6:
            stage += 1
        elif b == 0 and stage == 7:
            stage += 1
        elif r == 0 and stage == 8:
            stage += 1

        colormode(255)
        tim.color(r/1000, g/1000, b/1000)
        tim.forward(x)
        tim.right(angle)
        x += 1
    clear()
    reset()
    tim.reset()
    tim.clear()
    tk.withdraw()