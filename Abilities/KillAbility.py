from Player import Player
from Game import Game
from Event import Event
from Ability import Ability
from PriorityQueue import PriorityQueue
from Events.KillEvent import KillEvent
from Events.BroadcastEvent import BroadcastEvent
from Events.SendEvent import SendEvent

class KillAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Kill", ["kill","k"])
        self.activeKills = {}
        
    def hasActiveKill(self, playerName):
        """ Does the player have an active kill placed on them?
        """
        return (playerName in self.activeKills) and ( not self.activeKills[playerName].empty() )

    def addActiveKill(self, playerName, event):
        if playerName not in self.activeKills :
            self.activeKills[playerName] = PriorityQueue()
        self.activeKills[playerName].put(event)

    def removeActiveKill(self, playerName):
        if playerName in self.activeKills :
            return self.activeKills[playerName].get()
        return None

    def removeSpecificKill(self, playerName, event):
        if playerName in self.activeKills :
            self.activeKills[playerName].remove(event)

    def getEventsFor(self, game, player, targetPlayer):
        """ Calls guardedEventsFor to check if the player has a kill.
        """
        return self.guardedEventsFor(game, player, targetPlayer, KillAbility.onSuccess)

    def onSuccess(self, game, player, targetPlayer):
        """ Sends messages to everyone, performs kill event.
        """
        if game.isValidPlayer(targetPlayer):
            killEvent = KillEvent(targetPlayer)
            game.getAbility("Kill").addActiveKill(targetPlayer, killEvent)

            events = []
            events.append(BroadcastEvent("An icy shiver runs down your spine. You sense that " + targetPlayer + " is in imminent peril."))
            events.append(killEvent)
            return (True, events)
        else:
            return (False, SendEvent(player, 'Improperly formatted kill.'))
