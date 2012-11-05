import re
from Ability import Ability
from Events.SendEvent import SendEvent
from Events.StealEvent import StealEvent
from LimitedUseString import LimitedUseString

class StealAbility(Ability):
    """ Steal items from characters
    """
    def __init__(self):
        Ability.__init__(self, LimitedUseString("Steal",2), ["steal","st"])

    def getEventsFor(self, game, player, args):
        """ Sub-classes must override this method.
            Returns a list of events that perform the state changes.
        """
        return self.guardedEventsFor(game, player, args, StealAbility.onSuccess, True)

    def onSuccess(self, game, player, args, oldName):
        argList = re.split(' from ', args)
        if( len(argList) == 2 ):
            return (True, [StealEvent(player, argList[1], argList[0], oldName)])
        else:
            return (False, [SendEvent(player,"Poorly formatted steal.")])


