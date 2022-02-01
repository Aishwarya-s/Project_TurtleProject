import turtle as t
import random
timmy = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction=[0,90,180,270]

timmy.pensize(10)
timmy.speed("fastest")

for _ in range(100):
    timmy.forward(30)
    timmy.pencolor(random.choice(colours))
    timmy.setheading(random.choice(direction))
