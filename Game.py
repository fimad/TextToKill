import Queue
from datetime import datetime

class Game:
""" Defines a running instance of a Murder Mystery.
    Handles the initialization of the various game states.
"""
    def __init__(self):
        self.players = []
        self.abilities = []
        self.eventQueue = Queue.PriorityQueue()
        self.inbox = nil #TODO: define me!
        self.parser = nil #TODO: define me!

    def addEvent(self, event):
    """ Schedules an event to be run.
    """
        self.eventQueue.put(event)

    def run(self):
    """ Run the game, and Don't stop.
        Ever.
    """
        while( True ):
            step()

    def step(self):
    """ Perform one step of the game logic.
        You need to call this repeatedly to make the game run.
    """
        #process incoming messages
        newMessages = self.inbox.poll()
        commands = self.parser.parse(self.abilities, newMessages)
        for command in commands:
            pass

        #Process the queue of events
        while( !self.eventQueue.empty() ):
            event = self.eventQueue.get()
            if( event.when() < datetime.now() ):
                event.perform()
            else:
                #Doesn't support peeking, so shove it back in the queue if it
                #shouldn't happen yet
                self.eventQueue.put(event)

