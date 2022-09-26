import requests
import time
import os

class Player:
    def __init__(self, guess = 0) -> None:
        self.guess = guess

    def value_guess(self):
        self.guess = input("What is your final value guess? ")
        return self.guess

class Deck:
    def __init__(self, deck = requests.get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")) -> None:
        self.deck = deck
        self.deck_info = self.deck.json()

    def find_deck_id(self):
        self.deck_id = self.deck_info["deck_id"]
        return self.deck_id

    def num_cards_remaining(self):
        self.cardsremaining = self.deck_info["remaining"]
        return self.cardsremaining

class GameBrain:
    def __init__(self, difficulty: str = "") -> None:
        self.difficulty = difficulty

    def welcome_user(self):
        return "Welcome to the card counting game!"

    def difficulty_options(self):
        return "\n1 for Easy\n2 for Medium\n3 for Hard\n"

    def difficulty_choice(self):
        options = ["1", "2", "3", "off"]
        difficulty = ""
        while difficulty not in options:
            try:
                difficulty = input(f"{self.difficulty_options()}Select a difficulty ")
                if difficulty not in options:
                    raise ValueError
            except ValueError:
                print("Please select a correct difficulty option")
        return difficulty

    def round_time(self, difficulty):
        if difficulty == "1": 
            return time.sleep(4)
        elif difficulty == "2": 
            return time.sleep(3)
        elif difficulty == "3": 
            return time.sleep(2)
        elif difficulty == "off": exit()
    
    def amount_of_rounds(self, difficulty):
        if difficulty == "1": 
            return 3
        elif difficulty == "2": 
            return 5
        elif difficulty == "3": 
            return 2
        elif difficulty == "off": exit()

    def deal_player_in(self):
        draw_two_cards = requests.get(f"https://deckofcardsapi.com/api/deck/{deck.find_deck_id()}/draw/?count=4")
        cards_drawn = draw_two_cards.json()
        card1 = cards_drawn["cards"][0]["value"]
        card2 = cards_drawn["cards"][1]["value"]
        card3 = cards_drawn["cards"][2]["value"]
        card4 = cards_drawn["cards"][3]["value"]
        cards_remaining = cards_drawn["remaining"]
        return card1, card2, card3, card4, cards_remaining

    def player_cards_value_calc(self, *args):
        pc_value = 0
        low_cards = ["2", "3","4", "5", "6"]
        high_cards = ["10", "JACK","QUEEN", "KING", "ACE"]
        for i in args: 
            if i in low_cards: pc_value +=1
            elif i in high_cards: pc_value -=1
        return pc_value

    def deal_dealer_in(self):
        draw_two_cards = requests.get(f"https://deckofcardsapi.com/api/deck/{deck.find_deck_id()}/draw/?count=2")
        cards_drawn = draw_two_cards.json()
        card1 = cards_drawn["cards"][0]["value"]
        card2 = cards_drawn["cards"][1]["value"]
        cards_remaining = cards_drawn["remaining"]
        return card1, card2, cards_remaining

    def check_player_guess(self, player_guess, total_value):
        if total_value == player_guess:
            return True
        else:
            return False


# GAME CODE BELOW
gamebrain = GameBrain() 
deck = Deck()
deck_id = deck.find_deck_id()
cards_remaining = deck.num_cards_remaining()

print(gamebrain.welcome_user()) # Welcome user
difficulty = gamebrain.difficulty_choice() # Select difficulty

player1 = Player() # Generate player

for i in range(gamebrain.amount_of_rounds(difficulty)):
    total_value = 0
    card1, card2, card3, card4, cards_remaining = gamebrain.deal_player_in()
    if cards_remaining < 1:
        print("No more cards!")
        break
    else:
        print(f"Your cards are {card1} and {card2}")
        print(f"Dealer's cards are {card3} and {card4}")
        print(f"{cards_remaining} cards left")
        round_value = gamebrain.player_cards_value_calc(card1, card2, card3, card4)
    total_value += round_value
    print(round_value)
    print(total_value)
    gamebrain.round_time(difficulty)
    os.system("clear")

player_guess = player1.value_guess()
print(player_guess)
result = gamebrain.check_player_guess(player_guess, total_value)
if result:
    print("Correct! Well done")
else: 
    print(f"Sorry, that is not correct")


# Functions needed:
# Value Guess
# DECK
# Create new deck - requests.get(deckofcardsapi)
# Create new object in Deck class from request
# Attributes of deck include...
#   cards remaining
#   
# GAME BRAIN
# Choose difficulty 
#   Hard = 1 second show, 15 rounds
#   Medium = 2 second show, 10 rounds
#   Easy = 3 second show, 5 rounds
#   Custom = User selected seconds, User selected rounds
# Deal cards
#   Deal for dealer
#   Deal for player
# Calculate value of the 4 cards, (current score += value)
# Show hands
#   Print dealer cards (for X seconds)
#   Show player cards (for X seconds)
# Repeat game for i in rounds
# Compare user guess to current value
# Respond
# Play again?