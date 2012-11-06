from re import search
from Player import Player
from Game import Game
from Event import Event
from Ability import Ability
from Events.SendEvent import SendEvent
from Events.CoerceEvent import CoerceEvent

class CoerceAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Coerce", ["coerce","co"])
    
    def getEventsFor(self,game,player,args):
        """ Calls guardedEventsFor to check if the player has a Coerce.
        """
        return self.guardedEventsFor(game, player, args, CoerceAbility.onSuccess)
    
    def onSuccess(self,game,player,args):
        """ Checks if the targetPlayer has the ability in question.
        """
        fields = search('(\w+) to use (\w+) on (\w+)',args)
        if fields:
            print "GOT FIELDS!"
            print "'"+fields.group(0)+"'"
            print "'"+fields.group(1)+"'"
            print "'"+fields.group(2)+"'"
            print "'"+fields.group(3)+"'"
            if game.isValidPlayer(fields.group(1)) and game.isValidPlayer(fields.group(3)):
                print "VALID PLAYERS"
                if fields.group(2) in game.getAbility("Kill").getKeywords() or fields.group(2) in game.getAbility("Save").getKeywords():
                    print "VALID KEYWORDS!"
                    coerceTargetPlayer = fields.group(1)
                    abilityTargetPlayer = fields.group(3)
                    ability = fields.group(2)
                    return (True, [CoerceEvent(coerceTargetPlayer,ability,abilityTargetPlayer)])
        return (False,[SendEvent(player,"Poorly formatted coerce.")])
        
        
