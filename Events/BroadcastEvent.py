from Event import Event

class BroadcastEvent(Event):
    def __init__(self, message):
        Event.__init__(self)
        self.message = message

    def perform(self, game):
        for name in game.getPlayerNames():
            game.getOutbox().sendText(game.getPlayer(name).getContact(), self.message)
