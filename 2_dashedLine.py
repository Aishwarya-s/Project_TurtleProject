from turtle import Turtle, Screen

turty = Turtle()
turty.shape("turtle")
turty.color("red")
screen = Screen()
for _ in range(0,20):
    turty.forward(10)
    turty.penup()
    turty.forward(10)
    turty.pendown()

screen.exitonclick()