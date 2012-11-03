from Ability import Ability
from Events.SendEvent import SendEvent

class StealAbility(Ability):
    """ Steal items from characters
    """
    def __init__(self):
        Ability.__init__(self, "Error", [])

    def getEventsFor(self, player, errorMessage):
        """ Sub-classes must override this method.
            Returns a list of events that perform the state changes.
        """
        return [SendEvent(player, errorMessage)]

