import turtle as t
import random

turty = t.Turtle()
t.colormode(255)

direction = [0, 90, 180, 270]
turty.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r,g,b)
    return random_colors


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turty.circle(100)
        turty.color(random_color())
        turty.setheading(turty.heading() + size_of_gap)


draw_spirograph(5)

