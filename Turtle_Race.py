import random
from turtle import *


screen = Screen()
screen.setup(width=500, height=400)
color_palette = ["red", "blue", "green", "orange", "yellow", "purple"]
turtle_list = []
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False

for turtle_index in range(6):
    #create turtle , give color and bring to start point
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_palette[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    new_turtle.pendown()
    turtle_list.append(new_turtle)

#user bet color
user_betcolor = screen.textinput(title="Make your bet", prompt="Which turtle color do you think will win?")
print(user_betcolor)

if user_betcolor:
    is_race_on = True

while is_race_on :
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_betcolor:
                print("You won the bet!! ")
            else:
                print(f"Sorry ! You lost the bet . Winning color is {winning_turtle}")
            is_race_on = False
        distance = random.randint(0,10)
        turtle.penup()
        turtle.forward(distance)

screen.exitonclick()
