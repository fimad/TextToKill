from datetime import datetime

class Event:
    def __init__(self, time=datetime.now()):
        self.time = time

    def when():
        """ When should this event take place.
        """
        return self.time

    def perform():
        """ Implement this method in children clases to define the semantics of
            this event
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
