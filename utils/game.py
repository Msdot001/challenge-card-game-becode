
from player import Player, Deck
from card import Card
from random import shuffle,random
class Board:
    def __init__ (self,players):
        self.players = []     # this will hold a list of Player objects
        self.turn_count = 0
        self.active_cards =[]
        self.history_card =[] 



        #to create name of individual players for the game

        name1 = input("player 1 name: ")
        name2 = input("player 2 name: ")
        name3 = input("player 3 name: ")
        name4= input("player 4 name: ")

        #Creating 4 player from the class player created in the player.py
        p1 = Player(name1)
        p2 = Player(name2)
        p3 = Player(name3)
        p4 = Player(name4)

        # appending the players created (p1-p4) into the players list created above
        players.append(p1)
        players.append(p2)
        players.append(p3)
        players.append(p4)
      
        """
        #short code
        players list created, append class Player and name (input)
        self.players.append(Player(name1))
        self.players.append(Player(name2))
        self.players.append(Player(name3))
        self.players.append(Player(name4))
        """


        #filling the card with deck and distribute one card to each player per turn 

        self.deck = Deck()  # object deck from the class Deck
    
        def start_game(self):

            self.deck.fill_deck() # to fill
            self.deck.shuffle()
            self.deck.distribute()
            while len(self.cards) > 0:     #Each player should will have continue have chance to pick the card until the card is zero
                for eachPlayer in self.players:
                     eachPlayer.play()       #Each player playing
                     self.turn_count += 1
                     print("Turn count: ",self.turn_count)
                     self.active_cards.append(eachPlayer.play())
                     print(self.active_cards)
                     self.history_card.append(eachPlayer.play())
                     print(len(self.history_card))
                    
                

                
                




