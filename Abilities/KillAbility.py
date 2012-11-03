from Player import Player
from Game import Game
from Event import Event
from Ability import Ability

class KillAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Kill", ["kill","k"])

    def getEventsFor(self, player, targetPlayer):
        """ Calls guardedEventsFor to check if the player has a kill.
        """
        return guardedEventsFor(self, player, targetPlayer)

    def onSuccess(self, player, targetPlayer):
        """ Sends messages to everyone, performs kill event.
        """
        BroadcastEvent(targetPlayer.getName() + ' has had a kill placed on them.')
        KillEvent(targetPlayer)
