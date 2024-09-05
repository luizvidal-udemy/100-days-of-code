from turtle import Screen, Turtle
from time import sleep
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()


screen.update()


game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)

    snake.move()


screen.exitonclick()
