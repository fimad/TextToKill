import Queue
from datetime import datetime

from Inbox import Inbox

class Game:
    """ Defines a running instance of a Murder Mystery.
        Handles the initialization of the various game states.
    """
    def __init__(self, abilities, players):
        self.gm = players[0]
        self.players = players[1:]
        self.abilities = abilities
        self.errorAbility = Error()
        self.eventQueue = Queue.PriorityQueue()
        self.parser = Parser()
        self.inbox = Inbox()
        self.outbox = Outbox()

    def getGameMaster(self):
        return self.gm

    def addEvent(self, event):
        """ Schedules an event to be run.
        """
        self.eventQueue.put(event)

    def getOutbox(self):
        return self.outbox

    def isValidPlayer(self, name):
        return name in self.player

    def getPlayer(self, name):
        return self.player[name]

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
        commands = self.parser.parse(self.abilities, newMessages, self.errorAbility)
        for (sender,ability,args) in commands:
            for player in self.players:
                if( player.contact().matches(sender) ): #TODO: sync this with Player once it's written
                    ability.getEventsFor(player, args) #TODO: sync this with Ability once it's written
                    break

        #Process the queue of events
        while( not self.eventQueue.empty() ):
            event = self.eventQueue.get()
            if( event.when() < datetime.now() ):
                event.perform()
            else:
                #Doesn't support peeking, so shove it back in the queue if it
                #shouldn't happen yet
                self.eventQueue.put(event)

