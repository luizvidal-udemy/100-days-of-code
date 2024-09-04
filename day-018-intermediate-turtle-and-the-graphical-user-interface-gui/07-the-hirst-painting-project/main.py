from turtle import Turtle, Screen, colormode, bgcolor
from random import choice
from colorgram import extract


turtle = Turtle()
turtle.speed("fastest")
turtle.hideturtle()
colormode(255)
turtle.color(255, 255, 255)
bgcolor(200, 200, 200)


colors = extract("image.png", 10)

color_list = []


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))

turtle.penup()
turtle.goto(-225, -225)

for _ in range(10):
    for _ in range(10):
        turtle.dot(20, choice(color_list))
        turtle.forward(50)

    y = turtle.position()[1]

    turtle.goto(-225, y + 50)

screen = Screen()
screen.exitonclick()
