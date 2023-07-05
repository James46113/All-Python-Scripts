from turtle import *
from random import randint


def stop(x, y):
    global go
    go = False


size, angle = 200, 90.911
tim = Turtle()
tim.hideturtle()
tim.speed(-1)
tim.color('white')
bgcolor('black')
tim.penup()
tim.goto(-120, 60)
tim.pendown()
listen()
onscreenclick(stop, 1)
go = True
x = 1
r, g, b = 0, 0, 0


while go:
    r += 1
    g += 1
    b += 1
    colormode(255)

    tim.color(r, g, b)

    tim.forward(size+x)
    tim.right(angle)
    x += 1
mainloop()