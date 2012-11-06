from Player import Player
from Game import Game
from Event import Event
from Ability import Ability
from KillAbility import KillAbility
from Events.SendEvent import SendEvent
from Events.BroadcastEvent import BroadcastEvent

class SaveAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Save", ["save","sa"])

    def getEventsFor(self, game, player, targetPlayer):
        """ Calls guardedEventsFor to check if the player has a save.
        """
        return self.guardedEventsFor(game, player, targetPlayer, SaveAbility.onSuccess)
        
    def onSuccess(self, game, player, targetPlayer):
        """ Sends messages to everyone, performs save event.
        """
        events = []
        if game.isValidPlayer(targetPlayer):
            if game.getAbility("Kill").hasActiveKill(targetPlayer) :
                events.append(BroadcastEvent(targetPlayer + ' has had a save used on them.'))
                killEvent = game.getAbility("Kill").removeActiveKill(targetPlayer)
                game.removeEvent(killEvent)
                return (True, events)
            else:
                events.append(SendEvent(player, targetPlayer + ' is not dying.'))
                return (False, events)
        else:
            return (False, [SendEvent(player, 'Improperly formatted save.')])
