from logic import Logic
class Player():
        def __init__(self,team,name): #initialize a player and give him a team
            self.team = team
            self.cards = []
            self.cnt =0
            self.round = 0
            self.isdeclarer = False
            self.remaining =[]
            self.power =0
            self.turn =0
            self.name = "Player" + str(name)
            self.logic = Logic(self)
        def showcards(self): # print the cards that the player holds
            for card in self.cards:
                card.show()
        def play(self,cardtoplay): #the player plays a card, removing it from their hand and returning it's class value
            self.remaining = self.round.game.compdeck.cards
            self.cnt = self.cnt-1
            for card in self.cards:
                if card.suit == cardtoplay.suit and card.value == cardtoplay.value:
                    self.cards.remove(card)
                    for card in self.remaining:
                       if card in self.cards:
                           self.remaining.remove(card)
                    print(f"Playing {card.value} of {card.suit} for {self.name}")
                    return card
        def addcard(self,card): #the player gets handed a card and its added to his cards increasing the count by 1
            self.cards.append(card)
            self.cnt = self.cnt+1
