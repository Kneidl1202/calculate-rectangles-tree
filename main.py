from tkinter import *
import tkinter as tk


class Calculate:
    def __init__(self):
        self.window = Tk()

        self.diameter = tk.StringVar()
        self.diameter.set("")

        self.window.title = "Baumberechnung"
        self.window.minsize(width=300, height=300)

        self.diameter_entry = Entry(self.window)
        self.diameter_label = Label(self.window, text="Durchmesser rot: ")
        self.calculate_button = Button(self.window, text="Berechnen", command=self.calculate)
        self.result_label = Label(self.window, textvariable=self.diameter)

        self.diameter_label.grid(column=0, row=0)
        self.diameter_entry.grid(column=1, row=0)
        self.calculate_button.grid(column=0, row=1)
        self.result_label.grid(column=1, row=1)

        self.window.mainloop()

    def calculate(self):
        self.diameter.set(self.diameter_entry.get())


Calculate()
