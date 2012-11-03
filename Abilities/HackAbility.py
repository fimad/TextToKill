from re import search
from Player import Player
from Event import Event
from Ability import Ability
from Events.SendEvent import SendEvent

class HackAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Hack", ["hack","hk"])
    
    def getEventsFor(self,game,player,args):
        """Hacks another player.
        """
        if game.infectedPlayer  == player:
            if game.isValidPlayer(args) :
                targetPlayer = game.getPlayer(args)
                game.infectedPlayer = targetPlayer
                return [SendEvent(targetPlayer,'You\'ve been infected!')]
            else:
                return [SendEvent(player,'Typo? (Try again!)')]
