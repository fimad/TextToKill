from datetime import datetime
from datetime import timedelta

class Event:
    def __init__(self, offset=0):
        self.time = datetime.now()+timedelta(0,offset)

    def when(self):
        """ When should this event take place.
        """
        return self.time

    def perform(self, game):
        """ Implement this method in children clases to define the semantics of
            this event.  Game is an instance of the current game.
        """
        pass

    """ Define an ordering based on the time. """
    def __lt__(self, other):
        return self.time < other.time
    def __gt__(self, other):
        return self.time > other.time
    def __eq__(self, other):
        return self.time == other.time
    def __le__(self, other):
        return self.time <= other.time
    def __ge__(self, other):
        return self.time >= other.time
    def __ne__(self, other):
        return self.time != other.time
