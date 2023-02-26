import random
from tkinter import *
from tkinter import ttk
from Mongo import Mongo
from button_sandbox import button_sandbox
from Entry_Box import entry_sandbox

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

again = True

def deal():
    card = random.choice(card_values)

    return card

def score(cards):
    numeric_hand = []
    for index in range(len(cards)):
        if(cards[index] == "Jack" or cards[index] == "Queen" or cards[index] == "King"):
            numeric_hand.append(10)
        elif(cards[index] == "Ace"):
            numeric_hand.append(11)
        else:
            numeric_hand.append(cards[index])

    while((11 in numeric_hand) and sum(numeric_hand) > 21):
        ace_index = numeric_hand.index(11)
        numeric_hand[ace_index] = 1
        print(numeric_hand)
    return sum(numeric_hand)


def game(d=0):
    deposit = d
    dealer_hand = []
    user_hand = []
    for c in range(2):
        user_card = deal()
        dealer_card = deal()
        dealer_hand.append(dealer_card)
        user_hand.append(user_card)

    print(f"Your Cards: {user_hand} \t Your Score: {score(user_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")


    root = Tk()
    es = entry_sandbox(root, user_hand, score(user_hand), dealer_hand[0])
    es.win.mainloop()

    bet = es.get_val()
    print("BET", bet)

    gu = button_sandbox(user_hand, score(user_hand), dealer_hand[0])

    #more_cards = input("Do you want to hit or stand? ")
    #test = GUI()
    more_cards = gu.getValue()
    print(more_cards)
    while(more_cards == 1 and score(user_hand) <= 21):
        c = deal()
        user_hand.append(c)
        print(f"Your Cards: {user_hand} \t Your Score: {score(user_hand)}")
        if(score(user_hand) > 21):
            break
        else:
            #more_cards = input("Do you want to hit or stand? ")
            gu = button_sandbox(user_hand, score(user_hand), dealer_hand[0])

            more_cards = gu.value
    while(score(dealer_hand)< 17):
        dealer_hand.append((deal()))

    user_score = score(user_hand)
    dealer_score = score(dealer_hand)

    print(f"Dealer Score: {dealer_score}")
    #Print out results
    if(user_score > 21):
        print("You Lost! You went over ")
        deposit = deposit - int(bet)
    elif(dealer_score > 21):
        print("You win! The dealer went over!")
        deposit = deposit + int(bet)
    elif(user_score > dealer_score):
        print(f"You win! You scored {user_score} versus the dealer's {dealer_score}")
        deposit = deposit + int(bet)
    elif (dealer_score > user_score):
        print(f"You lose! You scored {user_score} versus the dealer's {dealer_score}")
        deposit = deposit - int(bet)

    print(f"Your funds currently stand at: {deposit}")
    return deposit

d = 100
while(again):
    d = game(d)
    response = input("Do you want to play again? ")
    response = response.lower()
    if(response == "no"):
        again = False
        storage = Mongo("Test Name", d)




