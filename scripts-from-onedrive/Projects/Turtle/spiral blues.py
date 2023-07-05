from turtle import *
from random import randint


def stop(x, y):
    global go
    go = False


size, angle = 200, 90.911
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
r, g, b = 0, 0, 0


while go:
    if b != 255 and x % 2 == 0:
        b += 1
    colormode(255)
    try:
        tim.color(r, g, b)
    except TurtleGraphicsError:
        pass
    tim.forward(x)
    tim.right(angle)
    x += 1
mainloop()