class Card:
    def __init__(self,suit,val): #each card will have a suit and a value
        self.suit = suit
        self.value = val
        self.score = 0
        if self.value == 1:
            self.score =13
        else:
            self.score = self.value-1
    def show(self): #prints the card's suit and value to the terminal
        print(f"{self.value} of {self.suit}")
    def setplayer(self,player):
         self.player = player
         self.team = self.player.team