import tkinter


def calculate():
    miles = miles_value_input.get()
    km =  float(miles) * 1.6
    result.config(text=km)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Hack Element
_ = tkinter.Label(text="")
_.grid(column=0, row=0)

# Miles Value Input
miles_value_input = tkinter.Entry()
miles_value_input.grid(column=1, row=0)

# Miles Text Label
miles_text_label = tkinter.Label(text="Miles")
miles_text_label.grid(column=2, row=0)

# Is equal to Label
equal_to = tkinter.Label(text="is equal to")
equal_to.grid(column=0, row=1)

# conversion result label
result = tkinter.Label(text="0")
result.grid(column=1, row=1)

# Km Text Label
km_text_label = tkinter.Label(text="Km")
km_text_label.grid(column=2, row=1)

# Calculate Buttton
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
