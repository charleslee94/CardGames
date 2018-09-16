

""" Using the abstract method module import the ABC class and abstractmethod
In order to create a generic card game class that can function as an interface
for potential future games tom be implemented
"""
from abc import ABC, abstractmethod

class CardGame(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def startGame():
        pass

    @abstractmethod
    def endGame():
        pass

    @abstractmethod
    def executeTurn():
        pass
