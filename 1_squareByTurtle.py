from turtle import *

turty = Turtle()
turty.shape("turtle")
turty.color("red")
screen = Screen()
for _ in range(0,4):
    turty.forward(200)
    turty.right(90)

screen.exitonclick()
