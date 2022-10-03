import os
from player import Player
from deck import Deck
from gamebrain import GameBrain

# GAME CODE BELOW
gamebrain = GameBrain() 
deck = Deck()
deck_id = deck.find_deck_id()
cards_remaining = deck.num_cards_remaining()
print(gamebrain.welcome_user()) # Welcome user
difficulty = gamebrain.difficulty_choice() # Select difficulty
player1 = Player() # Generate player

total_value = 0
while True:
    for i in range(gamebrain.amount_of_rounds(difficulty)):
        card1, card2, card3, card4, cards_remaining = deck.deal_in()
        if cards_remaining < 1:
            print("No more cards! Reshuffling! The current value will stay the same.")
            deck.shuffle_deck()
            print(f"{deck.num_cards_remaining()} cards shuffled!")
            gamebrain.play_again()
        else:
            print(f"Your cards are {card1} and {card2}")
            print(f"Dealer's cards are {card3} and {card4}")
            print(f"{cards_remaining} cards left")
            round_value = gamebrain.player_cards_value_calc(card1, card2, card3, card4)
        total_value += round_value
        
        gamebrain.round_time(difficulty)
        os.system("clear")

    player_guess = player1.value_guess()
    gamebrain.check_player_guess(player_guess, total_value)
    gamebrain.play_again()

