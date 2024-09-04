from turtle import Turtle, Screen
from random import choice
from colorgram import extract


turtle = Turtle()
turtle.speed("fastest")

hex_colors = []


def clamp(x):
    return max(0, min(x, 255))


def rgb_to_hex(rgb):
    return "#{0:02x}{1:02x}{2:02x}".format(
        clamp(rgb[0]), clamp(rgb[1]), clamp(rgb[2]))


colors = extract("image.png", 10)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    hex_color = rgb_to_hex((r, g, b))
    hex_colors.append(hex_color)


def change_color():
    color = choice(hex_colors)
    turtle.color(color)


def draw_dots(quantity):
    for _ in range(quantity):
        change_color()
        turtle.pendown()
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)


def draw_hirst(size):

    for _ in range(size):
        draw_dots(size)
        y = turtle.position()[1]

        turtle.goto(0, y + 50)


draw_hirst(10)


screen = Screen()
screen.exitonclick()
