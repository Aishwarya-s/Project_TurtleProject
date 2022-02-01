from turtle import *

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def move_clockwise():
    timmy.right(10)


def move_anticlockwise():
    timmy.left(10)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards, "s")
screen.onkey(move_anticlockwise,"a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()