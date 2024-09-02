from turtle import Turtle, Screen
from random import random, choice

turtle = Turtle()
turtle.width(15)
turtle.speed("fastest")


def change_color():
    R = random()
    B = random()
    G = random()

    turtle.color(R, G, B)


directions = [0, 90, 180, 270]

for _ in range(200):
    turtle.forward(30)
    turtle.setheading(choice(directions))
    change_color()


screen = Screen()
screen.exitonclick()
