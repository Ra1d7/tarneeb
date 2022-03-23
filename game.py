import time
import random
from Card import Card
from Deck import Deck
from Round import Round
from Team import Team
from Player import Player
class Game:

    def declare(self):
        self.max_declare =0
        for player in self.players:
            if player.logic.callguess()[0] > self.max_declare:
                self.max_declare = player.logic.callguess()[0]
        for player in self.players:
            if player.logic.callguess()[0] == self.max_declare:
                player.isdeclarer = True
                self.tarneeb = player.logic.callguess()[1]
    def runrounds(self):
        for i in range(13):
            round = Round(self.tarneeb,self)
            round.play()
    def showscore(self):
        for team in self.teams:
            print(f"Team {team.id} Has {team.score} score!")
    def __init__(self): #initialize a game
        #initialize a deck and build it and shuffle it
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()
        self.compdeck = Deck()
        self.compdeck.build()
        self.tarneeb = ""
        # create teams
        self.team1 = Team(1)
        self.team2 = Team(2)
        self.teams = [self.team1,self.team2]
        # creating players 
        self.player1 , self.player2 , self.player3, self.player4 = Player(self.team1,1),Player(self.team1,2),Player(self.team2,3),Player(self.team2,4)
        self.players = [self.player1,self.player2,self.player3,self.player4]
        
        # assigning cards to players
        for player in self.players:
            for i in range(13):
                player.addcard(self.deck.draw())
                for card in player.cards:
                    card.setplayer(player)
        self.declare()
        for player in self.players:
            player.logic.tarneeb = self.tarneeb
        print(f"[+] TARNEEB IS {self.tarneeb} , with value of {self.max_declare}")
        self.runrounds()
        self.showscore()
    def remain(self,team): # keeps track of the remaining cards
        remaining = []
        for player in team:
            for card in player.cards:
                remaining.append(card)
        return remaining



game1 = Game()