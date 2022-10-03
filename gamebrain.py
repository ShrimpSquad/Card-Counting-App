import time

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
            return time.sleep(6)
        elif difficulty == "2": 
            return time.sleep(4)
        elif difficulty == "3": 
            return time.sleep(2)
        elif difficulty == "off": exit()
    
    def amount_of_rounds(self, difficulty):
        if difficulty == "1": 
            return 3
        elif difficulty == "2": 
            return 4
        elif difficulty == "3": 
            return 5
        elif difficulty == "off": exit()

    def player_cards_value_calc(self, *args):
        pc_value = 0
        low_cards = ["2", "3","4", "5", "6"]
        high_cards = ["10", "JACK","QUEEN", "KING", "ACE"]
        for i in args: 
            if i in low_cards: pc_value +=1
            elif i in high_cards: pc_value -=1
        return pc_value

    def check_player_guess(self, player_guess, total_value):
        if total_value == int(player_guess):
            print(f"Correct! The total value is {total_value}")
        else:
            print(f"Wrong! The total value is {total_value}")

    def play_again(self):
        answer = input("Play again? Y or N ")
        yes_or_no = ["y", "n"]
        while answer.lower() not in yes_or_no:
            try:
                answer = input("Play again? Y or N ")
                if answer not in yes_or_no:
                    break
                else: raise ValueError
            except ValueError: "That is not a correct answer"
        if answer == "y":
            pass
        else:
            exit()