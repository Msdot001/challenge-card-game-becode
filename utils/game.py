from player import Player

class Board:
    def __init__ (self,players):
        self.players = []
        self.turn_count = 0
        self.active_cards =[]
        self.history_card =[] 

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

        def start_game():
            