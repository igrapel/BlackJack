from tkinter import *
from tkinter import ttk

# create a tkinter window
from tkinter.ttk import Label
class Entry_Box:
    def __init__(self, root, user_hand, score, dealer_card):
        self.win = root
        self.win.title("BLACKJACK")

        # create an entry widget
        self.win.geometry("700x180")
        label = Label(self.win, text="BLACKJACK").pack()
        label = Label(self.win, text=f"Your Cards: {user_hand} \t Your Score: {score}", font=('Times', 18)).pack()
        label = Label(self.win, text=f"Dealer's first card: {dealer_card}", font=('Times', 18)).pack()
        self.label = Label(self.win, text = "How much do you want to bet? ", font=('Times', 18)).pack()
        self.entry = Entry(self.win)
        self.entry.pack()
        self.val = -1
        # create a button to save the entry value
        save_button = Button(self.win, text="Enter", command=self.save_entry)
        save_button.pack()



    def save_entry(self):
        # get the value of the entry widget
        self.val = self.entry.get()
        self.val = int(self.val)
        print(f"Entry value: {self.val}")
        self.win.destroy()

    def get_val(self):
        print("here")
        print(self.val)
        return self.val


