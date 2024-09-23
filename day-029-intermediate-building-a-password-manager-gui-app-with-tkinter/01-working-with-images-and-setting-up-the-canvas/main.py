from pathlib import Path
from tkinter import *


CURRENT_DIR = Path(__file__).parent
LOGO_DIR = CURRENT_DIR / "logo.png"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=LOGO_DIR)

canvas.create_image(100, 100, image=logo_img)

canvas.pack()

window.mainloop()
