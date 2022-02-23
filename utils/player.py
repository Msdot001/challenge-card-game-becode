
from card import Card                                           # Importation of class Card from card.py inorder to used it in this file
from random import random
from random import shuffle

#to create a player and the attribute 

class Player:
    def __init__(self,player_name):
        self.cards = []                                        #List containing the total cards that will be used during the game
        self.turn_count = 0                                    
        self.number_of_cards = 0
        self.history = []
        self.player_name = player_name  

    def play(self):                                             # A play() method is used demonstrate the feature of each player during the game 
        card = random(self.cards)                               
        self.history.append(card)
        print(f"{self.player_name} {self.turn_count} played: {card.value} {card.icon}")
        return card

#to create the total card(52) which will used during the game
class Deck:                                                    
    """Initializing the attribute of class Deck"""
    def __init__(self): 
        self.cards = []                                         # this will hold a list of Card objects
      

    def fill_deck(self):                                       # creating the total card(13 value * 4 icons = 52 cards)
        for icon in range(4):
            for value in range(13):
                self.cards.append(Card(icon, value))
                

    def shuffle(self):                                         # shuffle() method ensure that the total card created is randonly shuffle  
        """Shuffles the deck"""
        shuffle(self.cards)

    def distribute(self,players):                              # distribute() method is a list that will contain the distribution of cards among the players
        self.players = []
        

total_card = Deck()
total_card.fill_deck()
total_card.shuffle()
for card in total_card.cards:
    print(card)
