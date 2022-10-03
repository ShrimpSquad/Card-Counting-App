import requests

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

    def shuffle_deck(self):
        self.deck = requests.get(f"https://www.deckofcardsapi.com/api/deck/{self.find_deck_id()}/shuffle/")

    def deal_in(self):
        draw_two_cards = requests.get(f"https://www.deckofcardsapi.com/api/deck/{self.find_deck_id()}/draw/?count=4")
        cards_drawn = draw_two_cards.json()
        card1 = cards_drawn["cards"][0]["value"]
        card2 = cards_drawn["cards"][1]["value"]
        card3 = cards_drawn["cards"][2]["value"]
        card4 = cards_drawn["cards"][3]["value"]
        cards_remaining = cards_drawn["remaining"]
        return card1, card2, card3, card4, cards_remaining