class Round(): #initialize a round class
    def __init__(self,tarneeb,game):
        self.game = game
        self.tarneeb = tarneeb
        self.scores = []
        self.cards = []
        self.players = []
        startindex =0
        game.player1.isdeclarer = True
        for player in game.players: # assign turn to each player and add him to self.players
            if player.isdeclarer == True:
                startindex = game.players.index(player)
                for i in range(4):
                    if startindex >= len(game.players):
                        self.players.append(game.players[startindex-len(game.players)])
                    else:
                        self.players.append(game.players[startindex])
                    startindex +=1
        for playerr in self.players: #assign turn to each player
            playerr.turn = self.players.index(playerr)
        for player in self.players:
            player.round = self
    def playerplay(self,player):
        cardtoplay = player.logic.playthink(self.game.compdeck.cards)
        self.game.compdeck.remov(cardtoplay)
        self.cards.append(cardtoplay)
    def play(self):
        c = 0
        if len(self.cards) ==0:
            self.playerplay(self.players[0])
            self.suit = self.cards[0].suit
            self.players.remove(self.players[0])
        self.suit = self.cards[0].suit
        print(f"The Suit is {self.suit}")
        for player in self.players:
            self.playerplay(player)
        self.wincard()
    def wincard(self):
        for card in self.cards:
            if card.suit == self.tarneeb:
                card.score = 100 + card.score
            elif card.suit == self.suit:
                card.score = card.score
            else:
                card.score = 0
            self.scores.append(card.score)
        max_score = max(self.scores)
        for card in self.cards:
            if card.score == max_score:
                for player in self.game.players:
                    for crd in player.cards:
                        if crd.value == card.value and crd.suit == card.suit:
                            print(f"Winning card is {crd.value} of {crd.suit} for {crd.player.name} of team {crd.player.team.id}")
                            crd.player.team.score = crd.player.team.score +1
