from turtle import Turtle, Screen
from random import random, choice

turtle = Turtle()
turtle.speed("fastest")


def change_color():
    R = random()
    B = random()
    G = random()

    turtle.color(R, G, B)


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        change_color()
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap_size)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
