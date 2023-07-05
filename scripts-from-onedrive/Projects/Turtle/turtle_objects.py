import turtle

turt = turtle.Turtle()
turt.color('red')
turt.pensize(10)
turt.shape('turtle')

turt.speed(1)  # speed of turtle
turt.forward(100)  # moves turtle forward 100 pixels
turt.left(90)  # rotates turle 90 degres to left
turt.penup()  # doesn't draw line where turle goes
turt.forward(100)
turt.pendown()  # draws line where turtle goes
turt.right(90)
turt.forward(100)


input()
