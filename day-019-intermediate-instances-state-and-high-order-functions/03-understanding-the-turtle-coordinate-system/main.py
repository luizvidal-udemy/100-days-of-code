from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=500, height=400)

# user_bet = screen.textinput(
#     title="Make your bet",
#     prompt="Which turtle will win the race? Enter a color: "
# )

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-240, y=0)

turtles = []


for index in range(len(colors)):
    turtle = Turtle(shape="turtle")
    print(index)
    print(colors[index])
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-240, y=index * 35 - 80)
    turtles.append(turtle)


screen.exitonclick()
