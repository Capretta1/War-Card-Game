from Card import suits, Card, ranks
import random

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #CREATE CARD OBJECT
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    #SHUFFLE CARDS IN DECK
    def shuffle(self):
        random.shuffle(self.all_cards)

    #this method grabs one of the cards from the list
    def deal_one(self):
        return self.all_cards.pop()




