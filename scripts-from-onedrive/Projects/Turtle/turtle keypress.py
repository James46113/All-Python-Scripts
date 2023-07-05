from turtle import *
import random


def up():
    turt.setheading(90)
    turt.forward(100)


def down():
    turt.setheading(270)
    turt.forward(100)


def left():
    turt.setheading(180)
    turt.forward(100)


def right():
    turt.setheading(0)
    turt.forward(100)


def click_left(x, y):
    turt.color(random.choice(colours))


def click_right(x, y):
    turt.stamp()


def fill():
    global fill_on
    if fill_on:
        turt.end_fill()
        fill_on = False
    else:
        turt.begin_fill()
        fill_on = True


def pen():
    global pen_on
    if pen_on:
        turt.penup()
        pen_on = False
    else:
        turt.pendown()
        pen_on = True


def white():
    turt.color("white")


pen_on = True
fill_on = False
turt = Turtle()
turt.speed(0)
turt.width(5)
turt.shape("turtle")

colours = ["red", "blue", "green", "purple", "yellow", "orange", "black"]

listen()
onkey(up, "Up")
onkey(down, "Down")
onkey(left, "Left")
onkey(right, "Right")
onkey(fill, "f")
onkey(pen, "p")
onkey(white, "e")
onscreenclick(click_left, 1)
onscreenclick(click_right, 3)

mainloop()