from tkinter import *
from tkinter import ttk

# create a tkinter window
from tkinter.ttk import Label
class User_Name:
    def __init__(self, root):
        self.win = root
        self.win.title("BLACKJACK")

        # create an entry widget
        self.win.geometry("700x180")
        label = Label(self.win, text="BLACKJACK").pack()

        self.label = Label(self.win, text = "Let's have your name: ", font=('Times', 18)).pack()
        self.entry = Entry(self.win)
        self.entry.pack()
        self.val = -1
        # create a button to save the entry value
        save_button = Button(self.win, text="Enter", command=self.save_entry)
        save_button.pack()



    def save_entry(self):
        # get the value of the entry widget
        self.val = self.entry.get()
        print(f"Entry value: {self.val}")
        self.win.destroy()

    def get_val(self):
        print("here")
        print(self.val)
        return self.val


