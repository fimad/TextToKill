from Player import Player
from Game import Game
from Event import Event

class KillAbility(Ability):

    def __init__(self):
        self.abilityName = 'Kill'
        self.keywords = ['kill', 'k']

    def getEventsFor(self, player, targetPlayer):
        """ Calls guardedEventsFor to check if the player has a kill.
        """
        return guardedEventsFor(self, player, targetPlayer)

    def onSuccess(self, player, targetPlayer):
        """ Sends messages to everyone, performs kill event.
        """
        BroadcastEvent(targetPlayer.getName() + ' is dying and has 15 minutes to live.')
        KillEvent(targetPlayer)
