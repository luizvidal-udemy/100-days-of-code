import turtle
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
IMAGE_PATH = str(CURRENT_DIR / "blank_states_img.gif")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state's name?:")

screen.exitonclick()
