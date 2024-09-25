## Blackjack Game
This project implements a simple command-line Blackjack game where the player competes against the computer. The game uses a standard deck of cards (without suits) and follows the basic rules of Blackjack.

## How the Game Works
Game Start: Both the user and the computer are dealt two cards at the beginning of the game. The user sees both of their cards and one of the computer's cards.
User Turn: The user is asked if they would like to draw another card or stick with their current hand. If the user's hand totals more than 21, they lose. If their hand totals exactly 21, it's a Blackjack, and the user wins.
Computer Turn: The computer automatically draws cards until its total reaches 17 or higher. If the computer busts (i.e., goes over 21), the user wins.
Game End: The winner is determined based on the closest hand to 21 without exceeding it. If both have the same score, the game is a draw.
Replay: The player can choose to restart the game or exit after the results are displayed.
## Project Structure
The code contains the following key components:

deal_card(): Returns a random card from the deck.
calculate_score(cards): Calculates the total score for a given set of cards. It also handles the special case of an Ace, which can be counted as either 1 or 11, depending on the situation.
compare(): Compares the user's score with the computer's score to determine the winner.
Game Loop: Handles the game flow for both the user and the computer, and manages the drawing of cards, score checks, and game end logic.

## How to Run
Ensure you have Python installed on your system.
Install the necessary dependencies using:
pip install art
## Run the script using:
python blackjack_game.py
## Example Output
Welcome to Blackjack!
User's cards: [7, 10], user's score: 17
Computer's first card: 6
Do you wish to draw another card? (y/n) y
User's current cards: [7, 10, 3], current score: 20
Computer's cards [6, 9, 4], computer's score: 19
User wins!
Do you want to try again? (y/n) n
Goodbye!
## Game Rules
Aces can count as 1 or 11.
A hand totaling exactly 21 with two cards is a Blackjack.
The computer must keep drawing cards until its score reaches at least 17.
The user can keep drawing cards unless their score exceeds 21.
## Dependencies
Python 3.x
art library for displaying ASCII art in the terminal.
To install the art module, use the following command:
pip install art
