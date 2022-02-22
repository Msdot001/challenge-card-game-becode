import random 
from random import shuffle
from xml.etree.ElementTree import C14NWriterTarget


class Symbol:
    icon = ["♥", "♦", "♣", "♠"]
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    color = ""

    """A simple attempt to mode a symbol of card"""
    def __init__(self, icon, color = ""):
        """Initialize color and icon attribute"""
        self.color = color
        self.icon = icon

    def __str__(self):   
        return f"{self.color},{self.icon }"

class Card(Symbol):
    """Representing aspects of a Symbol"""
    def __init__(self,icon, value):
        super().__init__(icon, color ="")
        self.value = value

    def __str__(self):
           return f"{Card.value[self.value]}{Card.icon[self.icon]}"





