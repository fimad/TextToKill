from Event import Event
from Events.SendEvent import SendEvent

class KillEvent(Event):
    def __init__(self, playerName):
        Event.__init__(self, 15*60)
        self.playerName = playerName

    def perform(self, game):
        player = game.getPlayer(self.playerName)
        game.getAbility("Kill").removeSpecificKill(self)
        game.removePlayer(self.playerName)

        game.addEvents([SendEvent(player,"The world mourns for the loss of a hero. You have died.") ,
        BroadcastEvent("Lo! Fellow adventurers, a red sun rises, your fellow '"+playerName+"' has died of dysentery")])
