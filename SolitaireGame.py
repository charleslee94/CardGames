from CardGame import CardGame
from Deck import Deck
import pprint
from random import shuffle

class SolitaireGame(CardGame):
    """ 4 stepStates
    0: idle
    1: draw Card
    2: select card
    3: select place

    TODO
    make the displayGameState information more clear as to what is what and trim out unnecessary stuff
    Move enums to their own files, possibly their own dirs
    separate the turn logic into its own class?

    """

    def __init__(self, ruleset=None):
        deck = Deck()
        self.deck = deck
        self.drawPile = []
        self.playPile = []
        self.stepState = 0
        self.foundations = [[] for i in range(0,4)]
        self.piles = [[] for i in range(0,7)]

    def endGame(self):
        pass

    def reshuffleDrawPile(self):
        playPile = self.playPile
        shuffle(playPile)
        print(playPile)
        ### TODO flip the cards
        self.drawPile = playPile
        self.playPile = []


    def drawCard(self):
        if len(self.drawPile) == 0:
            self.reshuffleDrawPile()

        print("Drawing card")
        lastCard = self.drawPile.pop()
        lastCard.flip()
        self.playPile.append(lastCard)

        self.displayGameState()

    def selectCard(self):
        pass

    def calculateLegalCardSelect(self):
        pass

    def calculateLegalPlaceSelect(self):
        ### Should be of descending order, alternating card num (suit)
        pass
    
    def step0(self, userInput):
        return {
                '1': self.drawCard(),
                '2': self.selectCard()
        }[userInput]

    def step1(self, userInput):
        pass

    def step2(self, userInput):
        pass


    def stepFn(self,userInput):
        ### TODO provide default case
        stepState = self.stepState
        return {
            0: self.step0(userInput),
            1: self.step1(userInput),
            2: self.step2(userInput)
        }[stepState]

    def incrementStep(self):
        self.state += 1

    def interpretInput(self, userInput):
        ### TODO restrict actions
        turnFn = self.stepFn(userInput)

    def actionPerformed(self):
        ### TODO implement generic to print action after completed
        pass

    def getSelectCardInput(self):
        pass

    def getSelectPlaceInput(self):
        pass

    def getInputPrompt(self):
        stepState = self.stepState
        return {
                0: "Draw or select a card?",
                1: self.getSelectCardInput(),
                2: self.getSelectPlaceInput()
        }[stepState]

    def getInputActions(self):
        stepState = self.stepState
        return {
                0: "1: Draw \n2: Select a Card\nPlease Select the Action Number",
                1: self.getSelectCardInput(),
                2: self.getSelectPlaceInput()
        }[stepState]

    def executeTurn(self):
        inputPrompt = self.getInputPrompt()
        inputActions = self.getInputActions()
        print(inputPrompt)
        action = input(inputActions)
        self.interpretInput(action)


    def startGame(self):
        deck = self.deck
        initialCards = deck.draw(28, False)
        self.setupPiles(initialCards)
        self.drawPile = deck.getCardList()
        self.displayGameState()
        self.runGame()

    def isGameWon(self):
        foundations = self.foundations
        gameWon = True
        for foundation in foundations:
            if len(foundation) < 13:
                gameWon = False
        return gameWon

        

    def runGame(self):
        while not self.isGameWon():
            self.executeTurn()

        self.endGame()

    def displayGameState(self):
        pprint.pprint(self.piles)
        pprint.pprint(self.foundations)
        pprint.pprint(self.playPile)
        # pprint.pprint(self.drawPile)


    def setupPiles(self, initialCards):
        piles = self.piles
        for pileIndex in range(0, len(piles)):
            normalizedIndex = pileIndex + 1
            currentPileCards = initialCards[:normalizedIndex]
            lastCard = currentPileCards.pop()
            lastCard.flip()
            currentPileCards.append(lastCard)
            piles[pileIndex] = currentPileCards
            initialCards = initialCards[normalizedIndex:]

        self.piles = piles;


# sol = SolitaireGame()
# sol.startGame()


