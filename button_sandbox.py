from tkinter import *
from tkinter import ttk

class button_sandbox:
    def __init__(self, user_hand, score, dealer_card):
        #Initial setup - construct Tkinter Window
        self.win = Tk()
        self.win.geometry("700x180")
        self.win.title("Hangman")
        self.value = -1

        label = Label(self.win, text = "BLACKJACK").pack()
        label = Label(self.win, text = f"Your Cards: {user_hand} \t Your Score: {score}").pack()
        label = Label(self.win, text = f"Dealer's first card: {dealer_card}").pack()
        # Add Buttons on Window
        b1 = ttk.Button(self.win, text="HIT", command=self.hit)
        b1.pack()

        b2 = ttk.Button(self.win, text="Stand", command=self.stand)
        b2.pack()

        self.win.mainloop()


    #Methods for buttons
    def hit(self):
        print("Hit")
        self.value = 1
        self.win.destroy()

    def stand(self):
        print("Stand")
        self.value = 0
        self.win.destroy()

    def getValue(self):
        return self.value

