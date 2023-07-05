from turtle import *
from random import choice

tim = Turtle()
tim.speed(-1)
bgcolor('black')
x = 1
pos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

while x < 400:
    colour = "#"
    for x in range(6): colour += choice(pos)
    tim.pencolor(colour)
    fd(50 + x)
    rt(90.911)
    x = x+1
