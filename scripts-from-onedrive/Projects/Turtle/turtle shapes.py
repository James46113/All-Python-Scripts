import turtle
import random

turt = turtle.Turtle()
colours = ["red", "blue", "green", "purple", "yellow", "orange", "black"]

turt.color("red", "blue")
turt.width(5)
#turt.shape("turtle")

turt.begin_fill()  # begin area to fill
turt.circle(50)  # draw circle
turt.end_fill()  # end area to fill

turt.penup()
turt.forward(150)
turt.pendown()
turt.color("yellow", "black")

turt.begin_fill()
for x in range(4):
    turt.forward(100)
    turt.right(90)
turt.end_fill()

turt.penup()
while True:
    turt.color(random.choice(colours), random.choice(colours))
    rand1 = random.randrange(-400, 400)
    rand2 = random.randrange(-400, 400)
    turt.penup()
    turt.setpos(rand1, rand2)
    turt.pendown()
    turt.begin_fill()
    turt.circle(random.randrange(0, 80))
    turt.end_fill()
