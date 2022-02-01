import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

direction = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r,g,b)
    return random_colors


for _ in range(100):
    timmy.forward(30)
    timmy.color(random_color())
    timmy.setheading(random.choice(direction))
