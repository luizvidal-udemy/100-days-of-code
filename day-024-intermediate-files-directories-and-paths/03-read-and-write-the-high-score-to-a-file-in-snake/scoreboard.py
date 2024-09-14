import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
HIGH_SCORE_FILE = os.path.join(CURRENT_DIR, "high_score.txt")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def load_high_score(self):
        with open(HIGH_SCORE_FILE, "r") as file:
            self.high_score = int(file.read())

    def update_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))
