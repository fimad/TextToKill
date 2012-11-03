from re import search
from Player import Player
from Game import Game
from Event import Event
from Ability import Ability

class CoerceAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Coerce", ["coerce","co"])
    
    def getEventsFor(self,game,player,args):
        """ Calls guardedEventsFor to check if the player has a Coerce.
        """
        return guardedEventsFor(self,player,args)
    
    def onSuccess(self,game,player,args):
        """ Checks if the targetPlayer has the ability in question.
        """
        fields = search('(\w+) to use (\w+) on (\w+)',args)
        if fields:
            if game.isValidPlayer(fields.group(0)) and game.isValidPlayer(fields.group(2)):
                if fields.group(1) in game.getAbility("Kill").getKeyWords() and fields.group(1) in game.getAbility("Save").getKeyWords():
                    coerceTargetPlayer = fields.group(0)
                    abilityTargetPlayer = fields.group(2)
                    ability = fields.group(1)
                    return (True, [CoerceEvent(coerceTargetPlayer,ability,abilityTargetPlayer)])
        return (False,[SendEvent(player,"Poorly formatted coerce.")])
        
        
