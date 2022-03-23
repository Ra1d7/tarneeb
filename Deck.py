import random
from Card import Card
class Deck:
    def __init__(self): #initialize a deck
        self.cards = []
    def build(self): # fill the deck with cards
        for s in ["Diamonds","Clubs","Spades","Hearts"]:
            for v in range(1,14):
                c = Card(s,v)
                self.cards.append(c)
    def showdeck(self): #print the deck's cards
        for card in self.cards:
            card.show()
    def shuffle(self): # randomly shuffle the deck
        random.shuffle(self.cards)
    def remov(self,cardtoremove):
        for card in self.cards:
            if card.suit == cardtoremove.suit and card.value == cardtoremove.value:
                self.cards.remove(card)
    def draw(self): # remove a card from the deck and return it's class value
        return self.cards.pop()
    def count(self): # print how many cards are in the deck currently
        return len(self.cards)