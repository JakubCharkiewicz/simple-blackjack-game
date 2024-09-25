import time
import os, sys
from textwrap import indent

from art import logo, goodbye
import random
print(logo)
user_cards = []     ## User's cards holder
computer_cards = []     ## Computer's cards holder
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_game_over = False
def deal_card():
    """Returns a random card form the deck"""
    return random.choice(cards)
def  calculate_score(cards):
   if sum(cards) == 21 and len(cards) == 2:
       return 0
   if 11 in cards and sum(cards) > 21:
       cards.remove(11)
       cards.append(1)
   return sum(cards)

def compare():
    if calculate_score(user_cards) == calculate_score(computer_cards):
        print("Draw!")
    elif calculate_score(computer_cards) == 0:
        print("User loses, computer has a blackjack!")
    elif calculate_score(user_cards) > 21:
        print("User went over and loses!")
    elif calculate_score(computer_cards) > 21:
        print("Computer went over and  loses!")
    else:
        if calculate_score(user_cards) > calculate_score(computer_cards):
            print("User wins!")
        elif calculate_score(user_cards) < calculate_score(computer_cards):
            print("Computer wins!")


for card in range(2):
    user_cards.append(deal_card())       # Dealing the user two cards
    computer_cards.append(deal_card())   # Dealing the computer two cards

time.sleep(1)
print(f"User's cards: {user_cards}, user's score: {sum(user_cards)}")
time.sleep(1)
print(f"Computer's first card: {computer_cards[0]}")

while not is_game_over:
    if calculate_score(user_cards) == 21:
        is_game_over = True
        print("User's blackjack! You win!")
        break
    elif calculate_score(computer_cards) == 21:
        print("Computer's blackjack, you lose!")
        is_game_over = True
        break

    elif not is_game_over:
        time.sleep(1)
        question = input("Do you wish to draw another card? (y/n) ")
        if question == "y":
            user_cards.append(deal_card())
            print(f"User's current cards: {user_cards}, current score: {calculate_score(user_cards)}")
            if calculate_score(user_cards) == 21:
                print("User's blackjack!")
                is_game_over = True
                break
            elif calculate_score(user_cards) > 21:
                is_game_over = True
                break
        elif question == "n":

            is_game_over = True
            break

while is_game_over:
    if calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    elif is_game_over:
        print(f"Computer's cards {computer_cards}, computer's score: {calculate_score(computer_cards)}")
        compare()
        break

question2 = input("Do you want to try again? (y/n) ")
if question2 == "y":
    os.system('clear')
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    os.system('clear')
    print(goodbye)
k=[2.4,5,6,7]
import  json
with open("heja_tu_lenka.json", "w") as file:
    json.dump(k, file,  indent=4)

