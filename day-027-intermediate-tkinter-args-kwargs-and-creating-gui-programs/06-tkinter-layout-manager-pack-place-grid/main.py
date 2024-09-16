from tkinter import *
# import tkinter


def button_click():
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)


# Button
new_button = Button(text="New Button", command=button_click)
# button.pack()
new_button.grid(column=2, row=0)


# Button
button = Button(text="Click Me", command=button_click)
# button.pack()
button.grid(column=1, row=1)


# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()
