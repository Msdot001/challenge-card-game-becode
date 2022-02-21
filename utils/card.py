icon= ["heart", "diamonds", "spades" , "clubs"]
value = ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']
color = ""
import random 


from random import shuffle

class Symbol:
    """A simple attempt to mode a symbol of card"""
    def __init__(self, color = "", icon=["heart", "diamonds", "spades" , "clubs"]):
        """Initialize color and icon attribute"""
        self.color = color
        self.icon = icon

    def sample(self):
        """Return a neatly formatted sample"""
        for _icon in icon:
            result = color + _icon
            return result


white = Symbol()   
print(white.sample())      

