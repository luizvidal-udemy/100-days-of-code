from pathlib import Path
from tkinter import *

ASSETS_DIR = Path(__file__).parent.parent.joinpath("assets")

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=ASSETS_DIR / "images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file=ASSETS_DIR / "images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=ASSETS_DIR / "images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)


window.mainloop()
