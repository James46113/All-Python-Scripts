from turtle import *


scale = 1

tim = Turtle("turtle")
tim.color("black", "#ba7a4b")
tim.pensize(int(5 * scale))
tim.speed(7)
tim.hideturtle()
tim.penup()
tim.goto(-200 * scale, -200 * scale)
tim.pendown()
# Main house shadow
tim.begin_fill()
for x in range(4):
    if x % 2 == 0:
        tim.forward(400 * scale)
    else:
        tim.forward(300 * scale)
    tim.left(90)
tim.end_fill()

# Roof shadow
tim.goto(-200 * scale, 100 * scale)
tim.begin_fill()
tim.setheading(180)
tim.forward(100 * scale)
tim.setheading(35)
tim.forward(366 * scale)
tim.right(70)
tim.forward(366 * scale)
tim.setheading(180)
tim.forward(500 * scale)
tim.end_fill()

tim.color("#f9a467")
tim.penup()
tim.goto(-180 * scale, -180 * scale)
tim.pendown()
# Main house colour
tim.setheading(0)
tim.begin_fill()
for x in range(4):
    if x == 0:
        tim.forward(360 * scale)
    elif x % 2 == 0:
        tim.left(90)
        tim.forward(360 * scale)
    else:
        tim.left(90)
        tim.forward(260 * scale)
tim.end_fill()

# Roof colour
tim.penup()
tim.goto(0, 120 * scale)
tim.pendown()
tim.begin_fill()
tim.setheading(180)
tim.forward(240 * scale)
tim.setheading(35)
tim.forward(296 * scale)
tim.right(70)
tim.forward(296 * scale)
tim.goto(0, 120 * scale)
tim.end_fill()

# Chimney
tim.color("black", "#f9a467")
tim.penup()
tim.goto(100 * scale, 242 * scale)
tim.pendown()
tim.begin_fill()
tim.setheading(90)
tim.forward(30 * scale)
tim.setheading(0)
tim.forward(30 * scale)
tim.setheading(270)
tim.forward(50 * scale)
tim.end_fill()

# Chimney shadow
tim.color("#ba7a4b")
tim.penup()
tim.goto(105 * scale, 260 * scale)
tim.pendown()
tim.begin_fill()
tim.setheading(0)
tim.forward(20 * scale)
tim.left(90)
tim.forward(7 * scale)
tim.left(90)
tim.forward(20 * scale)
tim.left(90)
tim.forward(7 * scale)
tim.end_fill()

# Chimney top
tim.color("black", "#aa5240")
tim.penup()
tim.goto(100 * scale, 272 * scale)
tim.pendown()
tim.begin_fill()
tim.setheading(180)
tim.forward(20 * scale)
tim.right(90)
tim.forward(25 * scale)
tim.right(90)
tim.forward(70 * scale)
tim.right(90)
tim.forward(25 * scale)
tim.right(90)
tim.forward(50 * scale)
tim.end_fill()

# Doorstep
tim.penup()
tim.goto(-100 * scale, -200 * scale)
tim.pendown()
tim.begin_fill()
tim.setheading(90)
tim.forward(35 * scale)
tim.right(90)
tim.forward(200 * scale)
tim.right(90)
tim.forward(35 * scale)
tim.right(90)
tim.forward(200 * scale)
tim.end_fill()
tim.right(90)
tim.forward(17 * scale)
tim.right(90)
tim.forward(200 * scale)

# Door
tim.penup()
tim.goto(-50 * scale, -165 * scale)
tim.pendown()
tim.begin_fill()
tim.setheading(90)
tim.forward(180 * scale)
tim.right(90)
tim.forward(100 * scale)
tim.right(90)
tim.forward(180 * scale)
tim.right(90)
tim.forward(100 * scale)
tim.end_fill()

# Door handle
tim.color("black")
tim.penup()
tim.goto(-35 * scale, -75 * scale)
tim.pendown()
tim.begin_fill()
tim.circle(3 * scale)
tim.end_fill()

# Left window
tim.color("black", "#bfcbf3")
tim.penup()
tim.goto(-175 * scale, 15 * scale)
tim.pendown()
tim.begin_fill()
tim.setheading(0)
for x in range(4):
    tim.forward(100 * scale)
    tim.right(90)
tim.end_fill()

# Left window partions
tim.penup()
tim.goto(-175 * scale, -20 * scale)
tim.pendown()
tim.setheading(0)
tim.forward(100 * scale)

tim.setheading(180)
tim.forward(50 * scale)
tim.left(90)
tim.forward(62 * scale)

# Right window
tim.penup()
tim.goto(175 * scale, 15 * scale)
tim.pendown()
tim.begin_fill()
tim.setheading(180)
for x in range(4):
    tim.forward(100 * scale)
    tim.left(90)
tim.end_fill()

# Right window partions
tim.penup()
tim.goto(175 * scale, -20 * scale)
tim.pendown()
tim.setheading(180)
tim.forward(100 * scale)

tim.setheading(0)
tim.forward(50 * scale)
tim.right(90)
tim.forward(62 * scale)

mainloop()
