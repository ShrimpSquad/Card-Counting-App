class Player:
    def __init__(self, guess = 0) -> None:
        self.guess = guess

    def value_guess(self):
        while True:
            try:
                self.guess = input("What is your final value guess my dude? ")
                if self.guess.lower() == "off":
                    exit()
                elif not self.guess.lstrip("-").isdigit():
                    raise ValueError
                else: 
                    return self.guess
            except ValueError:
                print("That's not a number! Try again.")