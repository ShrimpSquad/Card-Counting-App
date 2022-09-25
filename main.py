import requests
import time
import os

class Player:
    def __init__(self, name: str, guess = 0) -> None:
        self.name = name
        self.guess = guess

    def player_name(self):
        self.name = input("What is your name? ")
        return self.name

    def value_guess(self):
        self.guessguess = input("What is your final value guess? ")
        return self.guess

class Deck:
    def __init__(self, deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")) -> None:
        self.deck = deck
        self.deck_info = self.deck.json()

    def find_deck_id(self):
        self.deck_id = self.deck_info["deck_id"]
        return self.deck_id

    def num_cards_remaining(self):
        self.cardsremaining = self.deck_info["remaining"]
        return self.cardsremaining

deck = Deck()
deck_id = deck.find_deck_id()
cards_remaining = deck.num_cards_remaining()
print(deck_id)
print(cards_remaining)

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
            return 7
        elif difficulty == "off": exit()

    def deal_player_in(self):
        draw_two_cards = requests.get(f"https://deckofcardsapi.com/api/deck/{deck.find_deck_id()}/draw/?count=2")
        cards_drawn = draw_two_cards.json()
        card1 = cards_drawn["cards"][0]["value"]
        card2 = cards_drawn["cards"][1]["value"]
        cards_remaining = cards_drawn["remaining"]
        return card1, card2, cards_remaining

    def player_cards_value_calc(self, card1, card2):
        pc_value = 0
        low_cards = ["2", "3","4", "5", "6"]
        high_cards = ["10", "JACK","QUEEN", "KING", "ACE"]
        if card1 in low_cards: pc_value += 1
        elif card1 in high_cards: pc_value -= 1
        if card2 in low_cards: pc_value += 1
        elif card2 in high_cards: pc_value -= 1
        return pc_value

    def deal_dealer_in(self):
        pass
    def calc_round_value(self, pc_value, c_value):
        pass
        
    def check_player_guess(self, player_guess):
        pass

class UserList:
    def __init__(self) -> None:
        pass

# GAME BELOW
gamebrain = GameBrain()
print(gamebrain.welcome_user())
difficulty = gamebrain.difficulty_choice()
amount_of_rounds = gamebrain.amount_of_rounds(difficulty)

for i in range(gamebrain.amount_of_rounds(difficulty)):
    card1, card2, cards_remaining = gamebrain.deal_player_in()
    if cards_remaining < 1:
        print("No more cards!")
        break
    else:
        print(f"Card1 is {card1}\nCard2 is {card2}\nCards left = {cards_remaining}")
        print(f"Round value: {gamebrain.player_cards_value_calc(card1, card2)}")
        gamebrain.round_time(difficulty)
        os.system("clear")

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