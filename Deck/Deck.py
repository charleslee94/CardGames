from collections import OrderedDict
from Card import Card
import pprint
from random import shuffle


class Deck():
    """
    This is the deck class
    can have as many cards as you want, but the default will be 52 of 4 suits
    """
    def __init__(self, ruleset=None):

        self.drawCount = 0
        self.cardsDrawn = 0
        if ruleset is None:
            self.cardList = self.buildDefaultDeck()
            # self.shuffleCards()

    def buildDefaultDeck(self):
        cardList = []
        suitCount = 4
        cardCount = 13
        for suit in range(0, suitCount):
            for value in range(1, cardCount + 1):
                cardList.append(Card(suit, value))
        return cardList


    def getCardList(self):
        return self.cardList

    def setCardList(self, newCardList):
        self.cardList = newCardList

    def printCardList(self):
        pp = pprint.PrettyPrinter(indent=4)
        cardList = self.getCardList()
        for card in cardList:
            pp.pprint((card.suit, card.value))
        self.getDeckInfo()

    def getDeckInfo(self):
        remaining = str(len(self.getCardList())) + " are remaining."
        drawCount = str(self.drawCount) + " times drawn."
        cardsDrawn = str(self.cardsDrawn) + " cards drawn."
        print(remaining)
        print(drawCount)
        print(cardsDrawn)


    def shuffleCards(self):
        cardList = self.cardList
        return shuffle(cardList)

    def draw(self, number, countDraws=True):
        cardList = self.getCardList()
        drawnCards = cardList[0:number]
        restOfDeck = cardList[number: len(cardList)]

        if (countDraws):
            self.drawCount += 1
            self.cardsDrawn += number

        self.setCardList(restOfDeck)
        return drawnCards

