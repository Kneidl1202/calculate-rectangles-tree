from tkinter import *
import tkinter as tk

window = Tk()

diameter = tk.StringVar()
diameter.set("")


def calculate():
    diameter.set(diameter_text.get("1.0"))


window.title = ""

diameter_text = Text(window, width=10, height=1)
diameter_label = Label(window, text="Durchmesser rot: ")
calculate_button = Button(window, text="Berechnen", command=calculate())
result_label = Label(window, textvariable=diameter)

diameter_label.grid(column=0, row=0)
diameter_text.grid(column=1, row=0)
calculate_button.grid(column=0, row=1)
result_label.grid(column=1, row=1)



window.mainloop()