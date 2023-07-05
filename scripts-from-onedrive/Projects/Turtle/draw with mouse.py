from turtle import *


def drag(x, y):
    turt.ondrag(None)
    turt.setheading(turt.towards(x, y))
    turt.goto(x, y)
    turt.ondrag(drag)


def click_right(x, y):
    turt.clear()


def go(event):
    turt.penup()
    turt.setheading(turt.towards(event.x, event.y))
    turt.goto(event.x, event.y)
    turt.pendown()


screen = Screen()
turt = Turtle()
turt.speed(-1)
listen()
#turt.ondrag(drag)
onscreenclick(click_right, 3)
canvas = getcanvas()
canvas.bind("<B1-Motion>", go)
screen.mainloop()
