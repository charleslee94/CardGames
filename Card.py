from termcolor import colored

from CardColor import CardColor
"""
This is the basic unit of a deck
Card can have value, and color
"""
class Card():
    def __init__(self, suit, value, display=False):
        self.suit = suit
        self.value = value
        self.display = display

    def __repr__(self):
        colors = {
            0: 'red',
            1: 'blue',
            2: 'green',
            3: 'purple'
        }
        cardColor = colors[self.suit]
        cardValue = self.getCardValue()
        if self.display:
            return colored(("(%s)" % (cardValue)), cardColor)
        return "Face Down"

    def getCardValue(self):
        if self.value < 10:
            return self.value
            faceCards = {
                11: 'J',
                12: 'Q',
                13: 'K'
            }
            return faceCards.get(self.value)

        
    def flip(self):
        self.display =  not self.display

    def faceUp(self):
        self.display = True

    def faceDown(self):
        self.display = False

