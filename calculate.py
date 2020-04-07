from tkinter import *


class Calculate():
    def __init__(self, main):
        result = ""

        self.result_label = Label(main, text=result)
        self.result_label.grid(column=0, row=3)
