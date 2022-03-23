import random
class Suit:
    def __init__(self):
        self.cards = []
        self.power = 0
        self.allpower =0
        self.lowestcard = 0
        self.maxcard = 0
        self.rand = 0
        self.count = len(self.cards)
    def calcpower(self):
        max = 0
        low = 0
        self.power = 0
        self.allpower =0
        for card in self.cards:
            self.power += card.value
            if card.value > 10:
                self.allpower += 1
        self.suit = self.cards[0].suit
        for card in self.cards:
            if card.value > max:
                max = card.value
        for card in self.cards:
            if card.value == max:
                self.maxcard = card
        for card in self.cards:
            if card.value < low:
                low = card.value
        for card in self.cards:
            if card.value == low:
                self.lowestcard = card
        self.rand = random.choice(self.cards)
    def addcard(self,card):
        self.cards.append(card)
        self.calcpower()

class Sorter:
    def __init__(self,cards):
        if len(cards) > 0:
            self.hearts = Suit()
            self.clubs = Suit()
            self.diamonds = Suit()
            self.spades = Suit()
            self.suits = []
            for card in cards:
                if card.suit == "Hearts":
                    self.hearts.addcard(card)
                elif card.suit == "Spades":
                    self.spades.addcard(card)
                elif card.suit == "Clubs":
                    self.clubs.addcard(card)
                else:
                    self.diamonds.addcard(card)
            self.suits = [self.hearts,self.clubs,self.diamonds,self.spades]

class Logic:
    def __init__(self,player):                #suits are ["Diamonds","Clubs","Spades","Hearts"]
        self.player = player
        self.tarneeb = ""
        self.smart = 0
        if self.player.name == 1:
            self.smart = 1
    def sort(self,cards):
        sorter = Sorter(cards)
        self.hearts = sorter.hearts
        self.clubs = sorter.clubs
        self.diamonds = sorter.diamonds
        self.spades = sorter.spades
        self.suits = sorter.suits
    def callguess(self):
        self.sort(self.player.cards)
        max_guess = 0
        allpower =0
        tarneeb = ""
        for suit in self.suits:
            g = suit.power/13
            allpower += suit.allpower
            if g > 7 and g > max_guess:
                max_guess = g
        for st in self.suits:
            z = st.power/13
            if z == max_guess:
                tarneeb = suit.suit
        self.player.power = round(max_guess) + allpower
        return self.player.power,tarneeb
    def playthink(self,cardsPlayed):
        sorted_remaining = Sorter(self.player.remaining)
        self.sort(self.player.cards)
        self.remaining = self.player.remaining
        self.cardsPlayed = cardsPlayed
        self.suit = ""
        pos = len(cardsPlayed)+1
        if pos != 1:
            self.suit = cardsPlayed[0].suit
        def smart():
            if pos !=1: #if our position isn't the first
                for suit in self.suits:
                    if suit.count >0 and suit.suit == self.suit: #if we have a card of the suit being played
                        return self.player.play(suit.maxcard) #play the maximum card we have of that suit
                    elif suit.count > 0 and suit.suit == self.tarneeb: #if have tarneeb and dont have a card of the suit being played, play the max tarneeb
                        return self.player.play(suit.maxcard)
                    else: #if we don't have tarneeb and dont have a card of the suit being played
                        low_val = 0
                        for suit in self.suits:
                            if suit.lowestcard.value < low_val:
                                g = suit.lowestcard.value
                        for suit in self.suits:
                            if suit.lowestcard.value == low_val:
                                return self.player.play(suit.lowestcard) #play the lowest card of all suits we have
            if pos ==1: #if our position is the first
                mx =0
                for suit in self.suits:
                    if suit.count > 0 and suit.maxcard.value > mx:
                        mx = suit.maxcard.value
                for suit in self.suits:
                    if suit.maxcard.value == mx:
                        return self.player.play(suit.maxcard) #play the max card in our hand


        def notsmart():
            if pos != 1: # if we're not the first
                for suit in self.suits:
                    if suit.count >0 and suit.suit == self.suit: #we have a card of the suit being played
                        return self.player.play(suit.rand) #play a random card of that suit
                    else: #we dont have a card of the suit being played
                        return self.player.play(random.choice(self.player.cards)) #play a random card
            if pos ==1: #if we're the first
                return self.player.play(random(self.player.cards)) #play a random card that the player holds
        
        



        #PLAYYYY ------------
        if self.smart == 1:
            return(smart())
        if self.smart ==0:
            return(notsmart())

        
