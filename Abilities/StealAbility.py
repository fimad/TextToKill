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
        return guardedEventsFor(self, player, args, onSuccess):

    def onSuccess(self, player, args):
        argList = re.split(' from ', args)
        if( argList.size() == 2 ):
            return [StealEvent(p
        else:
            return [SendEvent(player,"Poorly formatted steal.")]


