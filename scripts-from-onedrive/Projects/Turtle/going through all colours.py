from turtle import *
from random import random


def stop(x, y):
    global go
    #go = False
    print(r, g, b)


size, angle = 200, random()*90  # Also: 90.991 or 98 are good values
wn = Screen()
wn.screensize()

tim = Turtle()
tim.hideturtle()
tim.speed(0)
tim.color('white')
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

while go and over < 50:
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
    tim.color(r, g, b)
    tim.forward(x)
    tim.right(angle)
    x += 1
mainloop()