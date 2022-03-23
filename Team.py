class Team():
    def __init__(self,id):
        self.score = 0
        self.players = []
        self.id = id
        for player in self.players:
            player.team = self