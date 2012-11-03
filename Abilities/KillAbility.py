from Player import Player
from Game import Game
from Event import Event
from Ability import Ability

class KillAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Kill", ["kill","k"])
        self.activeKills = {}

    def getEventsFor(self, game, player, targetPlayer):
        """ Calls guardedEventsFor to check if the player has a kill.
        """
        return guardedEventsFor(self, player, targetPlayer)

    def onSuccess(self, game, player, targetPlayer):
        """ Sends messages to everyone, performs kill event.
        """
        if Game.isValidPlayer(targetPlayer):
            events = []
            events.append(BroadcastEvent(targetPlayer.getName() + ' has had a kill placed on them.'))
            events.append(KillEvent(targetPlayer))
            return (True, events)
        else:
            return (False, SendEvent(player, 'Improperly formatted kill.'))
