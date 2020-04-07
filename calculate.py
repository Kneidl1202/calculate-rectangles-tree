from tkinter import *
import pickle


class Calculate:
    def __init__(self, main):
        main.withdraw()
        self.calculate_gui = Tk()
        self.calculate_gui.title("Maße eingeben")
        self.calculate_gui.minsize(width=300, height=300)

        try:
            with open('input.pkl', 'rb') as handle:
                self.dict_entry = pickle.load(handle)
        except:
            self.dict_entry = {}

        self.file = open('counter.txt', 'r')
        self.counter = self.file.read()
        self.file.close()

        self.key = ""
        self.value = ""

        self.amount_trees_label = Label(self.calculate_gui, text="Wie viele Balken: ")
        self.length_label = Label(self.calculate_gui, text="Laenge des Balkens: ")
        self.height_label = Label(self.calculate_gui, text="Breite des Balkens: ")
        self.with_label = Label(self.calculate_gui, text="Hoehe des Balkens")
        self.amount_entry = Entry(self.calculate_gui)
        self.length_entry = Entry(self.calculate_gui)
        self.height_entry = Entry(self.calculate_gui)
        self.with_entry = Entry(self.calculate_gui)
        self.add_button = Button(self.calculate_gui, text="Maße hinzufuegen", command=lambda: self.get_user_input())
        self.calculate_button = Button(self.calculate_gui, text="Beste Moeglichkeit berechnen", command=lambda: self.end(main))

        self.amount_trees_label.grid(column=0, row=0)
        self.amount_entry.grid(column=1, row=0)
        self.length_label.grid(column=0, row=1)
        self.length_entry.grid(column=1, row=1)
        self.height_label.grid(column=0, row=3)
        self.height_entry.grid(column=1, row=3)
        self.with_label.grid(column=0, row=4)
        self.with_entry.grid(column=1, row=4)
        self.add_button.grid(column=0, row=5)
        self.calculate_button.grid(column=1, row=5)

    def end(self, main):
        result = ""
        self.calculate_gui.withdraw()
        main.deiconify()
        result_label = Label(main, text=result)
        result_label.grid(column=0, row=3)

    def add(self):
        self.dict_entry[self.key] = self.value
        with open('input.pkl', 'wb') as handle:
            pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def get_user_input(self):
        self.key = self.counter
        self.value = [self.amount_entry.get(), self.height_entry.get(), self.length_entry.get(), self.with_entry.get()]
        self.add()
        self.counter = str(int(self.counter) + 1)
        self.file = open('counter.txt', 'w')
        self.file.write(self.counter)
        self.file.close()
