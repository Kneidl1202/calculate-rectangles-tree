from tkinter import *
import tkinter as tk
import pickle
import calculate as cal


class Calculate:
    def __init__(self):
        self.main = Tk()

        self.diameter = tk.StringVar()
        self.diameter.set("")

        self.main.title("main")
        self.main.minsize(width=300, height=300)

        self.generate_tree = Button(self.main, text="Baeume hinzufuegen", command=self.generate_trees)
        self.calculate_tree = Button(self.main, text="Berechnungsmaße eingeben", command=lambda: self.calculate_trees())
        self.show_tree = Button(self.main, text="gespeicherte Baeume anzeigen", command=self.show_trees)

        self.generate_tree.grid(column=0, row=0)
        self.calculate_tree.grid(column=0, row=1)
        self.show_tree.grid(column=0, row=2)

        self.main.mainloop()

    def generate_trees(self):
        Add_trees(self.main)

    def show_trees(self):
        print_dict = ""

        self.main.withdraw()
        show_tree_gui = Tk()
        show_tree_gui.minsize(width=300, height=300)

        try:
            tree_dict = pickle.load(open('trees.pkl', 'rb'))
        except:
            tree_dict = {}

        for key, value in tree_dict.items():
            print_dict = print_dict + ("\nBaumnummer: {0} \nLaenge: {1}\nDurchmesser rot: {2}\n"
                                       .format(key, value[0], value[1]))

        show_tree_label = Label(show_tree_gui, text=print_dict)
        end_button = Button(show_tree_gui, text="Beenden", command=lambda: self.close(show_tree_gui, self.main))

        show_tree_label.grid(column=0, row=0)
        end_button.grid(column=1, row=0)

    def close(self, show_tree_gui, main):
        show_tree_gui.withdraw()
        main.deiconify()

    def calculate_trees(self):
        cal.Calculate(self.main)


class Add_trees:
    def __init__(self, main):
        main.withdraw()

        self.add_tree_gui = Tk()
        self.add_tree_gui.title("Baeume hunzufuegen")
        self.add_tree_gui.minsize(width=300, height=300)

        try:
            self.tree_dict = pickle.load(open("trees.pkl", "rb"))
        except:
            self.tree_dict = {}

        self.key_label = Label(self.add_tree_gui, text="Baumnummer")
        self.tree_lenght_label = Label(self.add_tree_gui, text="Laenge des Baumes")
        self.tree_diameter_red_label = Label(self.add_tree_gui, text="Durchmesser des roten Teiles")
        self.key_entry = Entry(self.add_tree_gui)
        self.lenght_entry = Entry(self.add_tree_gui)
        self.diameter_red_entry = Entry(self.add_tree_gui)
        self.add_button = Button(self.add_tree_gui, text="Hinzufuegen", command=self.get_user_input)
        self.end_button = Button(self.add_tree_gui, text="Beenden", command=lambda: self.close(main))

        self.key_label.grid(column=0, row=0)
        self.tree_lenght_label.grid(column=0, row=1)
        self.tree_diameter_red_label.grid(column=0, row=2)
        self.key_entry.grid(column=1, row=0)
        self.lenght_entry.grid(column=1, row=1)
        self.diameter_red_entry.grid(column=1, row=2)
        self.add_button.grid(column=0, row=3)
        self.end_button.grid(column=1, row=3)

    def add(self, key, item, dict):
        if key not in dict.keys():
            dict[key] = item
            with open('trees.pkl', 'wb') as handle:
                pickle.dump(dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return dict

    def get_user_input(self):
        key = self.key_entry.get()
        item = [self.lenght_entry.get(), self.diameter_red_entry.get()]
        self.tree_dict = self.add(key, item, self.tree_dict)

    def close(self, main):
        self.add_tree_gui.withdraw()
        main.deiconify()


if __name__ == '__main__':
    Calculate()
