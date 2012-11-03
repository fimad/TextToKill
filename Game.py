import Queue
from datetime import datetime

from Inbox import Inbox
from Outbox import Outbox
from Parser import Parser
from Abilities.ErrorAbility import ErrorAbility

class Game:
    """ Defines a running instance of a Murder Mystery.
        Handles the initialization of the various game states.
    """
    def __init__(self, abilities, players):
        self.gm = players[0]
        self.errorAbility = ErrorAbility()
        self.eventQueue = Queue.PriorityQueue()
        self.parser = Parser()
        self.inbox = Inbox()
        self.outbox = Outbox()

        self.players = {}
        for player in players[1:]:
            self.players[player.getName()] = player

        self.abilities = {}
        for ability in abilites:
            self.abilities[ability.getName()] = ability

    def getGameMaster(self):
        return self.gm

    def addEvent(self, event):
        """ Schedules an event to be run.
        """
        self.eventQueue.put(event)

    def getOutbox(self):
        return self.outbox

    def isValidAbility(self, name):
        return name in self.player

    def getAbility(self, name):
        return self.abilities[name]

    def getAbilityNames(self):
        return self.abilities.keys()

    def isValidPlayer(self, name):
        return name in self.player

    def getPlayer(self, name):
        return self.player[name]

    def getPlayerNames(self, name):
        return self.players.keys()

    def removePlayer(self, name):
        if( self.isValidPlayer(name) ):
            del self.players[name]

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

