class Card:

    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
              'Ten': 10, 'Jack': 11, 'Que': 12, 'King': 13, 'Ace': 14}
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    #ATRRIBUTES ARE SUIT, RANK AND VALUE(WHERE THE PROGRAM WOULD DETERMINE THE VALUE BY THE HELP OF A DICTIONARY)
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value= self.values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit