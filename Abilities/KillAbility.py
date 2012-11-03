from Player import Player
from Game import Game
from Event import Event
from Ability import Ability
from PriorityQueue import PriorityQueue

class KillAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Kill", ["kill","k"])
        self.activeKills = {}

    def addActiveKill(self, playerName, event):
        if playerName not in self.activeKills :
            self.activeKills[playerName] = PriorityQueue()
        self.activeKills[playerName].put(event)

    def removeActiveKill(self, playerName):
        if playerName in self.activeKills :
            self.activeKills[playerName].put(event)

    def removeSpecificKill(self, playerName, event):
        if playerName in self.activeKills :
            self.activeKills[playerName].remove(event)

    def getEventsFor(self, game, player, targetPlayer):
        """ Calls guardedEventsFor to check if the player has a kill.
        """
        return guardedEventsFor(self, player, targetPlayer, onSuccess)

    def onSuccess(self, game, player, targetPlayer):
        """ Sends messages to everyone, performs kill event.
        """
        if Game.isValidPlayer(targetPlayer):
            killEvent = KillEvent(targetPlayer)
            addActiveKill(targetPlayer, killEvent)

            events = []
            events.append(BroadcastEvent(targetPlayer.getName() + ' has had a kill placed on them.'))
            events.append(killEvent)
            return (True, events)
        else:
            return (False, SendEvent(player, 'Improperly formatted kill.'))
