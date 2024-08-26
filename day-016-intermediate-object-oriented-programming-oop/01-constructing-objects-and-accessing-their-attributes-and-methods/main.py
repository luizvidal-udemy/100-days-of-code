# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen

my_screen = Screen()
my_screen.bgcolor("black")

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)


my_screen.exitonclick()

