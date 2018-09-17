

""" Using the abstract method module import the ABC class and abstractmethod
In order to create a generic card game class that can function as an interface
for potential future games tom be implemented
"""
from abc import ABC, abstractmethod

class CardGame(ABC):

    def __init__(self):
        self.stepState = 0
        self.gameState = {}
        super().__init__()

    @abstractmethod
    def startGame():
        pass

    @abstractmethod
    def setupGame():
        pass

    @abstractmethod
    def endGame():
        pass

    @abstractmethod
    def executeTurn():
        pass

    @abstractmethod
    def stepFn(self,userInput):
        pass

    @abstractmethod
    def incrementStep(self, step=1):
        self.incrementStep += step

    @abstractmethod
    def interpretInput(self, userInput):
        ### TODO restrict actions
        turnFn = self.stepFn(userInput)

    @abstractmethod
    def actionPerformed(self, action):
        ### TODO implement generic to print action after completed
        pass

    @abstractmethod
    def getInputPrompt(self):
        pass

    def getInputActions(self):
        pass

    @abstractmethod
    def executeTurn(self):
        pass
        # inputPrompt = self.getInputPrompt()
        # inputActions = self.getInputActions()
        # print(inputPrompt)
        # action = input(inputActions)
        # self.interpretInput(action)


    @abstractmethod
    def startGame(self):
        pass

    @abstractmethod
    def isGameWon(self):
        pass

    def runGame(self):
        while not self.isGameWon():
            self.executeTurn()

        self.endGame()

    @abstractmethod
    def displayGameState(self):
        pprint.pprint(self.gameState)
