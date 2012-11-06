from Event import Event
from Events.SendEvent import SendEvent
from Events.BroadcastEvent import BroadcastEvent

class KillEvent(Event):
    def __init__(self, playerName):
        Event.__init__(self, 15*60)
        self.playerName = playerName

    def perform(self, game):
        player = game.getPlayer(self.playerName)
        game.getAbility("Kill").removeSpecificKill(self.playerName,self)
        game.removePlayer(self.playerName)

        return [SendEvent(player,"The world mourns for the loss of a hero. You have died.") ,
        BroadcastEvent("Lo! Fellow adventurers, a red sun rises, your fellow '"+self.playerName+"' has died of dysentery and knife wounds.")]
