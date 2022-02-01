import turtle as t
import random

timmy = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_size in range(3,8):
    timmy.color(random.choice(colours))
    draw_shape(shape_size)
    

