from Event import Event

class SendEvent(Event):
    def __init__(self, player, message):
        Event.__init__(self)
        self.player = player
        self.message = message

    def perform(self, game):
        game.getOutbox().sendText(self.player.getContact(), self.message) #TODO: update player.getContact() once it's API is defined
