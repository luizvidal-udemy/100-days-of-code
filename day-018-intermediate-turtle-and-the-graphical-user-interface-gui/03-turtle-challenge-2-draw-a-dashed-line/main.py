from turtle import Turtle, Screen

turtle = Turtle()

def draw_dash():
    for _ in range(20):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


draw_dash()

# for _ in range(4):
#     draw_dash()
#     turtle.right(90)

screen = Screen()
screen.exitonclick()
