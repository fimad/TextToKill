import re
from Ability import Ability
from Events.SendEvent import SendEvent

class StealAbility(Ability):
    """ Steal items from characters
    """
    def __init__(self):
        Ability.__init__(self, LimitedUseString("Steal",2), ["steal","st"])

    def getEventsFor(self, player, args):
        """ Sub-classes must override this method.
            Returns a list of events that perform the state changes.
        """
        return guardedEventsFor(self, player, args, onSuccess, True):

    def onSuccess(self, player, args, oldName):
        argList = re.split(' from ', args)
        if( argList.size() == 2 ):
            return (True, [StealEvent(player, argList[1], argList[0], oldName)])
        else:
            return (False, [SendEvent(player,"Poorly formatted steal.")])


