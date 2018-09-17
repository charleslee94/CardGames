from CardGame import CardGame
from Deck import Deck
import pprint
from functools import reduce
import pdb
from copy import deepcopy

""" Using the abstract method module import the ABC class and abstractmethod
In order to create a generic card game class that can function as an interface
for potential future games tom be implemented
"""

class MemoryMatchCardGame(CardGame):
    ### TODO display x number of cards in the beginning?
    ### TODO handle restrictions on inputs better (int only, selected cards must be display false
    ### TODO 2nd card cannot be same as first
    ### TODO change the colors of the inputs so that theyre clearer
    ### TODO cleanup inputs

    def __init__(self, deck, width):
        ### TODO if width**2 > len(deck.cardList) or width not even throw error
        self.stepState = 0
        self.width = width
        self.matches = 0
        self.turnCount = 1
        self.gameState = {
            'board': [],
            'currentCard': None,
            'currentCardIndex': None
        }
        self.deck = deck
        super().__init__()

    ### Setup Function ###

    def setupBoard(self):
        board = [[] for i in range(0,self.width)]
        deck = self.deck
        dimensions = int((self.width ** 2) / 2)
        boardCards = deck.draw(dimensions)
        boardCards = boardCards + deepcopy(boardCards)
       
        for i in range(0, len(board)):
            currentCardsSlice = boardCards[:len(board)]
            board[i] = currentCardsSlice
            boardCards = boardCards[len(board):]

        self.assignCardbackNumbers(board)
        self.displayGameState()

    def setupGame(self):
        self.setupBoard()


    ### Helper functions ###

    def getBoard(self):
        return self.gameState.get('board')


    def setBoard(self, board):
        self.gameState['board'] = board

    def displayGameState(self):
        board = self.getBoard()
        for row in board:
            pprint.pprint(row)
        print("\n")

    def incrementMatchedCount(self):
        self.matches += 2

    def incrementTurnCount(self):
        self.turnCount += 1

    def incrementStep(self, step=1):
        self.stepState += step

    def decrementStep(self, step=1):
        self.stepState -= step

    def isGameWon(self):
        if self.matches == self.width ** 2:
            return True
        return False

    def flipBoard(board):
        for row in board:
            for card in row:
                card.flip()
        return board

    def assignCardbackNumbers(self, board):
        for rowNum in range(0, len(board)):
            row = board[rowNum]
            for cardNum in range(0, len(row)):
                card = board[rowNum][cardNum]
                card.cardBack = len(row) * rowNum + cardNum + 1
        self.setBoard(board)

    ### Turn Logic ###

    def printIntroduction(self):
        print("Hello and welcome to Memory Matching, select cards to flip them over and match two that are the same in the least amount of turns you can!")
        print("\n")

    def stepFn(self):
        stepState = self.stepState
        stepFunctions = {
            0: self.flipFirstCard,
            1: self.flipSecondCard
        }
        ### TODO better error handling
        return stepFunctions.get(stepState, "error")

    def getCardByBackNumber(self, number):
        board = self.getBoard()
        if number % self.width == 0:
            row = (number // self.width) - 1
            col = self.width - 1
            return board[row][col]
        # Floor division, neat python thing
        row = number // self.width
        col = number - (row * self.width) - 1
        return board[row][col]


    def flipFirstCard(self, userInput):
        card = self.getCardByBackNumber(userInput)
        card.flip()
        self.gameState['currentCard'] = card
        self.gameState['currentCardIndex'] = int(userInput)

        self.incrementStep()
        self.displayGameState()

    def flipSecondCard(self, userInput):
        card = self.getCardByBackNumber(userInput)
        cardMatches = self.checkCardMatch(card)

        card.flip()
        if cardMatches:
            self.incrementMatchedCount()
            self.gameState['currentCard'] = None
            self.gameState['currentCardIndex'] = None
            print("Congratulations, you found a match!")
            print("\n")

        else:
            self.displayGameState()
            print("Did not match")
            print("\n")
            self.gameState.get('currentCard').flip()
            card.flip()
        self.decrementStep()
        self.displayGameState()

    def checkCardMatch(self, card):
        currentCard = self.gameState.get('currentCard')
        if (currentCard and currentCard.value, currentCard.suit) == (card.value, card.suit):
            return True
        return False


    def interpretInput(self, userInput):
        ### TODO restrict actions
        userInput = int(userInput)
        stepFunction = self.stepFn()
        stepFunction(userInput)

    def actionPerformed(self, action):
        ### TODO implement generic to print action after completed
        pass

    def getInputPrompt(self):
        stepState = self.stepState
        return {
                0: "Select first card by number: ",
                1: "Select second card by number: "
        }[stepState]

    ### Main Game Logic ###

    def startGame(self):
        self.setupGame()
        self.printIntroduction()
        self.runGame()

    def runGame(self):
        while not self.isGameWon():
            self.executeTurn()

        self.endGame()

    def executeTurn(self):
        print("it is turn %s" % self.turnCount)
        inputPrompt = self.getInputPrompt()
        action = input(inputPrompt)
        self.interpretInput(action)
        self.incrementTurnCount()

    def endGame(self):
        aArt = """\
        
 /$$     /$$ /$$$$$$  /$$   /$$       /$$$$$$$  /$$$$$$ /$$$$$$$        /$$$$$$ /$$$$$$$$       /$$
|  $$   /$$//$$__  $$| $$  | $$      | $$__  $$|_  $$_/| $$__  $$      |_  $$_/|__  $$__/      | $$
 \  $$ /$$/| $$  \ $$| $$  | $$      | $$  \ $$  | $$  | $$  \ $$        | $$     | $$         | $$
  \  $$$$/ | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$  | $$        | $$     | $$         | $$
   \  $$/  | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$  | $$        | $$     | $$         |__/
    | $$   | $$  | $$| $$  | $$      | $$  | $$  | $$  | $$  | $$        | $$     | $$             
    | $$   |  $$$$$$/|  $$$$$$/      | $$$$$$$/ /$$$$$$| $$$$$$$/       /$$$$$$   | $$          /$$
    |__/    \______/  \______/       |_______/ |______/|_______/       |______/   |__/         |__/
                                                                                                   
                                                                                                   
                                                                                                   
"""
        print(aArt)



deck = Deck()
mem = MemoryMatchCardGame(deck, 4)
mem.startGame()

