
from card import Card
from random import random
from random import shuffle

class Player:
    def __init__(self,player_name):
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
        self.player_name = player_name  

    def play(self):
        card = random(self.cards)
        self.history.append(card)
        print(f"{self.player_name} {self.turn_count} played: {card.value} {card.icon}")
        return card

class Deck:
    """Initializing the attribute of class Deck"""
    def __init__(self): 
        self.cards = []
      

    def fill_deck(self):
        for icon in range(4):
            for value in range(13):
                self.cards.append(Card(icon, value))
                

    def shuffle(self):
        shuffle(self.cards)

    def distribute(self,players):
        self.players = []
        

total_card = Deck()
total_card.fill_deck()
total_card.shuffle()
for card in total_card.cards:
    print(card)
