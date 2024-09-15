import turtle
import pandas
from pathlib import Path

CURRENT_DIR = Path(__file__).parent

IMAGE_PATH = str(CURRENT_DIR / "blank_states_img.gif")

DATA_PATH = str(CURRENT_DIR / "50_states.csv")

OUTPUT_PATH = str(CURRENT_DIR / "states_to_learn.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

data = pandas.read_csv(DATA_PATH)

all_states = data.state.to_list()

guessed_states = []


while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?:"
    )

    answer_state = str(answer_state).title()

    if answer_state == "Exit":
        missing_states = []

        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(OUTPUT_PATH)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        coordinates = (state_data.x.item(), state_data.y.item())
        t.goto(coordinates)
        t.write(answer_state)
