from model.Game import Game


class CardGame(Game):
    def __init__(self, quantity_of_cards):
        self.quantity_of_cards = quantity_of_cards
    def __str__(self):
        return "Quantity of cards : % s\n" % \
            (self.quantity_of_cards)