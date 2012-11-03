from Player import Player
from Game import Game
from Event import Event
from Ability import Ability
from KillAbility import KillAbility

class SaveAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Save", ["save","sa"])

    def getEventsFor(self, game, player, targetPlayer):
        """ Calls guardedEventsFor to check if the player has a save.
        """
        return guardedEventsFor(self, player, targetPlayer)
        
    def onSuccess(self, game, player, targetPlayer):
        """ Sends messages to everyone, performs save event.
        """
        if targetPlayer in dyingPlayers:
            BroadcastEvent(targetPlayer.getName() + ' has had a save used on them.')
            SaveEvent(targetPlayer)
        else:
            SendEvent(player, targetPlayer.get(Name) + ' is not dying.')
