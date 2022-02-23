
# Creating a class Symbol with two attribute (icon and value)

class Symbol:
    icon = ["♥", "♦", "♣", "♠"]                                                    # contains the 4 different pattern that will be used to create the card
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]     # contains the 13 different value that will be used to create the card
    color = ""

    """A simple attempt to mode a symbol of card"""
    def __init__(self, icon, color = ""):
        """Initialize color and icon attribute"""
        self.color = color
        self.icon = icon           

    def __str__(self):   
        return f"{self.color},{self.icon }"                                         #turns list (icon) into a stings

# Creating a class Card that inherits Symbol with additional attribute value

class Card(Symbol):
    """Representing aspects of a Symbol"""
    def __init__(self,icon, value):
        super().__init__(icon, color ="")                                           #Inheritance from the Class Symbols
        self.value = value

    def __str__(self):                                                             # method used to create a card, by combining the icons and values 
           return f"{Card.value[self.value]}{Card.icon[self.icon]}"





