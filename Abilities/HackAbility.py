from re import search
from Player import Player
from Game import Game
from Event import Event
from Ability import Ability

class HackAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Hack", ["hack","hk"])
    
    def getEventsFor(self,game,player,args):
        """Hacks another player.
        """
        if Game.isValidPlayer(args):
            targetPlayer = Game.getPlayer(args)
            return (True, [SendEvent(targetPlayer,'You\'ve been infected!')])
