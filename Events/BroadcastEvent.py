from Event import Event

class BroadcastEvent(Event):
    def __init__(self, playerList, message):
        Event.__init__(self)
        self.playerList = playerList
        self.message = message

    def perform(self, game):
        for player in playerList:
            game.getOutbox().sendText(self.player.getContact(), self.message)
