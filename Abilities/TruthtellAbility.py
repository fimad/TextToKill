from re import search
from Player import Player
from Game import Game
from Event import Event
from Ability import Ability
from Events.SendEvent import SendEvent

class TruthtellAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Truthtell", ["truthtell","tt"])
    
    def getEventsFor(self,game,player,args):
        """ Calls guardedEventsFor to check if the player has a truthtell.
        """
        return self.guardedEventsFor(game,player,args,TruthtellAbility.onSuccess)
    
    def onSuccess(self,game,player,args):
        """ Parses "rest of string" - should be in the form "on <Player>"
            Sends messages to the player, the target player, and the GM.
            Is called by guardedEventsFor.
        """
        fields = search('on (\w+)', args)
        if fields:
            if fields.group(1) in game.getPlayerNames():
                targetPlayer = fields.group(1)
                events = []
                events.append(SendEvent(game.getPlayer(targetPlayer), player.getName() + ' is using a truthtell on you. Please find the game master.'))
                events.append(SendEvent(player, targetPlayer + ' has been notified. Please find the game master.'))   
                gameMaster = game.getGameMaster()
                events.append(SendEvent(gameMaster, player.getName() + ' is using a truthtell on ' + targetPlayer +'.'))
                return (True,events)
        else: 
            return (False,[SendEvent(player,'Improperly formatted truthtell.')])
