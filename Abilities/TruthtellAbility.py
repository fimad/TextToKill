from re import search
from Player import Player
from Game import Game
from Event import Event
from Ability import Ability

class TruthtellAbility(Ability):

    def __init__(self):
        self.abilityName = 'Truthtell'
        self.keywords = ['truthtell','tt']
    
    def getEventsFor(self,player,args):
        """ Calls guardedEventsFor to check if the player has a truthtell.
        """
        return guardedEventsFor(self,player,args)
    
    def onSuccess(self,player,args):
        """ Parses "rest of string" - should be in the form "on <Player>"
            Sends messages to the player, the target player, and the GM.
            Is called by guardedEventsFor.
        """
        fields = search('on (\w+)')
        if fields:
            if fields.group(1) in Game.getPlayerNames():
                targetPlayer = fields.group(1)
                events = []
                events.append(SendEvent(targetPlayer, player.getName() + ' is using a truthtell on you. Please find the game master.'))
                events.append(SendEvent(player, player.getName() + ' has been notified. Please find the game master.'))   
                gameMaster = Game.getGameMaster()
                events.append(SendEvent(gameMaster, player.getName() + ' is using a truthtell on ' + player.getName() +'.'))
                return (True,events)
        else: 
            return (False,[SendEvent(player,'Improperly formatted truthtell.')])
