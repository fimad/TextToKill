from re import search
from Player import Player
from Game import Game
from Event import Event

class CoerceAbility(Ability):

    def __init__(self):
        self.abilityName = 'Coerce'
        self.keywords = ['coerce','co']
    
    def getEventsFor(self,player,args):
        """ Calls guardedEventsFor to check if the player has a Coerce.
        """
        return guardedEventsFor(self,player,args)
    
    def onSuccess(self,player,args)
        """ Checks if the targetPlayer has the ability in question.
        """
        fields = search('(\w+) to use (\w+) on (\w+)',args)
        if fields:
            if fields.group(0) in game.getPlayerNames() and fields.group(2) in game.getPlayerNames():
                coerceTargetPlayer = fields.group(0)
                abilityTargetPlayer = fields.group(2)
            if fields.group(1) in Game.getAbilityNames():
                ability = fields.group(1)
            if coerceTargetPlayer and abilityTargetPlayer and ability:
                return (True, [CoerceEvent(coerceTargetPlayer,ability,abilityTargetPlayer)])
        return (False,[SendEvent(player,"Poorly formatted coerce.")])
        
        
