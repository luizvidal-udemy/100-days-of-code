from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def left():
    # tim.left(10)
    tim.setheading(tim.heading() + 10)


def right():
    # tim.right(10)
    tim.setheading(tim.heading() - 10)


def reset():
    tim.reset()


screen.listen()

screen.onkey(fun=forwards, key="w")
screen.onkey(fun=backwards, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=reset, key="c")

screen.exitonclick()
