from turtle import Turtle, Screen
from random import random

turtle = Turtle()


def change_color():
    R = random()
    B = random()
    G = random()

    turtle.color(R, G, B)


def draw_polygon(size):
    for _ in range(size):
        turtle.forward(100)
        turtle.right(360 / size)


for size in range(3, 11):
    draw_polygon(size)
    change_color()


screen = Screen()
screen.exitonclick()
